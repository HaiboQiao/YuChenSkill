---
name: frontend-design-codex
description: Use when Codex is building, revising, or reviewing a browser-rendered frontend UI (including Electron/Tauri Web frontends), web app screen, responsive layout, component surface, dashboard view, form flow, visual system, or no-template product interface that needs visual polish, accessibility, screenshots, or browser QA. Excludes native Qt Widgets, QML and non-Web Flutter interfaces.
---

# Frontend Design Codex

## Scope and Coordination

Follow the user's requested mode and the existing project UI stack. Analysis/audit and review-only requests do not authorize code changes, dependency installation or persisted design files. Design-only requests produce a proposal; explicit implementation requests permit scoped UI edits. Preserve business behavior.

When `adaptive-ui-workflow` applies, read its entrypoint and use its current brief, scope, stack routing and delivery criteria. This helper contributes only its assigned phase; do not generate a competing redesign, switch frameworks, or treat a helper instruction as broader authorization. Apply numeric/platform examples only to matching targets and distinguish actual visual evidence from static inference.

## Overview

Use this skill to make browser-rendered product interfaces feel intentional, usable, and verified. Prefer the existing app framework and design conventions before adding new abstractions.

## Design Upskill Contribution

This skill teaches Codex to judge frontend design from rendered behavior rather than source code alone. It improves no-template work by forcing the agent to choose layout, hierarchy, spacing, controls, responsive states, accessibility, and screenshot evidence as one loop.

It matters because product UI without a template can easily become decorative or inconsistent. Codex should make useful interfaces that hold up under repeated use, mobile wrapping, and real browser rendering.

## Workflow

1. Inspect the existing app structure, framework, routes, components, styles, and design conventions.
2. Identify the primary user workflow and optimize the first screen for that workflow.
3. Define semantic design tokens before styling repeated components: background, surface, text, muted text, border, accent, status colors, type, spacing, and radius. Check contrast and keep the palette compact.
4. Build the smallest complete UI that covers normal, empty, loading, error, and narrow viewport states.
5. Use familiar controls: icon buttons for tools, toggles for binary choices, sliders or inputs for numbers, tabs for alternate views, and menus for option sets.
6. Apply the visual tokens consistently to core surfaces, controls, charts, and annotations. Keep typography and layout scaled to the surface; avoid hero-scale text inside compact panels.
7. Capture screenshots at the product's supported desktop and narrow viewport or desktop window sizes before claiming visual quality.
8. Revise tokens and layout until screenshot evidence supports the design decisions.

## Browser Evidence Tools

Use available agent browser/screenshot tools or the project's existing browser test setup for actual rendering, screenshots, console and request failures. Inspect overflow, contrast, focus, accessible names and text fit with those tools and manual screenshot review. Check the real app's theme/token files first.

The upstream repository's `.shared/visual-runtime` is not bundled in this standalone user skill. Do not assume its capture/lint/contact-sheet scripts exist, fetch them silently, or install a new runtime. Use a compatible already-available tool. If rendering or screenshot capture is unavailable, report the missing evidence explicitly and complete the checks that remain possible.

Capture viewport sizes the product supports: desktop and narrow/mobile for responsive Web apps; minimum/default window sizes for desktop-only Web shells. Browser evidence does not verify Electron/Tauri host integration by itself.

## Verification

Before completion:

- run the app's normal build/test/lint command when available;
- capture screenshots at the supported viewport/window sizes;
- use available layout/accessibility/console checks and address verified blockers;
- inspect screenshots for responsive UI, accessibility, hierarchy, text fit, controls, spacing, palette, typography, and token consistency;
- preserve screenshot evidence and note any accepted tradeoffs.

## Common Mistakes

- Building a landing page when the user asked for a usable app.
- Inventing a visual language that conflicts with the existing app.
- Shrinking text to fix density instead of reducing content.
- Claiming responsive quality without a mobile screenshot.
