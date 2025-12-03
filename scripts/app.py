import pandas as pd

df = pd.read_csv("input.csv")

print("Sum:", df['value'].sum())
print("Average:", df['value'].mean())
print("Min:", df['value'].min())
print("Max:", df['value'].max())
