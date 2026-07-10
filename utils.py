import pandas as pd

def standardize_dataframe(df, project_name, district=None):

    # Add project name
    df["Project"] = project_name

    # Add district if missing
    if "pd.district" not in df.columns:
        df["pd.district"] = district

    return df
