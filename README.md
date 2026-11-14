# silent-failures

A public corpus of real incidents where a data, ML or AI system **ran without error and produced a wrong output that reached people**: a dashboard, a paper, a payment, a public-health count, a decision.

Each incident records what broke, **who caught it and how**, how long it ran, what it cost, and the check that would have caught it. Each one cites a public source.

**Version 0.1 (Nov 2026):** 27 silent incidents (1983–2026), 2 context-only cases, 8 mechanism reports, 3 runnable reproductions.

## What's here

| Path | Contents |
|---|---|
| `data/incidents.csv` | 29 rows: 27 silent incidents with documented harm, plus 2 marked `context-only` |
| `data/mechanisms.csv` | 8 public bug reports showing a mechanism that produces silent wrong output, where harm to a consumer isn't documented, plus 1 contrast case caught by a declared test |
| `repros/` | Minimal pandas scripts that reproduce a mechanism with synthetic data (not the original data or exact figures) |
| `docs/related_work.md` | Prior research and how this corpus differs |
| `docs/DATA_DICTIONARY.md` | Column definitions |

## What the corpus shows so far

**Who caught it (27 silent incidents):** outsiders (10), insiders, usually after damage (11), users, maintainers or volunteers (4), courts (1), unknown (1). **None** was caught by monitoring or anomaly detection.

**Could a check that needs no business knowledge have caught it?** (`generic_check`)

| Answer | Count |
|---|---|
| Yes: row-count conservation, monotonic cumulative series, unique keys and timestamps, freshness, run-to-run distribution diff, train/test overlap | 13 |
| Partly | 9 |
| No: needs a written business rule, a unit declaration, or ground-truth outcomes | 5 |

**Read these numbers carefully.**
- The corpus only contains failures that became public. Failures caught early by tools rarely do. So this does **not** show that tools fail. It shows what the failures that got through have in common, and how long they ran.
- The `generic_check` answers are the author's judgement and have not been independently validated.

## Running the reproductions

```
pip install pandas numpy
python repros/repro_002_vse_truncation.py
```

Each script ends with a wrong number and a clean exit, then shows the check that catches it.

## Adding or correcting an incident

Corrections are very welcome, especially from the people involved in an incident. Open an issue or a pull request. A row needs:

1. a dated public source
2. evidence that the wrong output reached someone
3. how it was detected, not just that it was

See `CONTRIBUTING.md`.

## License

- Data (`data/`, `docs/`): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- Code (`repros/`): MIT

## Citation

See `CITATION.cff`. Kishan Raj VG, *silent-failures: a corpus of real silent data and ML pipeline failures*, 2026.
