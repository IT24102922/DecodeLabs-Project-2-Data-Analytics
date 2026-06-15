import pandas as pd
import numpy as np
import os

# ==========================================
# 1. AUTOMATED INPUT: Auto-detect File & Path
# ==========================================
# Get the folder where clean_data.py is located
current_folder = os.path.dirname(os.path.abspath(__file__))

# Automatically scan the folder for any file containing "Dataset for Data Analytics"
detected_file = None
for file in os.listdir(current_folder):
    if "Dataset for Data Analytics" in file:
        detected_file = file
        break

print("--- SYSTEM CHECK ---")
if detected_file is None:
    print(f"[ERROR] Could not find any file containing 'Dataset for Data Analytics' in this folder.")
    print(f"Current Folder path: {current_folder}")
    print("Please make sure your dataset file is in the EXACT same folder as this script!")
else:
    full_path = os.path.join(current_folder, detected_file)
    print(f"🎉 Success! Detected File: '{detected_file}'")
    print("Loading data... Please wait.")
    
    # Automatically detect extension and load correctly (CSV or Excel)
    if detected_file.lower().endswith('.csv'):
        df = pd.read_csv(full_path)
    elif detected_file.lower().endswith(('.xlsx', '.xls')):
        # Note: If it's excel, openpyxl library might be needed
        try:
            df = pd.read_excel(full_path)
        except Exception:
            print("To read Excel files, installing openpyxl...")
            os.system('pip install openpyxl')
            df = pd.read_excel(full_path)

    # Clean column names by removing any leading/trailing spaces
    df.columns = df.columns.str.strip()

    # ==========================================
    # 2. DATA CLEANING & PREPARATION
    # ==========================================
    print("\n--- STARTING DATA CLEANING ---")
    
    # Check for missing values
    missing_values = df.isnull().sum()
    print("Missing values per column:")
    print(missing_values[missing_values > 0] if missing_values.sum() > 0 else "No missing values found!")

    # Check for duplicate rows
    duplicates = df.duplicated().sum()
    print(f"Total duplicate rows found: {duplicates}")
    if duplicates > 0:
        df = df.drop_duplicates()
        print("Duplicates removed successfully.")

    # Convert Date column to standard datetime format
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        print("Date column converted to Datetime format.")

    # ==========================================
    # 3. STATISTICAL SUMMARY (Project 2 Requirements)
    # ==========================================
    print("\n--- DESCRIPTIVE STATISTICS ---")
    numeric_cols = [col for col in ['Quantity', 'UnitPrice', 'TotalPrice', 'ItemsInCart'] if col in df.columns]
    basic_stats = df[numeric_cols].describe()
    print(basic_stats)

    if 'TotalPrice' in df.columns:
        print(f"\nTotalPrice Mean (Average): ${df['TotalPrice'].mean():.2f}")
        print(f"TotalPrice Median (Middle): ${df['TotalPrice'].median():.2f}")

        # ==========================================
        # 4. OUTLIER CLEANING (IQR Method)
        # ==========================================
        print("\n--- HANDLING OUTLIERS ---")
        Q1 = df['TotalPrice'].quantile(0.25)
        Q3 = df['TotalPrice'].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[(df['TotalPrice'] < lower_bound) | (df['TotalPrice'] > upper_bound)]
        clean_df = df[(df['TotalPrice'] >= lower_bound) & (df['TotalPrice'] <= upper_bound)]

        print(f"Total Outliers detected: {len(outliers)}")
        print(f"Cleaned dataset rows: {len(clean_df)} (out of {len(df)})")

        # Save the cleaned dataset
        output_file = os.path.join(current_folder, "Cleaned_Data_Analytics.csv")
        clean_df.to_csv(output_file, index=False)
        print(f"\n🎉 Success! Cleaned dataset saved as: 'Cleaned_Data_Analytics.csv'")