import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
file_path = "sample.csv"
df = pd.read_csv(file_path)

# Preview
print("Columns in CSV:")
print(df.columns)
print("\nData Preview:")
print(df.head())

# Let user choose columns
x_col = input("Enter column for X-axis: ")
y_col = input("Enter column for Y-axis (if needed): ")

if x_col not in df.columns or y_col not in df.columns:
    print("Invalid column name(s). Exiting.")
    exit()

print("\nChoose Chart Type:")
print("1. Line Chart\n2. Bar Chart\n3. Pie Chart")
choice = input("Enter choice (1/2/3): ")
if choice == '1':
    sns.lineplot(data=df, x=x_col, y=y_col)
    plt.title("Line Chart")
elif choice == '2':
    sns.barplot(data=df, x=x_col, y=y_col)
    plt.title("Bar Chart")
elif choice == '3':
    df.groupby(x_col)[y_col].sum().plot(kind='pie', autopct='%1.1f%%')
    plt.ylabel('')  # Hides y-axis label
    plt.title("Pie Chart")
else:
    print("Invalid choice.")
    exit()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



while True:
    # (repeat input + plot code)
    again = input("\nDo you want to visualize another chart? (y/n): ")
    if again.lower() != 'y':
        break