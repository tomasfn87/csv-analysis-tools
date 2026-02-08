import pandas as pd

def assemble_dataframe(source_df, column_ops):
    operations_row = {}
    results_row = {}
    
    for col, op in column_ops.items():
        operations_row[col] = op
        results_row[col] = getattr(source_df[col], op)()

    df = pd.DataFrame(
        [operations_row, results_row],
        index=["Operation", "Results"]
    )
    
    for col, op in column_ops.items():
        value = df.loc["Results", col]
        if pd.api.types.is_integer_dtype(source_df[col]):
            df.loc["Results", col] = f"{int(value):,}"
        elif pd.api.types.is_float_dtype(source_df[col]):
            df.loc["Results", col] = f"{value:,.2f}"
    
    return df