import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("cleaned_sigma_dataset.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Detect likely category column
category_col = next((col for col in df.columns if 'category' in col.lower()), None)
if not category_col:
    raise ValueError("No column found with 'Category' in the name.")

# Detect likely price column
price_col = next((col for col in df.columns if 'price' in col.lower()), None)
if not price_col:
    raise ValueError("No column found with 'Price' in the name.")

# Detect likely name column
name_col = next((col for col in df.columns if 'name' in col.lower()), None)

# Convert price to numeric
df[price_col] = pd.to_numeric(df[price_col], errors='coerce')

# Drop rows with missing critical values
df = df.dropna(subset=[price_col, category_col])

# Display summary
print("Columns:", df.columns.tolist())
print("Dataset Shape:", df.shape)
print("Unique Categories:", df[category_col].nunique())
print(df[price_col].describe())

# Plot 1: Price Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df[price_col], bins=30, kde=True)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

# Plot 2: Top 5 Most Expensive Products
if name_col:
    top5 = df.nlargest(5, price_col)[[name_col, price_col]]
    plt.figure(figsize=(10, 5))
    sns.barplot(data=top5, x=price_col, y=name_col, palette="viridis")
    plt.title("Top 5 Most Expensive Products")
    plt.xlabel("Price")
    plt.ylabel("Product Name")
    plt.tight_layout()
    plt.savefig("top5_expensive_products.png")
    plt.show()

# Plot 3: Boxplot of Price by Category
# Only include categories with at least 5 entries
counts = df[category_col].value_counts()
valid_categories = counts[counts >= 5].index
filtered = df[df[category_col].isin(valid_categories)]

if not filtered.empty:
    plt.figure(figsize=(15, 6))
    sns.boxplot(data=filtered, x=category_col, y=price_col)
    plt.xticks(rotation=90)
    plt.title("Price Distribution by Category")
    plt.tight_layout()
    plt.savefig("boxplot_price_by_category.png")
    plt.show()
else:
    print("Not enough data to create boxplot.")
