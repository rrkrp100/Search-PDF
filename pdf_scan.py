#! Python3

import PyPDF2
import csv
import pandas as pd
#import operator
keywords=input('Enter the keywords').split()        #Input
counter=dict()

pdffile=open('JavaBasics-notes.pdf','rb')           #Opening the pdf
pdfReader=PyPDF2.PdfFileReader(pdffile)
pg=pdfReader.numPages

for i in range(pg):                                 #Searching for the keywords
    pageobj=pdfReader.getPage(i)
    page=pageobj.extractText().split(' ')
    for wrd in page:
        if wrd in keywords:
            if wrd in counter.keys():
                counter[wrd]+=1
            else:
                counter[wrd]=1
                
                
for i in keywords:                                  #cleaning up
    if i not in counter.keys():
        counter[i]=0
        


from collections import OrderedDict 

sorted_counter= dict(OrderedDict(sorted(counter.items(), key=lambda t:t[1])))
res = list()                                                        
                                                    #Ordering the output
for key,value in sorted_counter.items():
        print(key, value)
        res.append((key,value))
    
with open('the_csv.csv',"w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(res)
    
data=pd.read_csv('the_csv.csv')
