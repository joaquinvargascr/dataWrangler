import pandas as pd
import numpy as np


def main():
    # Load the CSV files
    df1 = pd.read_csv("PYTEST_CSV_1.csv", delimiter='|')
    df2 = pd.read_csv("PYTEST_CSV_2.csv", delimiter='|')

    # Load the Excel file
    df3 = pd.read_excel("PYTEST_EXCEL.xlsx")

    # Combine the three dataframes
    df = pd.concat([df1, df2, df3])

    # Remove any special characters from the phone number field
    df['Phone Number'] = df['Phone Number'].str.replace('[^0-9]', '')

    # Remove any records with less than 10 digits in the phone number field
    df = df[df['Phone Number'].str.len() >= 10]

    # Convert the date of birth field to a datetime object and remove any records with an invalid format
    df['Date of Birth'] = pd.to_datetime(df['Date of Birth'], format='%m/%d/%Y', errors='coerce')
    df = df.dropna(subset=['Date of Birth'])

    # Remove any records with a zero balance amount
    df = df[df['Balance Amount'] != 0]

    # Calculate the remaining balance amount
    df['Remaining Balance Amount'] = df['Balance Amount'] - df['Paid Amount']

    # Remove any records with a zero remaining balance amount
    df = df[df['Remaining Balance Amount'] != 0]

    # Remove duplicates based on ID, Balance ID, Balance Amount, and Paid Amount
    df = df.drop_duplicates(subset=['ID', 'Balance ID', 'Balance Amount', 'Paid Amount'], keep='last')

    # Group by ID and aggregate the other fields
    agg_dict = {
        'ID': 'first',
        'First Name': 'first',
        'Last Name': 'first',
        'Phone Number': 'first',
        'Date of Birth': 'first',
        'Balance Amount': 'sum',
        'Paid Amount': 'sum',
        'Remaining Balance Amount': 'sum'
    }
    df_agg = df.groupby('ID').agg(agg_dict)

    # Reorder the columns in the aggregated dataframe
    df_agg = df_agg[['ID', 'First Name', 'Last Name', 'Phone Number',
                     'Date of Birth', 'Balance Amount', 'Paid Amount',
                     'Remaining Balance Amount']]

    # Write the output CSV file
    df_agg.to_csv('Output.csv', index=False)


if __name__ == '__main__':
    main()
