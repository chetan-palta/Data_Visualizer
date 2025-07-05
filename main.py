import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import random

# Optional CSV generator
def generate_csv():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    regions = ['North', 'South', 'East', 'West']
    data = []

    for _ in range(100):
        month = random.choice(months)
        region = random.choice(regions)
        sales = random.randint(1000, 5000)
        expenses = random.randint(500, 4000)
        profit = sales - expenses
        data.append([month, region, sales, expenses, profit])

    df_gen = pd.DataFrame(data, columns=['Month', 'Region', 'Sales', 'Expenses', 'Profit'])
    df_gen.to_csv('sample2.csv', index=False)
    print("✅ sample2.csv generate  d with 100+ rows.")

# Ask user if they want to generate random data
if input("📁 Generate sample2.csv with 100+ rows? (y/n): ").lower() == 'y':
    generate_csv()

# Choose which CSV to load
file_path = input("📂 Enter CSV filename to load (default: sample.csv): ").strip()
if file_path == '':
    file_path = 'sample.csv'

if not os.path.exists(file_path):
    print(f"❌ File '{file_path}' not found.")
    exit()

# Load CSV
df = pd.read_csv(file_path)
print("\n✅ CSV Loaded Successfully!")
print("📋 Columns in CSV:", list(df.columns))
print("\n🔍 Data Preview:\n", df.head())

# Detect numeric columns
numeric_cols = df.select_dtypes(include='number').columns.tolist()

# Optional filter
def filter_data(df):
    print("\n🔎 Do you want to filter data?")
    apply_filter = input("Filter by Month or Region? (m/r/b for both / n for none): ").lower()

    filtered_df = df.copy()

    if apply_filter == 'm' or apply_filter == 'b':
        months = df['Month'].unique().tolist()
        print(f"📅 Available Months: {months}")
        month_input = input("Enter Month(s) to filter (comma-separated, leave blank to skip): ")
        if month_input.strip():
            selected_months = [m.strip() for m in month_input.split(',')]
            filtered_df = filtered_df[filtered_df['Month'].isin(selected_months)]

    if apply_filter == 'r' or apply_filter == 'b':
        if 'Region' in df.columns:
            regions = df['Region'].unique().tolist()
            print(f"🗺️ Available Regions: {regions}")
            region_input = input("Enter Region(s) to filter (comma-separated, leave blank to skip): ")
            if region_input.strip():
                selected_regions = [r.strip() for r in region_input.split(',')]
                filtered_df = filtered_df[filtered_df['Region'].isin(selected_regions)]

    if filtered_df.empty:
        print("⚠️ No data matched the filters. Showing full dataset.")
        return df

    print(f"✅ Filtered rows: {len(filtered_df)}")
    return filtered_df

# Chart function
def plot_chart(x_col, y_col, choice, data):
    plt.figure(figsize=(10, 6))

    if choice == '1':
        sns.lineplot(data=data, x=x_col, y=y_col)
        plt.title(f"Line Chart: {y_col} vs {x_col}")
    elif choice == '2':
        sns.barplot(data=data, x=x_col, y=y_col)
        plt.title(f"Bar Chart: {y_col} vs {x_col}")
    elif choice == '3':
        data.groupby(x_col)[y_col].sum().plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.ylabel('')
        plt.title(f"Pie Chart: Sum of {y_col} grouped by {x_col}")
    elif choice == '4':
        sns.scatterplot(data=data, x=x_col, y=y_col, hue='Region' if 'Region' in data.columns else None)
        plt.title(f"Scatter Plot: {y_col} vs {x_col}")
    elif choice == '5':
        sns.histplot(data=data, x=y_col, bins=20, kde=True)
        plt.title(f"Histogram of {y_col}")
    elif choice == '6':
        sns.boxplot(data=data, x=x_col, y=y_col)
        plt.title(f"Box Plot: {y_col} grouped by {x_col}")
    elif choice == '7':
        numeric_df = data.select_dtypes(include='number')
        sns.heatmap(numeric_df.corr(), annot=True, cmap="YlGnBu")
        plt.title("Heatmap: Correlation Matrix")
    else:
        print("❌ Invalid chart choice.")
        return False

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    save = input("💾 Save this chart as PNG? (y/n): ").lower()
    if save == 'y':
        filename = f"{x_col}_{y_col}_{choice}_filtered.png".replace(" ", "_")
        plt.savefig(filename)
        print(f"✅ Chart saved as {filename}")
    return True


# Main loop
while True:
    print("\n🎯 Available Columns:", list(df.columns))

    x_col = input("Enter column for X-axis: ").strip()
    y_col = input("Enter column for Y-axis (if needed): ").strip()

    if x_col not in df.columns or y_col not in df.columns:
        print("❌ Invalid column name(s). Try again.")
        continue

    print("\n📊 Choose Chart Type:")
    print("1. Line Chart\n2. Bar Chart\n3. Pie Chart\n4. Scatter Plot\n5. Histogram\n6. Box Plot\n7. Heatmap")
    choice = input("Enter choice (1-7): ").strip()

    filtered_df = filter_data(df)
    success = plot_chart(x_col, y_col, choice, filtered_df)
    if not success:
        continue

    again = input("\n🔁 Do you want to visualize another chart? (y/n): ").lower()
    if again != 'y':
        print("👋 Exiting... Thank you!")
        break
