# Rendering and figure policy

Status: **Informative — documentation tooling policy**.

Tracked by: [zyx-corporation/kotonoha-docs#20](https://github.com/zyx-corporation/kotonoha-docs/issues/20)

## Purpose

`kotonoha-docs` uses diagrams and public-facing pages to explain Kotonoha concepts. These materials are non-normative: they help readers understand SLS, RDE, semantic lineage, and related workflows, but they do not replace the canonical specification in [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec).

This policy defines how SVG figures, Markdown sources, CSS, and HTML publication pages should be organized.

## Principle

Figures in `kotonoha-docs` should generally be written as **SVG**.

SVG is preferred because it is:

- text-based and reviewable in Git;
- scalable for web and print;
- easy to link from Markdown and HTML;
- compatible with static publishing;
- suitable for RDE-style review of visual meaning changes.

## Two supported authoring paths

`kotonoha-docs` supports two publication paths.

| Path | Use when | Source | Output |
| --- | --- | --- | --- |
| Markdown + SVG directive + preprocessor | The page is mostly prose with one or more SVG figures | `.md` plus SVG files | Generated `.html` |
| Direct HTML | The page needs custom layout, interaction, or precise visual composition | `.html` plus SVG/CSS/JS as needed | Authored `.html` |

The Markdown + preprocessor path is the default for ordinary explanatory pages. Direct HTML is allowed when the page would become awkward or fragile as Markdown.

## Directory conventions

Recommended locations:

```text
en/
ja/
assets/svg/
assets/css/
tools/render_docs.py
```

Language-specific pages should live under `en/` or `ja/`. Shared SVG and CSS assets may live under `assets/` when they are language-neutral. Language-specific SVG assets may use subdirectories such as `assets/svg/en/` and `assets/svg/ja/` when text is embedded inside the SVG.

## Markdown SVG directive

The minimal renderer in [`tools/render_docs.py`](../tools/render_docs.py) recognizes the following directive:

```text
:::svg path="../../assets/svg/example.svg" alt="Example" caption="Example figure"
:::
```

This expands to an HTML `<figure>` containing an `<img>` and optional `<figcaption>`.

The directive should be used when the SVG is explanatory, static, and externally reviewable.

## Rendering command

Example:

```bash
python3 tools/render_docs.py en/concepts/example.md site/en/concepts/example.html --css ../../../assets/css/kotonoha-docs.css --title "Example"
```

The renderer intentionally supports only a small Markdown subset. It is not a replacement for a full static-site generator. If a page requires tables, complex layout, interactive behavior, or fine-grained publication control, use direct HTML or introduce a separate documented build step through a future Issue.

## Direct HTML path

Use direct HTML when:

- layout is central to the explanation;
- SVG needs to be embedded inline for styling or interaction;
- JavaScript is necessary;
- the page is a public mini-site or chapter page;
- print/PDF behavior requires explicit control.

Direct HTML pages should still use shared CSS where possible and should keep SVG assets as separate files unless inline SVG is required.

## Figure rules

1. Prefer SVG over raster images for conceptual diagrams.
2. Avoid unreadable text embedded in diagrams unless the SVG is language-specific.
3. Keep SVG source reviewable and reasonably small.
4. Include alt text when rendering SVG into HTML.
5. Keep captions close to the figure.
6. Treat diagrams as explanatory unless a specification explicitly says otherwise.
7. Link to `kotonoha-spec` when a diagram illustrates a normative concept.

## RDE review for diagrams

When changing SVG or rendered pages, reviewers should check:

| Check | Question |
| --- | --- |
| Preserved | Does the diagram preserve the original conceptual relation? |
| Transformed | Does visual simplification change the meaning? |
| Complemented | Did the figure add a helpful but non-normative explanation? |
| Unresolved | Are omissions or simplifications visible to readers? |
| Drift risk | Could the diagram be mistaken for a stronger claim than the prose supports? |

## Boundary

This policy is about public documentation rendering. It does not define SLS semantics, RDE categories, interchange compatibility, or conformance obligations. Those remain in `kotonoha-spec`.
