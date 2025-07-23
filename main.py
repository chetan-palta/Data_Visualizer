import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Theme Selector 
print("\n🎨 Available Themes: darkgrid | whitegrid | ticks | poster")
theme = input("Choose a plot theme (default = whitegrid): ").strip().lower()
sns.set_style(theme if theme in ['darkgrid', 'whitegrid', 'ticks', 'poster'] else 'whitegrid')

# CSV Selection
csv_files = [f for f in os.listdir() if f.endswith('.csv')]
if not csv_files:
    print("❌ No CSV files found.")
    exit()

print("\n📂 Available CSV files:")
for i, file in enumerate(csv_files, 1):
    print(f"{i}. {file}")
choice = int(input("Choose a file: "))
file_path = csv_files[choice - 1]

df = pd.read_csv(file_path)
df.columns = df.columns.str.strip().str.title()

print("\n✅ Loaded:", file_path)
print("📋 Columns:", list(df.columns))
print("\n🔍 Data Preview:")
print(df.head())

# Drop nulls
if df.isnull().any().any():
    print("\n⚠️ Missing values detected. Cleaning...")
    df.dropna(inplace=True)

# Detect column types 
numeric_cols = df.select_dtypes(include='number').columns.tolist()
categorical_cols = df.select_dtypes(exclude='number').columns.tolist()
print("\n📊 Numeric Columns:", numeric_cols)
print("🔤 Categorical Columns:", categorical_cols)

# Optional Filters
region = input("\nFilter by Region (or Enter to skip): ")
if region and 'Region' in df.columns:
    df = df[df['Region'].str.lower() == region.strip().lower()]

month = input("Filter by Month (or Enter to skip): ")
if month and 'Month' in df.columns:
    df = df[df['Month'].str.lower() == month.strip().lower()]

if df.empty:
    print("❌ No data after filtering.")
    exit()

# Simple Insights
print("\n📈 Generating Data Insights...")
if 'Sales' in df.columns:
    top_month = df.groupby('Month')['Sales'].sum().idxmax() if 'Month' in df.columns else None
    top_region = df.groupby('Region')['Sales'].sum().idxmax() if 'Region' in df.columns else None
    print(f"💡 Peak Sales Month: {top_month}")
    print(f"💡 Region with Highest Sales: {top_region}")
if 'Expenses' in df.columns:
    top_expense = df.groupby('Region')['Expenses'].sum().idxmax() if 'Region' in df.columns else None
    print(f"💡 Region with Highest Expenses: {top_expense}")

# Create charts/ folder
os.makedirs("charts", exist_ok=True)

# Chart Plotting Function
def plot_chart(x, y, kind, ax=None):
    if kind == 'line':
        sns.lineplot(data=df, x=x, y=y, ax=ax)
    elif kind == 'bar':
        sns.barplot(data=df, x=x, y=y, ax=ax)
    elif kind == 'scatter':
        sns.scatterplot(data=df, x=x, y=y, ax=ax)
    elif kind == 'box':
        sns.boxplot(data=df, x=x, y=y, ax=ax)
    elif kind == 'hist':
        sns.histplot(data=df, x=y, bins=20, kde=True, ax=ax)
    else:
        print("❌ Unknown chart type.")

# Compare Charts
while True:
    compare = input("\n📊 Do you want to compare two charts side-by-side? (y/n): ").lower()
    if compare != 'y':
        break

    x1 = input("Chart 1 - X-axis: ")
    y1 = input("Chart 1 - Y-axis: ")
    type1 = input("Chart 1 - Type (line/bar/scatter/box/hist): ").lower()

    x2 = input("Chart 2 - X-axis: ")
    y2 = input("Chart 2 - Y-axis: ")
    type2 = input("Chart 2 - Type (line/bar/scatter/box/hist): ").lower()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    plot_chart(x1, y1, type1, ax=ax1)
    plot_chart(x2, y2, type2, ax=ax2)

    plt.tight_layout()
    filename = f"charts/compare_{x1}_{y1}_vs_{x2}_{y2}.png".replace(" ", "_")
    plt.savefig(filename)
    print(f"✅ Chart saved as {filename}")
    plt.show()

# Finish
print("✅ Done. All charts saved in /charts")
