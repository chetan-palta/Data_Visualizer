import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import random

# Load CSV
file_path = "sample2.csv"
if not os.path.exists(file_path):
    print(f"❌ File '{file_path}' not found.")
    exit()

df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip().str.title()

# Display info
print("\n✅ CSV Loaded Successfully!")
print("📋 Columns in CSV:", list(df.columns))
print("\n🔍 Data Preview:")
print(df.head())

# Show data summary
print("\n📊 Data Summary:")
print(df.describe(include='all'))

# Filter by Region/Month
filter_region = input("\n🔍 Enter Region to filter (or press Enter to skip): ")
if filter_region:
    df = df[df['Region'].str.lower() == filter_region.strip().lower()]

filter_month = input("🔍 Enter Month to filter (or press Enter to skip): ")
if filter_month:
    df = df[df['Month'].str.lower() == filter_month.strip().lower()]

if df.empty:
    print("❌ No data found after applying filters.")
    exit()

# Chart plotting function
def plot_chart(x_col, y_col, choice):
    plt.figure(figsize=(10, 6))




    if choice == '1':  # Line Chart
        sns.lineplot(data=df, x=x_col, y=y_col)
        plt.title(f"Line Chart: {y_col} vs {x_col}")

    elif choice == '2':  # Bar Chart
        sns.barplot(data=df, x=x_col, y=y_col)
        plt.title(f"Bar Chart: {y_col} vs {x_col}")

    elif choice == '3':  # Pie Chart
        df.groupby(x_col)[y_col].sum().plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.ylabel('')
        plt.title(f"Pie Chart: Sum of {y_col} by {x_col}")

    elif choice == '4':  # Scatter Plot
        sns.scatterplot(data=df, x=x_col, y=y_col, hue='Region' if 'Region' in df.columns else None)
        plt.title(f"Scatter Plot: {y_col} vs {x_col}")

    elif choice == '5':  # Histogram
        sns.histplot(data=df, x=y_col, bins=20, kde=True)
        plt.title(f"Histogram of {y_col}")

    elif choice == '6':  # Box Plot
        sns.boxplot(data=df, x=x_col, y=y_col)
        plt.title(f"Box Plot: {y_col} grouped by {x_col}")

    elif choice == '7':  # Heatmap
        numeric_df = df.select_dtypes(include='number')
        sns.heatmap(numeric_df.corr(), annot=True, cmap="YlGnBu")
        plt.title("Heatmap: Correlation Matrix")

    elif choice == '8':  # Trend Line (Regression)
        sns.regplot(data=df, x=x_col, y=y_col, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
        plt.title(f"Trend Line: {y_col} vs {x_col}")

    elif choice == '9':  # Multi-Line Plot
        if {'Sales', 'Expenses'}.issubset(df.columns):
            if x_col not in df.columns or df[x_col].ndim != 1 or df[x_col].dtype in ['int64', 'float64']:
                print("❌ For multi-line plot, X-axis must be a categorical column like 'Month' or 'Region'.")
            return False

        pivot_df = df.pivot_table(index=x_col, values=['Sales', 'Expenses'], aggfunc='sum')

        # Make sure it's a new figure
        fig, ax = plt.subplots(figsize=(10, 6))
        pivot_df.plot(marker='o', ax=ax)

        plt.title(f"Sales vs Expenses by {x_col}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        save = input("💾 Save this chart as PNG? (y/n): ").lower()
        if save == 'y':
            filename = f"{x_col}_multi_line.png".replace(" ", "_")
            fig.savefig(filename)
            print(f"✅ Chart saved as {filename}")
        return True
    else:
        print("❌ 'Sales' or 'Expenses' column missing.")
        return False



    save = input("💾 Save this chart as PNG? (y/n): ").lower()
    if save == 'y':
        filename = f"{x_col}_{y_col}_{choice}.png".replace(" ", "_")
        plt.savefig(filename)
        print(f"✅ Chart saved as {filename}")
    return True


# Main loop
while True:
    print("\n🎯 Available Columns:", list(df.columns))
    x_col = input("Enter column for X-axis: ")
    y_col = input("Enter column for Y-axis (if needed): ")

    if x_col not in df.columns or y_col not in df.columns:
        print("❌ Invalid column name(s). Try again.")
        continue

    print("\n📊 Choose Chart Type:")
    print("1. Line Chart\n2. Bar Chart\n3. Pie Chart\n4. Scatter Plot\n5. Histogram")
    print("6. Box Plot\n7. Heatmap\n8. Trend Line\n9. Multi-Line Plot (Sales vs Expenses)")

    choice = input("Enter choice (1-9): ")

    success = plot_chart(x_col, y_col, choice)
    if not success:
        continue

    again = input("\n🔁 Do you want to visualize another chart? (y/n): ")
    if again.lower() != 'y':
        print("👋 Exiting... Thank you!")
        break
