"""NOTE: reproduces the mechanism with synthetic data, not the original data or exact figures.
SF-004: Vancouver Stock Exchange index, 1982-83.

The index started at 1000.000 in Jan 1982 and was truncated (not rounded) to
three decimals after each of ~3,000 daily updates. The truncated value seeded
the next update. By Nov 1983 it read 524.811; the corrected value was 1098.892.
Sources: WSJ 1983-11-08; Toronto Star 1983-11-29 (via Wikipedia).

This script reproduces the mechanism, not the exact price path: random
zero-mean updates, truncation after each, 22 months x ~22 trading days x 3,000.
Run: python repro_002_vse_truncation.py
"""
import math
import numpy as np

rng = np.random.default_rng(1)
updates_per_day, days = 3000, 460  # ~22 months of trading days
truncated = exact = 1000.0
steps = rng.normal(0, 0.0001, updates_per_day * days)  # tiny relative moves, zero mean

for s in steps:
    exact = exact * (1 + s)
    truncated = math.floor(truncated * (1 + s) * 1000) / 1000  # truncate to 3 dp

print(f"after {days} days x {updates_per_day} updates:")
print(f"  exact index     = {exact:10.3f}")
print(f"  truncated index = {truncated:10.3f}")
print(f"  drift           = {exact - truncated:10.3f}  (~{(exact - truncated) / days * 21:.1f} points/month; VSE reported ~25)")
print("no exception was raised; every intermediate value looked plausible")
# Check that catches it: recompute the derived series from raw inputs on a
# schedule and bound |derived - recomputed|.
