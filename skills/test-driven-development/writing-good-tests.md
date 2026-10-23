# Writing good tests

This companion file is from the Superpowers project and is distributed under the MIT License. It is retained because the upstream TDD skill links to it.

## Principles

- Name the behavior being tested and the change that should make the test fail.
- Assert on observable results, not on mock call counts or private implementation details.
- Keep each test focused on one behavior and make failure output useful.
- Use real collaborators where practical. When a mock is necessary, understand and document the dependency side effects it replaces.
- Keep test-only helpers out of production code.
- Include meaningful boundary, invalid-input, and failure cases.
