import z3
import sys


class loc:
    def __init__(self,r,c):
        self.row = r
        self.col = c
    
inputpath = sys.argv[1]
file = open(inputpath,"r")

vcarsh = []
vcarst = []
hcarst = []
hcarhs = []
mines = []

line1 = file.readline()
linep1 = line1.split(",")
size = linep1[0]
limit = linep1[1]


line1 = file.readline()
linep1 = line1.split(",")
rowr = linep1[0]
colr = linep1[1]

RedCarLoc = loc(rowr, colr)
count = 0
for x in file:
    count+=1
    if count>1:
        line = x.split(',')
        rowr = line[1]
        colr = line[2]

        
        carType = line[0]
        if carType==0:
            vcarsh.append(loc(rowr, colr))
            vcarst.append(loc(rowr+1, colr))
        elif carType==1:
            hcarsh.append(loc(rowr, colr))
            vcarst.append(loc(rowr, colr+1))
        else:
            mines.append(loc(rowr, colr))
            
  

s = z3.solver

s.model