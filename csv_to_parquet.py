import pandas as pd

# path from files
path_to_csv = r'C:\Workspace\CURSO ADA TECH\MODULO II - tecnicas de programação\projeto_ccvil\cno.csv'
path_to_parquet = r'C:\Workspace\CURSO ADA TECH\MODULO II - tecnicas de programação\projeto_ccvil\cno.parquet'

# open CSV and save parquet
df_csv = pd.read_csv(path_to_csv, encoding='ISO-8859-1')

df_csv.to_parquet(path_to_parquet)

# Process completed successfully message
print(f'File successfully converted to {path_to_parquet}.')