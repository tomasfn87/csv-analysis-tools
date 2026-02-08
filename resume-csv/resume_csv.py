import pandas as pd
from sys import argv as argv

from assemble_df import assemble_dataframe as assemble_df

if len(argv) < 2:
    print("Usage: python csv_analysis.py <csv_file_path>")
    exit(1)

csv_file_path = argv[1]

df = pd.read_csv(
    csv_file_path,
    low_memory=False)

print("1) Fields names and data types:\n")

print(df.dtypes.to_frame(name="dtype"))

if len(argv) > 2 and argv[2] == '--list-csv-fields-only':
    exit(0)

""" Reduce operation functions to be applied to the fields:

min() → minimun value
max() → maxium value
mean() → mean
median() → median
std() → standard deviation
var() → variance
count() → quantity of non-null values
nunique() → number of unique values
"""

print("\n\n2) Result / Operation performed:\n")

result_dfs = [
    assemble_df(df, {
        "Início dos relatórios": "min",
        "Término dos relatórios": "max",
        "Nome da campanha": "nunique",
        "Frequência": "mean",
        "Alcance": "sum"
    }),
    assemble_df(df, {
        "Valor usado (BRL)": "sum",
        "Impressões": "sum",
        "Cliques no link": "sum",
        "Visualizações da página de destino": "sum"
    })    
]

for i in range(0, len(result_dfs)):
    print(result_dfs[i])
    if i != len(result_dfs) - 1:
        print()
