# Design DNA: Act's Paint & Body Shop

- **Hero archetype:** photo diptych. Centered serif headline, then the shop's own before (sanded to metal) and next (in primer) photos tilted left and right, with the paint deck, pitch and buttons in the middle column. New in the portfolio.
- **Signature motif:** the paint deck. Five chips in the order a tri-coat goes on: bare metal, primer, base, pearl, clear. They rise into place when they scroll into view. Used in the hero (with labels), the services heading, every subpage header, the 404 and the top of the footer (5 uses). It comes from a review: a metallic tri-coat matched in under 48 hours.
- **Motion:** fade plus 20px rise on `.rv`; chips scale up from the bottom with a short stagger. No blur. Reduced motion shows everything.
- **Type:** Gloock (display, a high contrast serif with some church bulletin warmth) plus Hanken Grotesk (body, 18px, line height 1.65). Self-hosted woff2 latin subsets, preloaded.

| Token | Hex | Use |
|---|---|---|
| soot | #1d1815 | dark band, footer, demo bar |
| brick | #9a3b22 | buttons (white text), marks, headline accent |
| brick-dk | #7a2c17 | small brick text on cream |
| gold | #d39a3a | tobacco gold accents on dark, stars, placeholder tags |
| cream | #f7f1e6 | page |
| card | #fffaf2 | cards |
| primer | #b3ada3 | primer chip, rules |
| pearl | #ebe5ee | pearl chip |

- **Section shapes:** diptych hero; "On the clock" dark band of four time stamps; "Paying out of pocket?" split with a review; services as a ruled menu; reviews with a lead card; footer closing spread ("Call Pastor Al for a quote.").
- **Buttons:** pill shaped, brick with white text; outline variant.
- **Placeholders:** gold pill tag "PLACEHOLDER" plus a striped box for photos.
