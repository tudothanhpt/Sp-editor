import pandas as pd
import numpy as np
from sp_editor.crud.cr_pier_force import read_pierdesign_forceDB
from sp_editor.crud.cr_level_group import read_groupDB
from sqlmodel import create_engine
from sqlalchemy.engine import Engine

#ENSURE THE 2 GIVEN DATAFRAMES' HEADERS TO BE ADDRESSED CORRECTLY FOLLOWING THE BELOW CONVENTION
HEADER_STORY = "Story"
HEADER_PIER = "Pier"
HEADER_TIER = "Tier"
HEADER_LOADCASE = "Combo"
HEADER_LOCATION = "Location"
HEADER_P = "P"
HEADER_M2 = "M2"
HEADER_M3 = "M3"

def create_force_filter_df(df_PierForces: pd.DataFrame, df_Tier: pd.DataFrame) -> pd.DataFrame:
    """
    Merge two DataFrames on the 'Story' column, create new columns based on certain operations,
    and return the resulting DataFrame.

    Parameters:
    df1 (pd.DataFrame): Pier Forces DataFrame
    df2 (pd.DataFrame): Group Definition DataFrame

    Returns:
    df3 (pd.DataFrame: The merged DataFrame with new columns.
    """
    df_FilteredForces = df_PierForces.merge(df_Tier, on=HEADER_STORY, how='left')
    
    df_FilteredForces['ID3'] = (
        df_FilteredForces[HEADER_STORY] + 
        df_FilteredForces[HEADER_PIER] + 
        df_FilteredForces[HEADER_LOADCASE] + 
        df_FilteredForces[HEADER_LOCATION]
    )
    print(df_FilteredForces['P'])
    
    df_FilteredForces['P_SPCol'] = np.round(df_FilteredForces['P'], 0).astype(float)*(-1)
    df_FilteredForces['Mx_SPCol'] = np.round(df_FilteredForces[HEADER_M2], 0).astype(float)
    df_FilteredForces['My_SPCol'] = np.round(df_FilteredForces[HEADER_M3], 0).astype(float)
    
    return df_FilteredForces

def force_filter_SPformat(df3: pd.DataFrame, pier_value: str, tier: str) -> tuple:
    """
    Merge two DataFrames on the 'Story' column, create new columns based on certain operations,
    filter rows based on specific conditions, and generate a formatted result string.

    Parameters:
    df3 (pd.DataFrame: The merged DataFrame with new columns.
    pier_value (str): The value to filter the 'Pier' column
    tier (str): The value to filter the 'Force Grouping' column

    Returns:
    tuple: A tuple containing the result string and the filtered DataFrame.
    """
    
    # Filter rows based on specific conditions
    filter_cond = (df3[HEADER_PIER] == pier_value) & (df3[HEADER_TIER] == tier)
    filter_df = df3.loc[filter_cond, ['P_SPCol', 'Mx_SPCol', 'My_SPCol']]
    
    # Create the 'Combined_Col' column by concatenating 'P_SPCol', 'Mx_SPCol', 'My_SPCol'
    filter_df['Combined_Col'] = filter_df.apply(
        lambda row: f"{row['P_SPCol']},{row['Mx_SPCol']},{row['My_SPCol']}", axis=1
    )
    
    # Get the total number of filtered rows
    total_rows = filter_df.shape[0]
    
    # Convert the 'Combined_Col' column values to a list
    combined_values = filter_df['Combined_Col'].to_list()
    
    # Join the list into a single string with each value on a new line
    load_string = '\n'.join(combined_values)
    
    # Create the result string
    result_string = f"{total_rows}\n{load_string}"
    
    return result_string, total_rows

def main():
    #PSEUDO DATA
    engine_temppath = r"C:\Users\abui\Desktop\Git\Repo\SP-editor\tests\TestBM\1.spe"
    engine: Engine = create_engine(f"sqlite:///{engine_temppath}")
    
    #MAIN
    df_PierForces = read_pierdesign_forceDB(engine)
    df_Tier = read_groupDB(engine)

    
    pier_value = "P1" #TO BE REPLACED WITH SELECTION FROM UI
    tier = "Tier1" #TO BE REPLACED WITH SELECTION FROM UI
    df_FilteredForces = create_force_filter_df(df_PierForces, df_Tier)

    #print(df_FilteredForces)
    result_string, total_rows = force_filter_SPformat(df_FilteredForces, pier_value, tier)
    print(result_string)

if __name__ == "__main__":
    main()
