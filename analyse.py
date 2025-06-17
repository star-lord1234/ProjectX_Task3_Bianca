import os

violations=0
forbiddenk=0
for dirpath, dirnames, filenames in os.walk("src"):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        with open(filepath, "r") as f:
            for line in f:
                if (line[0]=="#" and len(line)>80):
                    violations+=1
                    continue
                if(len(line)>80):
                    violations+=1
                if ("print(" in line and line[0]!='#'):
                    if(line.find("print(")<line.find('#') or line.find('#')==-1):
                        forbiddenk+=1
                if ("exec(" in line and line[0]!='#'):
                    if(line.find("print(")<line.find('#') or line.find('#')==-1):
                        forbiddenk+=1
                if ("eval(" in line and line[0]!='#'):
                    if(line.find("print(")<line.find('#') or line.find('#')==-1):
                        forbiddenk+=1
                if '"' in line:
                    if(line.count('"')%2!=0):
                        violations+=1
                if "'" in line:
                    if(line.count("'")%2!=0):
                        violations+=1
                if(line==""):
                    continue
        if(violations>=5 or forbiddenk>0):
            print(filepath+f": HIGH RISK")
        elif(violations<5 and violations!=0 ):
            print(filepath+": LOW RISK")
        elif(violations+forbiddenk==0):
            print(filepath+": CLEAR")
        violations=0
        forbiddenk=0
        


