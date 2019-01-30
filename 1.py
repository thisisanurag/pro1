import csv
k=5
a=[]
with open('data1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    sm=9999
    for row in readCSV:
        n=int(row[0])
        if (n-k>=0 and n-k<sm and k!=n):
            x=n
            sm=n-k
            p=row[1]
        if (n-k<0 and k-n<sm and k!=n):
            x=n
            sm=k-n
            p=row[1]
    a.append(p)
with open('data1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    sm=9999
    for r in readCSV:
        n = int(r[0])
        if (n - k >= 0 and n - k < sm and x!=n and k!=n):
            sm = n - k
            p = r[1]
        if (n - k < 0 and k - n < sm and x!=n and k!=n):
            sm = k - n
            p = r[1]
a.append(p)
print(a)
e=0
i=0
for u in a:
    if (u=="'E'"):
        e=e+1
    else:
        i=i+1
e=e/2*100
i=i/2*100
print('Extrovert=',e,'%',' ','Introvert=',i,'%')