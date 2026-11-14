"""NOTE: reproduces the mechanism with synthetic data, not the original data or exact figures.
SF-016: cumulative and daily semantics mixed in one table (covid19-sir #1373).

Two columns look alike; one is a running total, the other is a daily count.
Downstream code that diffs the cumulative column to get daily values produces
garbage for the daily one, and sums of the cumulative one are meaningless.
Nothing raises. Detected in the wild by plotting.
Run: python repro_004_cumulative_mixed.py
"""
import numpy as np
import pandas as pd

days = pd.date_range("2022-10-01", periods=10, freq="D")
daily_1st = np.array([9_744_650, 857, 582, 1_200, 950, 9_745_232, 300, 400, 100, 50])  # mixed: some rows cumulative, some daily
cum_3rd = np.cumsum([1000] * 10)
df = pd.DataFrame({"date": days, "Vaccinated_1st": daily_1st, "Vaccinated_3rd": cum_3rd})

# A consumer assumes both are cumulative and diffs them to get daily counts.
daily = df.set_index("date")[["Vaccinated_1st", "Vaccinated_3rd"]].diff()
print(daily.head(6))
print("negative 'daily' values from the mixed column:", int((daily["Vaccinated_1st"] < 0).sum()))
print("no exception was raised")

# The check: a column declared cumulative must be monotonic non-decreasing.
for col in ["Vaccinated_1st", "Vaccinated_3rd"]:
    print(f"{col} monotonic non-decreasing: {df[col].is_monotonic_increasing}")
