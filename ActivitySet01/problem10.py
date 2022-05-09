fname = input("Enter file name: ")
fh = open(fname,"r")
c=fh.readlines()
n=0
for i in c.copy():
    r=i
    if(i[:5]=="From "):
        k=r.split()
        print(k[1])
        n=n+1
print(f"There were {n} lines in the file with From as the first word")
fh.close()