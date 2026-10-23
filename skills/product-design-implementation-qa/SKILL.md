---
name: product-design-implementation-qa
description: Implement a supplied product design or reference and verify the rendered interface across relevant states and viewport sizes.
---

# Product Design Implementation and QA

Use when implementing an approved design, screenshot, mockup, or visual reference in an existing application, or when checking the visual quality of a UI change.

## Implement

- Inspect the existing stack, components, styles, and responsive behavior before editing.
- Identify what must match the reference and what may adapt to the product's established patterns.
- Preserve working behavior and accessibility. Use existing components where they fit.
- Implement responsive layout and relevant interaction states, not only the reference viewport.
- Do not introduce dependencies or replace architecture unless the task requires it.

## Verify

- Run the app and inspect the rendered result when tools allow.
- Compare the result against the supplied reference at matching viewport dimensions.
- Check at least one narrow and one wide viewport when layout changes; inspect relevant empty, loading, error, and success states.
- Test keyboard navigation, visible focus, labels, and interaction feedback for changed controls.
- Fix visible regressions and inspect the updated rendering.
- If visual inspection or a state cannot be tested, say exactly what remains unverified. Do not claim pixel accuracy, usability, or accessibility based only on source code.
