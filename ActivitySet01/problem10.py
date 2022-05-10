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
"""
there was an question on dictionaries but no place provided here so

fname = input("Enter file name: ")
fh = open(fname,"r")
c=fh.readlines()
dic={}
for i in c.copy():
    if(i[:5]=="From "):
        k=i.split()
        if(k[1] in dic):
            dic[k[1]]+=1
        else:
            dic[k[1]]=1
m=max(dic.values())
print(list(dic.keys())[list(dic.values()).index(m)],m)
fh.close()
"""

