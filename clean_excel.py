import pandas as pd
import json
import numpy as np
import re

# Load Excel
df = pd.read_excel("sigma products assesment (1).xlsx", sheet_name="Sigmaaldrich_Cell Culture_And_A")

# Fix encoding
for col in ['Short Description', 'Product Name']:
    df[col] = df[col].astype(str).str.encode('utf-8', 'ignore').str.decode('utf-8')
    df[col] = df[col].str.replace('Î¼', 'um').str.replace('â‚¹', 'Rs.')

# Extract SKU, Pack Size, and Price
def extract_sku_info(entry):
    try:
        parsed = json.loads(entry.replace("'", '"'))
        if isinstance(parsed, dict):
            sku = list(parsed.keys())[0]
            pack_size = parsed[sku].get('Pack Size')
            price = parsed[sku].get('Price')
            return pd.Series([sku, pack_size, price])
    except Exception:
        return pd.Series([np.nan, np.nan, np.nan])

df[['SKU', 'Pack Size', 'Price']] = df['SKU__Pack_Size__Price'].apply(extract_sku_info)
df['Price'] = df['Price'].replace('[^0-9.]', '', regex=True).astype(float)

# Pack Qty & Price per Unit
df['Pack Qty'] = df['Pack Size'].str.extract(r'(\\d+)').astype(float)
df['Price per Unit'] = df.apply(
    lambda row: row['Price'] / row['Pack Qty'] if pd.notnull(row['Price']) and pd.notnull(row['Pack Qty']) else None,
    axis=1
)

# Extract measurements
def extract_measurements(text):
    if pd.isna(text):
        return None
    matches = re.findall(r'(\\d+(?:\\.\\d+)?\\s?(?:μm|um|mm|mM|mg|g|mL|%|µg/mL))', text)
    return ", ".join(matches) if matches else None

df['Extracted Measurements'] = df['Short Description'].apply(extract_measurements)

# Save CSV
df.to_csv("cleaned_sigma_dataset.csv", index=False)
print("✅ Cleaned dataset saved as 'cleaned_sigma_dataset.csv'")
