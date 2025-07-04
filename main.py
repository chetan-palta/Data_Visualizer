import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load CSV
file_path = "sample.csv"    
if not os.path.exists(file_path):
    print(f"File '{file_path}' not found.")
    exit()

df = pd.read_csv(file_path)

# Display info
print("\n✅ CSV Loaded Successfully!")
print("📋 Columns in CSV:")
print(list(df.columns))

print("\n🔍 Data Preview:")
print(df.head())

# Detect numeric columns for y-axis suggestions
numeric_cols = df.select_dtypes(include='number').columns.tolist()

def plot_chart(x_col, y_col, choice):
    plt.figure(figsize=(10, 6))
    if choice == '1':
        sns.lineplot(data=df, x=x_col, y=y_col)
        plt.title(f"Line Chart: {y_col} vs {x_col}")
    elif choice == '2':
        sns.barplot(data=df, x=x_col, y=y_col)
        plt.title(f"Bar Chart: {y_col} vs {x_col}")
    elif choice == '3':
        df.groupby(x_col)[y_col].sum().plot(
            kind='pie', autopct='%1.1f%%', startangle=90)
        plt.ylabel('')
        plt.title(f"Pie Chart: Sum of {y_col} grouped by {x_col}")
    else:
        print("❌ Invalid chart choice.")
        return False

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Save chart option
    save = input("💾 Save this chart as PNG? (y/n): ").lower()
    if save == 'y':
        filename = f"{x_col}_{y_col}_{choice}.png".replace(" ", "_")
        plt.savefig(filename)
        print(f"✅ Chart saved as {filename}")
    return True


# Main loop
while True:
    print("\n🎯 Available Columns:")
    print(list(df.columns))
    
    x_col = input("Enter column for X-axis: ")
    y_col = input("Enter column for Y-axis (if needed): ")

    if x_col not in df.columns or y_col not in df.columns:
        print("❌ Invalid column name(s). Try again.")
        continue

    print("\n📊 Choose Chart Type:")
    print("1. Line Chart\n2. Bar Chart\n3. Pie Chart")
    choice = input("Enter choice (1/2/3): ")

    success = plot_chart(x_col, y_col, choice)
    if not success:
        continue

    again = input("\n🔁 Do you want to visualize another chart? (y/n): ")
    if again.lower() != 'y':
        print("👋 Exiting... Thank you!")
        break
