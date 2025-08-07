# Style Guide

## Voice and Perspective

- Primary voice: Neutral, professional third person.
- Case studies/anecdotes: Clearly attributed and minimal first person ("In one engagement, the team observed…").
- Avoid personal "I" unless part of a boxed case study.

## Tone

- Practical, instructional, inclusive.
- Prefer plain English over jargon; explain acronyms on first use.

## British English Spelling

Use: organisation, modernisation, behaviour, colour, optimise, analyse, empathise.

## Terminology Consistency

- GitHub Copilot (first use per chapter), thereafter: Copilot.
- Large-scale (hyphenated when adjectival: "large-scale change"; otherwise: "at large scale").
- Codebase (one word).
- AI-assisted development (hyphenated when before noun).
- Legacy system / heritage system (avoid "old code").
- Continuous integration (CI), continuous delivery (CD) after first expansion.

## Structural Conventions

Chapters should follow:

1. Purpose (why this matters)
2. Context / Problem
3. Practices / Patterns / Techniques
4. Case Insight(s)
5. Risks / Anti-patterns
6. Metrics / Validation
7. Key Takeaways (bulleted, 5–7 max)

## Headings

- One H1 per chapter file.
- Use sentence case for headings (except proper nouns).

## Lists

- Use hyphen (-) for unordered lists.
- Use ordered lists only for sequences.

## Inclusive Language

- Use "team", "people", "developers"; avoid gendered terms.
- Avoid ability assumptions (e.g. "simple"); prefer "straightforward", "clear".
- Avoid metaphors that rely on culture-specific references.

## Accessibility

- Provide alt text for images (future addition).
- Code blocks: annotate non-obvious sections with brief comments.

## Markdown Conventions

- Wrap lines at ~100 characters (soft wrap acceptable).
- Use backticks for filenames, code symbols, commands.
- Prefer reference links for repeated URLs.

## Prompt References

When describing prompt workflows, format inline like: `/improve-test-coverage`.

## Case Studies

Format:

> Case: Legacy Test Expansion (Finance Platform)
> Challenge: ...
> Approach: ...
> Outcome: ...

## Key Takeaways Block

Use final section:

### Key Takeaways

- ...

## Quality Checklist (per chapter)

- [ ] Third-person professional voice
- [ ] British English spelling
- [ ] Terminology matches Style Guide
- [ ] Acronyms defined on first use
- [ ] No placeholder text
- [ ] Inclusive language
- [ ] Headings structured correctly
- [ ] Key Takeaways section present
- [ ] Spelling/grammar pass
- [ ] markdownlint clean

## Prohibited / To Fix

| Issue | Replace With |
|-------|--------------|
| guys | team / everyone |
| master/slave | primary/replica or main/secondary |
| simply / just (when minimising effort) | (remove) or clearly explain |
| whitelist/blacklist | allowlist/denylist |
| sanity check | validation check |

## Metrics Wording

Use: cycle time, lead time, coverage ratio, change failure rate, mean time to recovery (MTTR).

---

This guide evolves; propose changes via Pull Request.
