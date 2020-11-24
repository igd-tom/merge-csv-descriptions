import pandas as pd
import sys

class InvalidFileType(Exception):
    pass

class InvalidFileFormat(Exception):
    pass


# if len(sys.argv) == 3:

    try:
        inFile = input("Enter input file path (.csv/xls): ") 
        # outFile = input("Enter output file path (.csv): ") 

        inFile = inFile.replace('"', "")

        outFile = inFile[:-4]
        outFile += ".out.xls"


        df = ''

        # read file, drop unnamed columns 
        if inFile.lower().endswith('.csv'):
            df = pd.read_csv(inFile).dropna(axis=1, how='all')

        elif inFile.lower().endswith('.xls'):
            df = pd.read_excel(inFile).dropna(axis=1, how='all')

        else:
            raise InvalidFileType

        
        if 'Description 1' in df.columns and 'Description 2' in df.columns and 'Description 3' in df.columns and 'Description 4' in df.columns and 'Tariff Code' in df.columns:
            # # combine descrip1 and decrip2 into col 'Product Name'
            # df['Product Name'] = df['Description 1'].str.cat(df['Description 2'],sep=", ")


            # combine descrip1 and decrip2 into col 'Product Name'
            df['Product Description'] = df['Description 1'].str.cat(df['Description 2'],sep=" ").str.cat(df['Description 3'],sep=" ").str.cat(df['Description 4'],sep=" ").str.cat(df['Tariff Code'],sep=" ")


            # combine descrip3 and decrip4 into col 'Product Description'
            # df['Product Description'] = df['Description 3'].str.cat(df['Description 4'],sep=", ")

            # remove columns tariff code, descrip 1,2,3,4
            df = df.drop(['Tariff Code', 'Description 1', 'Description 2', 'Description 3', 'Description 4'], axis=1)
            


            # df.to_csv(outFile, index=False)

            df.to_excel(outFile, index=False)  

            

        else:
            raise InvalidFileFormat
        
            
    
    except FileNotFoundError:
        print("Unable to find input file provided")

    except InvalidFileType:
        print("Invalid file type provided, please provide a .csv or .xls file")

    except InvalidFileFormat:
        print("Invalid file structure, Unable to find columns, Description 1/2/3/4")


    except UnicodeDecodeError:
        print("Invalid input file provided, please provide a csv file")


# else:
#     print("Please provide two arguments, the input file and the output file\n")
#     print("e.g. merge_descriptions.exe in.csv out.csv ")








