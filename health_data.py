''' this module will be used to extract data from given csv dataset and will
generate each record and each column of data'''

import csv

records=[]
columns=[]

def fieldHeadings():
    fieldDict={'Salary':0,'Time of Infection':1,'Time of reporting':2,'x location':3,'y location':4,'Age':5,'Diabetes':6,'Respiratory Illnesses':7,'Abnormal Blood Pressure':8,'Outcome':9}
    return fieldDict
    
def getRecord():
    global records
    with open('C:\\Users\\Humans\\Documents\\My Docs-Disha\\py\\mathrix2020\\COVID_Dataset.csv','r+') as csvfile:
    #with open("C:\\Users\\Humans\\Documents\\My Docs-Disha\\py\\mathrix2020\\emp.csv","r+") as csvfile:
        reader=csv.reader(csvfile)
        for i in reader :
            if i!=[]:
                records.append(i)
    return records
        
        

def getColumn(colnum):
    global columns
    global records
    getRecord()
    
    for i in records:
        columns.append(i[colnum])
    return columns[1::]
        

 
