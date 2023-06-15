#I'm gonna use this file to write down some helpful routines
#That I'm gonna use always

#import section
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import trunc

#routines section

def missing_values_table(df):
    # Total missing values by column
    mis_val = df.isnull().sum()
        
    # Percentage of missing values by column
    mis_val_percent = 100 * df.isnull().sum() / len(df)
        
    # build a table with the thw columns
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        
    # Rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(
    columns = {0 : 'Missing Values', 1 : '% of Total Values'})
        
    # Sort the table by percentage of missing descending
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        
    # Print some summary information
    print ('Sumary :')
    print ('========================================')
    print (f"Columns     :{str(df.shape[1])}")
    print (f"Null values :{str(mis_val_table_ren_columns.shape[0])}")
    print ('=========================================')
        
           
    return mis_val_table_ren_columns


def exact_values_table(df,fvalue):
    # Total zero values by column
    fval = df[(df == fvalue)].count()
        
    # Percentage of missing values by column
    fval_percent = 100 * df[(df == fvalue)].count() / len(df)
        
    # build a table with the thw columns
    f_val_table = pd.concat([fval, fval_percent], axis=1)
        
    # Rename the columns
    zero_val_table_ren_columns = f_val_table.rename(
    columns = {0 : 'f Values', 1 : '% of Total Values'})
        
    # Sort the table by percentage of zero descending
    zero_val_table_ren_columns = zero_val_table_ren_columns[
        zero_val_table_ren_columns.iloc[:,1] != fvalue].sort_values(
        '% of Total Values', ascending=False).round(1)
        
    # Print some summary information
    print ('Sumary :')
    print ('========================================')
    print (f"Columns     :{str(df.shape[1])}")
    print (f"f values :{str(zero_val_table_ren_columns.shape[0])}")
    print ('=========================================')
        
    return zero_val_table_ren_columns

def features_by_type(df):
    # Count of column datatypes for the training dataset
    df_cols = pd.DataFrame(index = ['Features'], columns = ['Integer', 'Float', 'Object'])
    df_cols['Integer'] = len(df.columns[df.dtypes == 'int64'])
    df_cols['Float'] = len(df.columns[df.dtypes == 'float64'])
    df_cols['Object'] = len(df.columns[df.dtypes == 'object'])
    #print(f'shape param: {df.shape}')
    return df_cols

def plot_features_distribution(df):
    plt.figure(figsize=(15,70))
    plotnumber = 1

    num_rows=trunc(len(df.columns)/3)
    if (len(df.columns) % 3) != 0:
        num_rows += 1

    for col in df:
        if plotnumber <= df.shape[1]:
            ax1 = plt.subplot(num_rows,3,plotnumber)
            if df[col].dtypes == 'O':
                sns.countplot(data=df, y=col, palette='Dark2')
            else:
                sns.histplot(data= df, x=col ,palette='Light2')

            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12)
            plt.title(col.title(), fontsize=14)
            plt.xlabel('')
            plt.ylabel('')
        plotnumber +=1
        plt.tight_layout()
    
    plt.show()
    
    return
