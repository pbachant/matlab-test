"""Plot the data with Python."""

import matplotlib.pyplot as plt
import pandas as pd

pd.read_parquet("data/raw/data.parquet").plot()
plt.savefig("figures/plot-py.png")
