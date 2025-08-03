Biomall Data Analyst Assignment – Summary Report

Data Cleaning and Preprocessing

The original dataset had several issues including encoding errors (like symbols “â‚¹” instead of ₹), nested data fields, and missing or inconsistent values.

Steps taken:

Fixed encoding issues and replaced incorrect characters with appropriate symbols.

Extracted structured information from complex fields like SKU/Pack/Price and Properties.

Converted price fields into numeric format.

Normalized units such as "μm" into a consistent format.

Dropped rows that were missing critical information or couldn't be cleaned.

Exploratory Data Analysis (EDA)

Summary of insights:

Identified the number of unique product categories and SKUs.

Analyzed price distributions across different categories.

Detected outliers and unusually high-priced products.

Found that most products are priced within ₹0 to ₹10,000, with a few outliers above ₹50,000.

Visualizations

Generated charts to support the analysis:

Histogram showing overall price distribution.

Box plot displaying price ranges for each category.

Bar chart showing the top 5 most expensive products.

Bonus: Data Enrichment

Additional analysis included:

Extracted measurement details like volumes, concentrations, or dimensions from product descriptions.

Calculated price per unit when pack size information was available.

Tools Used

The analysis was done using:

Python libraries: pandas, numpy, matplotlib, seaborn, re (for regular expressions), and ast.

Challenges and Assumptions

The column names required clarification and slight renaming.

Rows with incomplete or ambiguous data were removed for accurate analysis.

No assumptions were made about missing prices or quantities.

Deliverables

Cleaned dataset: cleaned_sigma_dataset.csv

Jupyter notebook with code and visualizations: eda_visualization.ipynb

Summary report (this document)

requirements.txt listing Python packages used

README.md describing the project
