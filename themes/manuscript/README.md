# manuscript

A theme for notebooks that want to read like a printed journal article: ink on
paper, old-style serifs, and prose set tight.

## Design

**Colours.** Light mode is warm paper (`#fdfbf6`) with near-black ink
(`#1c1a17`); dark mode inverts it to a slate-brown page with a bone-white ink.
Accents are borrowed from print conventions rather than from a syntax palette:
journal maroon for primary actions and links (the classic `hyperref` colour),
plum for visited links, and a faded highlighter yellow for the action colour.
Shadows are nearly flat — paper doesn't float.

**Fonts.** All from Google Fonts:

-   Text: [EB Garamond](https://fonts.google.com/specimen/EB+Garamond) — a
    compact old-style serif that packs a lot of words into a line.
-   Headings: [Spectral](https://fonts.google.com/specimen/Spectral) — a sturdier
    serif that holds up at heading weights.
-   Monospace: [IBM Plex Mono](https://fonts.google.com/specimen/IBM+Plex+Mono) —
    pairs cleanly with the serifs without shouting.

`--radius` is `3px`, so cells and controls read as boxes on a page rather than
cards in an app. The column is widened from marimo's default `740px` to `860px`
(`--content-width`), since a dense serif fits more words into the same measure.

## Typography

Unlike the other themes in this repository, `manuscript` also sets a few rules
on the `.markdown` blocks, because "dense" is a matter of layout as much as
colour:

-   Body text is justified with automatic hyphenation, on a `1.42` line height.
-   Consecutive paragraphs are indented instead of being separated by blank
    space.
-   `h1` is centred, like a paper title; `h2` and `h3` are set in small caps.
-   Block quotes are indented extracts rather than decorated callouts, and
    tables are set slightly smaller.
-   Code blocks and display maths are excluded from the justification and
    hyphenation.

If you would rather keep marimo's default prose layout, delete everything below
the `/* Typography */` comment in `manuscript.css`; the colours and fonts stand
on their own.
