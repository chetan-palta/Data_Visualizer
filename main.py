import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ========== Feature 1: Dynamic CSV selection ==========
csv_files = [f for f in os.listdir() if f.endswith('.csv')]
if not csv_files:
    print("❌ No CSV files found in the current directory.")
    exit()

print("📂 Available CSV files:")
for idx, file in enumerate(csv_files, 1):
    print(f"{idx}. {file}")

choice = int(input("🔽 Enter the number of the CSV file to load: "))
file_path = csv_files[choice - 1]

# ========== Load CSV ==========
df = pd.read_csv(file_path)
df.columns = df.columns.str.strip().str.title()
print(f"\n✅ Loaded: {file_path}")
print("📋 Columns:", list(df.columns))

# ========== Feature 2: Handle missing values ==========
missing_cols = df.columns[df.isnull().any()].tolist()
if missing_cols:
    print(f"\n⚠️ Columns with missing values: {missing_cols}")
    df.dropna(inplace=True)
    print("🧹 Rows with missing values removed.")

# ========== Preview ==========
print("\n🔍 Data Preview:")
print(df.head())

# ========== Filter Feature ==========
filter_region = input("\n🔍 Filter by Region (or press Enter to skip): ")
if filter_region:
    df = df[df['Region'].str.lower() == filter_region.strip().lower()]

filter_month = input("🔍 Filter by Month (or press Enter to skip): ")
if filter_month:
    df = df[df['Month'].str.lower() == filter_month.strip().lower()]

if df.empty:
    print("❌ No data found after filtering.")
    exit()

# ========== Create charts/ directory ==========
os.makedirs("charts", exist_ok=True)

# ========== Chart Function ==========
def plot_chart(x_col, y_col, chart_type):
    plt.figure(figsize=(10, 6))
    plt.xticks(rotation=45)

    if chart_type == '1':
        sns.lineplot(data=df, x=x_col, y=y_col)
    elif chart_type == '2':
        sns.barplot(data=df, x=x_col, y=y_col)
    elif chart_type == '3':
        df.groupby(x_col)[y_col].sum().plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.ylabel('')
    elif chart_type == '4':
        sns.scatterplot(data=df, x=x_col, y=y_col, hue='Region' if 'Region' in df.columns else None)
    elif chart_type == '5':
        sns.histplot(data=df, x=y_col, bins=20, kde=True)
    elif chart_type == '6':
        sns.boxplot(data=df, x=x_col, y=y_col)
    elif chart_type == '7':
        sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap="YlOrRd")
        plt.title("Correlation Heatmap")
    
    elif chart_type == '8':
        if x_col == 'Month' and df[x_col].dtype == 'object':
            month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December']
            month_map = {month: i+1 for i, month in enumerate(month_order)}
            df[x_col] = df[x_col].map(month_map)


        if not pd.api.types.is_numeric_dtype(df[x_col]):
            print("❌ Trend lines can only be plotted for numeric X-axis values.")
            return False
        sns.regplot(data=df, x=x_col, y=y_col, scatter_kws={"color": "blue"}, line_kws={"color": "red"})


    elif chart_type == '9':
        if {'Sales', 'Expenses'}.issubset(df.columns):
            pivot_df = df.pivot_table(index=x_col, values=['Sales', 'Expenses'], aggfunc='sum')
            pivot_df.plot(marker='o')
            plt.title(f"Sales vs Expenses by {x_col}")
            plt.xticks(rotation=45)
        else:
            print("❌ Columns 'Sales' or 'Expenses' not found.")
            return False
    else:
        print("❌ Invalid chart type.")
        return False

    plt.title(f"{y_col} vs {x_col}")
    filename = f"charts/{x_col}_{y_col}_{chart_type}.png".replace(" ", "_")
    plt.tight_layout()
    plt.savefig(filename)
    print(f"✅ Chart saved as {filename}")
    plt.show()
    return True

# ========== Loop ==========
while True:
    print("\n📊 Chart Types:")
    print("1. Line\n2. Bar\n3. Pie\n4. Scatter\n5. Histogram")
    print("6. Box\n7. Heatmap\n8. Trendline\n9. Multi-line (Sales vs Expenses)")

    x_col = input("\n📌 X-axis column: ")
    y_col = input("📌 Y-axis column: ")

    if x_col not in df.columns or y_col not in df.columns:
        print("❌ Invalid columns.")
        continue

    chart_type = input("🎨 Choose chart type (1-9): ")
    plot_chart(x_col, y_col, chart_type)

    cont = input("🔁 Visualize another? (y/n): ").lower()
    if cont != 'y':
        print("👋 Done! All charts saved in /charts")
        break
