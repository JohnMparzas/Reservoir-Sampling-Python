import random
import sys


#k=int(sys.argv[1]);
listofk=[];

k=int(input("dwse to k "));
f=open('input.txt','r');
#for l in open('input.txt'):
   # print(l,end='')
line=f.readline();

i=1;

while line:
    if (len(line.strip()) == 0 ):
        line=f.readline();
    if(i<=k):
        listofk.append(line);
    elif(i>k):
        j=random.randint(1, i);
        if(j<=k):
            listofk[j-1]=line;
   # print(line);
    line=f.readline();
    i=i+1;
  
#f=read();
print ("+++++++++++++Results+++++++++++");
print("the size is: ",len(listofk));
for i in range(k):
    print(listofk[i]);
    print("");
