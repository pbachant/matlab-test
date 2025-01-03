disp("Plotting");
data = parquetread("../data/raw/data.parquet");
plot(data, "voltage");
xlabel("Time (s)");
mkdir("../figures");
saveas(gcf, "../figures/plot.png")