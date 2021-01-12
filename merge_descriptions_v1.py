import pandas as pd
import sys
from typing import List


def trim_all_columns(df):
    """
    Trim whitespace from ends of each value across all series in dataframe
    """
    trim_strings = lambda x: x.strip() if isinstance(x, str) else x
    return df.applymap(trim_strings)



inFile = input("Enter input file path (.csv/xls): ") 
inFile = inFile.replace('"', "")
outFile = inFile[:-4]



df = ''

# read file, drop unnamed columns 
if inFile.lower().endswith('.csv'):
    df = pd.read_csv(inFile).dropna(axis=1, how='all')


elif inFile.lower().endswith('.xls'):
    df = pd.read_excel(inFile).dropna(axis=1, how='all')



matchesList = ['Description 1', 'Description 2', 'Description 3', 'Description 4', 'Tariff Code', 'Part Number'] 
dfColumnList = df.columns.tolist()


check =  all(item in dfColumnList for item in matchesList)

if check is True:
    # replace null characters with empty space
    df.fillna('', inplace=True)

    # rename columns Part Number and Description 1
    df.rename({"Part Number" : "SKU"}, axis=1, inplace=True)

    # merge columns Description 2,3,4 and Tariff Code into Description column
    df['Description'] = df[['Description 1','Description 2', 'Description 3', 'Description 4', 'Tariff Code']].agg(' '.join, axis=1)

    # df['Description'] = df['Description'].str.rstrip()
    # df['Description'] = df['Description'].str.strip()

    df = trim_all_columns(df)

   


    # removes columns Description 1,2,3,4 and Tariff Code
    df.drop(['Description 1', 'Description 2', 'Description 3', 'Description 4', 'Tariff Code'], axis=1, inplace=True)

    # create item name column, duplicate of SKU
    df['Item Name'] =  df['SKU']




    numRows = len(df)

    # appends addiitonal columns
    s = pd.Series(['1'])
    s = s.repeat(numRows)
    df['PriceList 1'] = s.values

    s = pd.Series(['2'])
    s = s.repeat(numRows)
    df['PriceList 2'] = s.values

    s = pd.Series(['3'])
    s = s.repeat(numRows)
    df['PriceList 3'] = s.values

    s = pd.Series(['4'])
    s = s.repeat(numRows)
    df['PriceList 4'] = s.values

    s = pd.Series(['per_item'])
    s = s.repeat(numRows)
    df['Type'] = s.values

    s = pd.Series(['GBP'])
    s = s.repeat(numRows)
    df['Currency Code'] = s.values

    s = pd.Series(['no_rounding'])
    s = s.repeat(numRows)
    df['Rounding Type'] = s.values

    df = df[['SKU', 'Product Group', 'Item Name', 'Description', 'Price 1', 'Price 2', 'Price 3', 'Price 4','PriceList 1', 'PriceList 2', 'PriceList 3', 'PriceList 4','Type', 'Currency Code', 'Rounding Type']]



    # df.to_csv(outFile + ".out.csv", index=False)

    df.to_excel(outFile + ".out.xls", index=False)  



else:
    print("Error not all columns found!")





#     df.fillna('', inplace=True)

#     df['SKU']


#     df['Product Description'] = df['Description 1'].astype(str) + " " + df['Description 2'].astype(str) + " " + df['Description 3'].astype(str) + " " +  df['Description 4'].astype(str) + " " +  df['Tariff Code'].astype(str)


#     # remove columns tariff code, descrip 1,2,3,4
#     df = df.drop(['Tariff Code', 'Description 1', 'Description 2', 'Description 3', 'Description 4'], axis=1)
    




#     df.to_excel(outFile, index=False)  

            

 


