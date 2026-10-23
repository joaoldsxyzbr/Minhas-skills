# Conditional reason for a delivery not received

## Goal and scope

Let a checker record a delivery as **not received** using **Closed shop**, **Missing documents**, or **Other**. Only Other requires explanatory text. Keep existing records readable for their currently authorized viewers across admin, checker, and supplier roles. Use the existing vanilla JavaScript architecture, with no dependencies or analytics. This deliverable is a plan; implementation and deployment are excluded.

Evidence: `exercises/design/brief.md` is the only supplied product file. Source paths, persistence format, current role permissions, and text length limits are unknown. Confirm these in step 1; preserve current permissions and limits. Do not invent or broaden access.

## Actionable sequence

1. **Locate integration points.** Identify the actual paths for the checker form, validation/submission handler, persistence contract, and all authorized record-detail/history views. Inspect legacy examples and existing checks. Record those paths before editing; no application source was supplied with this exercise.
2. **Specify regression cases before changing behavior.** Cover the acceptance matrix below using the existing test setup; otherwise propose native `node --test` for isolated JavaScript logic. First demonstrate the current failure: a predefined reason cannot submit without free text. Test commands and runtime results remain unverified in this plan.
3. **Update the checker form and validation together.** Keep the existing reason control and explicit Save action. Show a labeled required explanation field only for Other. When hidden, remove it from keyboard navigation and required validation. Validate the selected value; trim Other text and reject empty/whitespace-only input with an associated inline error. Move focus to the first invalid visible control after failed submission. Do not submit automatically on selection.
4. **Update submission and compatibility.** Use stable reason values mapped to display labels, adapting to the existing contract. Send explanatory text only for Other; enforce the same rule at the existing authoritative validation boundary if present. Keep any unsaved Other draft during reason switching within the current form, but omit it when saving a predefined reason and clear it on successful save or cancellation. Do not rewrite historical records. Readers must support the existing format and the new format: retain historical explanations even for predefined reasons, show legacy free text without requiring a recognized code, and provide a readable fallback for unknown or missing codes. Render stored text safely as text.
5. **Verify the complete flow when a runtime is available.** Exercise each case below, keyboard navigation, error announcements, and authorized role views. Check save failure and retry using the existing submission conventions. Review the diff for unrelated changes, new dependencies, analytics, or permission changes. No deployment is included.

## Acceptance criteria and edge cases

| Scenario | Expected result |
| --- | --- |
| Closed shop or Missing documents | Explanation is hidden and not required; save succeeds with the selected reason and no new explanation. |
| Other with meaningful text | Explanation is visible and required; trimmed text is saved and displayed with the reason. |
| Other empty or whitespace-only | Save is blocked; a clear, programmatically associated error identifies the explanation field. |
| No selection or unsupported submitted value | Save is blocked with a useful reason error; forged values fail at the existing authoritative boundary. |
| Other → predefined → Other | Hidden text cannot block validation or leak into a predefined-reason save; unsaved draft returns when switching back within the form. |
| Save fails or the user retries | Show the existing error/retry treatment, preserve input, and avoid duplicate submissions using existing conventions. |
| Cancel or successful save, then reopen | No stale explanation from the previous interaction appears. |
| Historical free text, old reason plus text, unknown/missing code | Existing information remains readable without migration, forced re-entry, or silent text loss. |
| Long text or markup-like text | Existing length rules apply consistently; text displays safely without executing markup. |
| Admin, checker, supplier | Existing viewing and editing permissions remain intact; each authorized record view supports old and new records. |
| Keyboard and assistive technology | Reason and explanation have labels; required/error state is conveyed; hidden fields receive no focus. |

## Validation limits and workflow

Plan reviewed against every requirement in the brief. No source inspection, executable behavior tests, browser interaction, screenshots, visual QA, or usability research was possible; none is claimed. Final source paths and contract details must be resolved during step 1.

Skills: local **using-minhas-skills** and its shared rules selected **writing-plans** as the lead. **product-design-ideation** was consulted only to confirm that this specified, small change does not need another discovery cycle. No alternative concepts, approval gates, implementation, or remote operations are required for this deliverable.
