import pandas as pd
import csv
import requests
# import mysql.connector
url = "link"

payload=""
 
response = requests.request("POST", url, headers=headers, data=payload)

daaata=response.json()

allinfo=[]
nextdata=daaata['articles']
alldetail=[]
# code to extract useful infomation from the api response

for i in range(len(nextdata)):  
    dtname=nextdata[i]
    details=dtname['details']
    arcticleno=dtname['articleNo']
    suplier=dtname['supplierName']
    print(suplier)
    for n in details:
        price=n['price']
        stock=n['stock']
        gtin=n['gtin']
        if(stock!="0.0"):
            articleStoreDetails=n['articleStoreDetails']
            for j in articleStoreDetails:
                if(j['storeNo']<25 and j['stock']!=0.0):
                    if(j['storeNo']==1):
                        store="TKFA"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==2):
                        store="LKSU"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==3):
                        store="SGMG"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==4):
                        store="COSU"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==5):
                        store="COLA"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==6):
                        store="COGU"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==7):
                        store="LPSA"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==8):
                        store="LKKW"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==9):
                        store="LKKO"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==10):
                        store="LKMH"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==11):
                        store="LPTR"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==12):
                        store="LPDO"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==13):
                        store="LPLE"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==14):
                        store="LPKW"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==15):
                        store="LPBO"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==17):
                        store="LPGU"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==18):
                        store="LPEL"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==19):
                        store="LPMH"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==20):
                        store="LPKK"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==21):
                        store="LASA"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==22):
                        store="LASU"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==23):
                        store="LAKK"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                    if(j['storeNo']==24):
                        store="SGSU"
                        alldetail.append(['',suplier,arcticleno,store,j['stock'],n['price'],n['gtin']])
                
            
            
                
# alldetail.append([suplierno,suplier,arcticleno,n['stock'],n['price'],n['gtin']])


        
        
# code to write the data to the csv file 
fields = ['item','Supplier', 'Article_No', 'Store','Stock', 'Price','Gtin'] 

filename = "allinforecords.csv"
# creating new csv which store allthe details
rows =alldetail
with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
# code to remove duplicate records according to articleno
df_state=pd.read_csv("allinforecords.csv",encoding='cp1252')
df_state.to_csv('allinforecords.csv', index = False)

#code to remove pattern & from column
datass = open("allinforecords.csv", "r")


datass = datass.read()

# search and replace the contents
datass = datass.replace("&", "")



# output.csv is the output file opened in write mode
x = open("allinforecords.csv", "w")

# all the replaced text is written in the output.csv file
x.write(datass)
x.close()





f = open('allinforecords.csv')
csv_f = csv.reader(f)   
data = []

for row in csv_f:
    data.append(row)
f.close()

df = pd.read_csv('allinforecords.csv')
header= list(df.columns)

def convert_row(row):
    
    str_row = """<%s>%s</%s> \n"""*(len(header)-1)
    str_row = """<%s>%s""" +"\n"+ str_row + """</%s>"""
    var_values = [list_of_elments[k] for k in range(1,len(header)) for list_of_elments in [header,row,header]]
    var_values = [header[0],row[0]]+var_values+[header[0]]
    var_values =tuple(var_values)
    return str_row % var_values

text ="""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>
<atom:link href="https://shop-lieblingsplatz.de/ProduktdatenfeedGoogleInventory.xml" rel="self" type="application/rss+xml" />
"""+"\n"+'\n'.join([convert_row(row) for row in data[1:]])+"\n" +"</channel></rss>"
print(text)
with open('ProduktdatenfeedGoogleInventory.xml', 'w') as myfile:
    myfile.write(text)