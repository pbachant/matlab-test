import pandas as pd

df = pd.read_parquet("data/raw/data.parquet")

ax = df.voltage.plot()
ax.set_ylabel("Voltage (V)")
ax.set_xlabel("Time (s)")
ax.get_figure().savefig("figures/plot-py.png")