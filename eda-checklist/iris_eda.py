import pandas as pd
import plotly.express as px
import seaborn as sns

df=sns.load_dataset("iris")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
df.info()

print("\nshape of dataset:",df.shape)


print("\nMissing Values:")
print(df.isnull().sum())


fig1=px.histogram(df, x="petal_length", title="Distribution of petal Length")
fig1.show()

fig2=px.box(df, y="petal_length", title="outliers of petal Length")
fig2.show()

fig3=px.scatter(
    df,
    x="petal_length",
    y="petal_width",
    color="species",
    title="petal Length vs petal Width"
)
fig3.show()

print("\nAverage values by species:")
print(df.groupby("species").mean())