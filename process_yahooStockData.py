# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 00:41:46 2017
Reads a really messy .tsv file, with 3 lines of introductory
remarks.
The actual header on line 3 (zero-based indexing).
The script throws away the first 3 lines, by using header = T.
There are also comments interspersed within the data, but
fortunately they're on individual lines. The script also throws
away the comments and makes an index column and throws
out the column used to make the index column.
.csv and .xlsx files are then written to.

"""



import pandas as pd

fn = 'yahooStockMessy.tsv'

def inspectFile_AsIs():
    f = open(fn, 'r')
    ln = 1
    for line in f:
        print(ln, line[:-1])
        ln+=1
    f.close()

def processAndWriteOutputFiles():
    fn = 'yahooStockMessy.tsv'
    df = pd.read_csv(fn, header = 3, comment = '#', delimiter = ' ')
    df.index = df['name']
    df.index.name = 'Company_name'
    df = df.iloc[:,1:]
    print(df)
    print(type(df))
    print(df.shape)
    
    yahooStockClean = 'yahooStockClean.csv'
    
    df.to_csv(yahooStockClean, index = False)
    
    df.to_excel('yahooStockClean.xlsx', index = False)
    
if __name__ == "__main__":
    print("HERE'S THE ORIGINAL FILE:")
    inspectFile_AsIs()
    print("-"*20)
    print("NOW HERE'S THE DATAFRAME RESULTING FROM PROCESSING THE FILE AND SOME RELATED INFO ABOUT IT:")
    processAndWriteOutputFiles()
    