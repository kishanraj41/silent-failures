# Related work scan (Nov 2, 2026, ~1 hour)

Purpose: know what has been written about silent data/ML failures before writing a paper, so the gap is real. Status per entry: **fetched** = abstract/page read today; **search-hit** = found, not read; verify before citing numbers.

## Closest prior work

| Work | What it covers | Gap vs this corpus |
|---|---|---|
| Tambon et al., *Silent bugs in deep learning frameworks: an empirical study of Keras and TensorFlow* (arXiv 2112.13314, 2021; later EMSE). **fetched** | 1,168 closed Keras issues → 77 reproducible silent bugs; "wrong behaviour without crash, hang or error"; threat levels; survey of 103 devs | Framework-internal bugs, not pipeline/data incidents in the wild. Shares the definition of "silent". |
| Foidl, Felderer, Ramler, *Data smells: categories, causes and consequences, and detection of suspicious data in AI-based systems* (arXiv 2203.10384, CAIN 2022). **fetched** | 36 data smells in 3 categories (believability, understandability, consistency); detection on 240+ datasets | Smells are latent properties of datasets; no incidents, no detection-mechanism or cost data. |
| Foidl, Golendukhina, Ramler, Felderer, *Data pipeline quality: influencing factors, root causes of data-related issues, and processing problem areas for developers* (arXiv 2309.07067, JSS 2024). **fetched** | 41 influencing factors (MLR + 8 interviews); mined GitHub + Stack Overflow; 33% of data-related issues from incorrect data types, 35% in cleaning; 47% of developer questions on integration/ingestion | Closest empirical cousin. Issue-level, developer-question-level; does not study *silent wrong outputs that reached a consumer*, time-to-detect, or who detected. |
| Kapoor & Narayanan, *Leakage and the reproducibility crisis in ML-based science* (Patterns 2023; arXiv 2207.07048). **fetched** | 20 surveys across 17 fields, 329 affected papers; 8 leakage types; model info sheets | Leakage only; our corpus has leakage as one mechanism class among ~15. |
| Sambasivan et al., *"Everyone wants to do the model work, not the data work": data cascades in high-stakes AI* (CHI 2021). **search-hit** | Interview study; data cascades = compounding downstream effects of upstream data issues; high prevalence | Qualitative, practitioner-reported; no incident catalogue. |
| Morán et al., *A taxonomy of defects in massive data processing programs* (Zenodo supplement, 2026). **search-hit** | Defect taxonomy for big-data programs (Spark/MapReduce-class) | Program defects, not production incidents. Read before writing related work. |
| Grafberger, Schelter et al., mlinspect: *Lightweight inspection of data preprocessing in native ML pipelines* (CIDR 2021); *Data distribution debugging in ML pipelines* (VLDBJ 2022); ArgusEyes; *Instrumentation and analysis of native ML pipelines via code rewriting* (arXiv 2407.07560, 2024). **search-hit** | Monkey-patching / rewriting pandas+sklearn pipelines to extract intermediate results and lineage; single-run inspections (distribution issues) | Tooling, not incidents. Must be cited as the closest capture mechanism to AutoLineage; our differentiator is run-to-run diff with line attribution and incident-grounded checks. |
| Breck et al., *Data validation for ML* (SysML 2019, TFDV); Schelter et al., Deequ (VLDB 2018); Hynes et al., *The data linter* (2017). **search-hit** | Declarative/suggested constraints on tables; schema + distribution skew | Checks are statistical and table-level; none cites the incident that motivated a check. |
| Dixit et al., *Silent data corruptions at scale* (arXiv 2102.11245, 2021); Hochschild et al., *Cores that don't count* (HotOS 2021). **search-hit** | Hardware-level silent wrong results at fleet scale | Establishes the term and the detection problem one layer down; useful framing. |

## What nobody has (the gap, as of this scan)

1. An **incident corpus**: real, dated, sourced cases where a data/ML/AI system produced a *wrong output that reached a consumer* without an error, with mechanism, **who detected it and how**, time-to-detect, and cost.
2. The finding the corpus already suggests at n=27: detection is overwhelmingly **human or external** (plausibility, cross-check, replication, disclosure), almost never a tool. Nobody has measured that.
3. **Checks with receipts**: each check in a library traced to the incident that needed it.

## Candidate venues (verify in December, not now)
- DEEM 2027 (SIGMOD workshop, US). ACM JDIQ (data quality journal). MSR 2027 is Dublin → out. ESEM/EMSE → long.

## Not read yet, read before submitting
- Humbatova et al., *Taxonomy of real faults in deep learning systems* (ICSE 2020). Islam et al., FSE 2019 DL bugs. Morovati et al., *Bugs in ML-based systems: a faultload benchmark* (EMSE 2023). Pimentel et al., notebook reproducibility (MSR 2019). Polyzotis et al., *Data lifecycle challenges in production ML* (SIGMOD Record 2018).
