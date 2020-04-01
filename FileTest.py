import os, shutil
DataPath = ("C:\project\\")
f = open(DataPath + "1", 'r')
Input = list(f.read())
f.close()
Output = []
now = ""
for i in Input:
    if i == "," or i == "\n":
        Output.append(int(now))
        now = ""
    elif i != " ":
        now+=i
o = str(Output)
f = open(DataPath + "1", 'w')
f.writelines(o[1:-1:1]+"\n")
print(o)
f.close()