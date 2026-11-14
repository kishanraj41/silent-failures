# Data dictionary

Both CSVs share these columns.

| Column | Meaning |
|---|---|
| id | Stable ID (SF-NNN). Never reused |
| status | `silent-incident (harm shown)`, `context-only`, `mechanism (harm not shown)`, or `caught-by-declared-test` |
| title | One-line summary |
| year | Year the failure was disclosed or occurred |
| org_or_repo | Organization, or `owner/repo #issue` |
| domain | Field (public health, finance, ML research, ...) |
| system_type | Spreadsheet, pandas script, ETL, ML model, agent, ... |
| layer | Where it broke: ingest, transform, join, aggregate, model, decision logic |
| mechanism_class | Failure mechanism (type coercion, merge fan-out, truncation, DST, leakage, ...) |
| cause_short | What happened, from the source |
| detection_how | How the wrong output was noticed |
| detected_by | outsider, insider, user, maintainer, volunteers, declared test, ... |
| time_to_detect | From start of the failure to detection, as stated or estimated from the source |
| cost_stated | Cost or harm as stated by the source |
| fix | What was done |
| reproducible_in_python | yes / pattern / partial / no |
| check_that_catches | A check that would likely have caught it |
| evidence_level | primary (issue, filing, paper, transcript), reputable-secondary (named outlet), or a VERIFY note |
| source_url | Main source |
| notes | Caveats |
| generic_check | Could a check needing no domain knowledge have caught it: yes / partial / no, plus which check (author's judgement) |
