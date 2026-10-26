"""Local, evidence-gated summary of independent routing exercises; no network or telemetry."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RESULTS = {"pass", "fail", "blocked", "not_run"}
INVOCATION = {"observed", "wrong", "not_observable"}


def evaluate(cases_path, observations_path, version):
    cases = json.loads(Path(cases_path).read_text(encoding="utf-8"))
    if not isinstance(cases, list) or not all(
        isinstance(c, list) and len(c) == 2 and
        all(isinstance(s, str) and s.strip() for s in c) for c in cases
    ):
        raise ValueError("Routing cases must be [id, prompt] pairs")
    ids = [case[0] for case in cases]
    if len(set(ids)) != len(ids):
        raise ValueError("Duplicate routing case IDs")

    data = json.loads(Path(observations_path).read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("version") != version:
        raise ValueError("Observation version must match the evaluated plugin version")
    if not re.fullmatch(r"[0-9a-f]{40}", str(data.get("revision", ""))):
        raise ValueError("Provide a 40-character revision SHA for the evaluated source")
    observations = data.get("observations")
    if not isinstance(observations, list):
        raise ValueError("observations must be a list")

    seen = set()
    counts = Counter({"not_run": len(ids), "pass": 0, "fail": 0, "blocked": 0})
    observed_invocations = 0
    for entry in observations:
        if not isinstance(entry, dict):
            raise ValueError("Each observation must be an object")
        case_id = entry.get("id")
        if case_id not in ids or case_id in seen:
            raise ValueError("Unknown or repeated case ID: " + str(case_id))
        seen.add(case_id)
        result = entry.get("result")
        invocation = entry.get("skill_invocation", "not_observable")
        evidence = entry.get("evidence", "")
        skill_evidence = entry.get("skill_evidence", "")
        if result not in RESULTS or invocation not in INVOCATION:
            raise ValueError("Invalid result or skill_invocation for " + case_id)
        if not isinstance(evidence, str) or not isinstance(skill_evidence, str):
            raise ValueError("Evidence must be text for " + case_id)
        if result == "not_run":
            if evidence.strip() or invocation != "not_observable" or skill_evidence.strip():
                raise ValueError("An unrun scenario cannot have an observed result: " + case_id)
        elif not evidence.strip():
            raise ValueError("Executed scenario requires independent evidence: " + case_id)
        if invocation != "not_observable":
            if result == "not_run" or not skill_evidence.strip():
                raise ValueError("Observed skill use needs independent evidence: " + case_id)
            observed_invocations += 1
        counts["not_run"] -= 1
        counts[result] += 1

    return {
        "version": version,
        "revision": data["revision"],
        "total": len(ids),
        "pass": counts["pass"],
        "fail": counts["fail"],
        "blocked": counts["blocked"],
        "not_run": counts["not_run"],
        "skill_invocation_observed_or_wrong": observed_invocations,
        "note": "Human-entered evidence is not independently verified by this script; "
                "results do not prove automatic ChatGPT skill activation.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--observations", type=Path, required=True,
                        help="Local JSON outside the repository, never commit private transcripts")
    parser.add_argument("--cases", type=Path, default=ROOT / "tests/routing-requests.json")
    args = parser.parse_args()
    version = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))["version"]
    try:
        summary = evaluate(args.cases, args.observations, version)
    except (ValueError, OSError, json.JSONDecodeError) as error:
        parser.exit(1, "INVALID: " + str(error) + "\n")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
