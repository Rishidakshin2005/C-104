import csv
with open('Data.csv',newline ='')as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

newdata=[]
for i in range(len(file_data)):
    num=file_data[i][1]
    newdata.append(float(num))

n=len(newdata)
newdata.sort()

#logic to find median
if n % 2==0:
    median1=float(newdata[n//2])
    median2=float(newdata[n//2-1])
    median=(median1+median2)/2
else:
    median=newdata[n//2]

print("Median="+str(median))    