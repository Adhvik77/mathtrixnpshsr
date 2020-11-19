'''
Vital info by grid
author: Ishaan Mishra, Dhruv Bhatia
18th November, 2020
'''


#------------------------INITIALISING------------------------#
import csv
L=[]
G=[]
GI=[]
grid_width=20
grid_length=20


#------------------------SETUP------------------------#

class stats:
    '''
    STATISTICS-
    population, infections, deaths, death rate, [disease wise death rate],
    [age wise death rate], time lag 
    '''
    def __init__(self):
        self.pop=0
        self.inf=0
        self.deds=0
        self.dr=0
        self.DD=[]
        self.DA=[[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.t=0
        self.irate=0
    def display_data(self):
        print(self.pop, self.inf, self.deds, self.dr, self.DD, self.DA, self.t, self.irate)


with open ('COVID_Dataset.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        L.append(row)    


totalpop=0
total=stats()
pop=[]
with open('Population.csv','r') as f:
    c=0
    reader=csv.reader(f)
    for row in reader:  
        if c!=0:
            pop.append(row[2])
            
            
        c+=1
counter=0
for i in range(grid_width):
    g=[]
    for j in range(grid_length):
        k=stats()
        k.pop=int(pop[counter][:-2])
        totalpop+=int(pop[counter][:-2])
        g.append(k)
        counter+=1
    G.append(g)

total.pop=totalpop

for i in range(grid_width):
    g=[]
    for j in range(grid_length):
        g.append([])
    GI.append(g)
c=0    
for i in L:
    if c!=0:
        GI[int(i[2])-1][int(i[3])-1].append(i)      
    c+=1


tval=[
[True, True, True],
[True, True, False],
[True, False, True],
[True, False, False],
[False, True, True],
[False, True, False],
[False, False, True],
[False, False, False]]




#------------------------FUNCTIONS------------------------#

def checkbelikeage(L, DA):
    L[4]=int(L[4])
    b1,b2,b3,b4,b5=DA
    if L[4]<=10:
        b1[1]+=1
        if L[8]=='Dead':
            b1[0]+=1
    elif L[4]<=20:
        b2[1]+=1
        if L[8]=='Dead':
           b2[0]+=1
    elif L[4]<=40:
        b3[1]+=1
        if L[8]=='Dead':
            b3[0]+=1
    elif L[4]<=60:
        b4[1]+=1
        if L[8]=='Dead':
            b4[0]+=1
    elif L[4]>60:
        b5[1]+=1
        if L[8]=='Dead':
            b5[0]+=1
    return([b1,b2,b3,b4,b5])



def checkbelikedisease(t1,t2,t3, L):
    ded=0
    total=0
    for i in L:
        if i[5]==str(t1) and i[6]==str(t2) and i[7]==str(t3):
            total+=1
            if i[8]=='Dead':
                ded+=1
    if total==0:
        rate='N/A' #if there is no one with the diseases infected in the area
    else:
        rate= round(ded/total*100,2)

    return(rate)


cellcount=1

def calc_stats(L,stats):
    global cellcount
    global tval
    c=0

    for j in tval:
                stats.DD.append(checkbelikedisease(j[0],j[1],j[2], L))
    for i in L:
   
        if c!=0:
            checkbelikeage(i, stats.DA)
            stats.inf+=1
            if i[8]=='Dead':
                stats.deds+=1
            '''for j in tval:
                stats.DD.append(checkbelikedisease(j[0],j[1],j[2], L))
            stats.DA=checkbelikeage(i, stats.DA)'''
            stats.t+=(int(i[1])-int(i[0]))/len(L)
        r=stats.deds/(stats.pop)*100
        stats.sr=round(r,2)    
        c+=1
    stats.t=round(stats.t,2)
    stats.irate=round(stats.inf/stats.pop*100,2)
    if stats.inf==0:
        stats.dr='N/A'
    else:    
        stats.dr=round(stats.deds/stats.inf*100,2)
    for i in range(len(stats.DA)):
        if stats.DA[i][1]==0:
            stats.DA[i]='N/A'
        else:
            stats.DA[i]=round(stats.DA[i][0]/stats.DA[i][1]*100,2)
        

    #print(cellcount, 'calculated')
    cellcount+=1
                

#------------------------DATA_COLLECTION------------------------#
tetet=0
    
for i in range(grid_width):
    for j in range(grid_length):
        calc_stats(GI[i][j],G[i][j])

calc_stats(L, total)
G[12][7].display_data()
total.display_data()

print('Well, it seems to be working')


    

#------------------------DATA_INTERPRETATION------------------------#
'''
- c1: high cases, high lag = suggest testing
- c2: many old dedz, = improve health infra
- c3: inf/pop high = implement lockdown
- c4: abnormally high death rate = check for varying strain
- c5: herd immunity distance time(60%)
'''
lm=10
c1=c2=c3=c4=c5=[]
c1max=c2max=c3max=c4max=[]

for i in range(lm):
    c1.append(G[0][i])
    c2=c3=c4=c1
    c1max.append([G[0][i].irate , G[0][i].t])
    c2max.append(G[0][i].DA[4])
    c3max.append(G[0][i].irate)
    c4max.append(G[0][i].dr)
    
    if G[0][i].irate>=60:
        c5.append(j)

for i in range(lm-1):
    for j in range(lm-i-1):
        print(c4max)
        if c4max[j]>c4max[j+1]:
            c4max[j],c4max[j+1]=c4max[j+1],c4max[j]
            c4[j],c4[j+1]=c4[j+1],c4[j]
        if c3max[j]>c3max[j+1]:
            c3max[j],c3max[j+1]=c3max[j+1],c3max[j]
            c3[j],c3[j+1]=c3[j+1],c3[j]
        if c2max[j]>c2max[j+1]:
            c2max[j],c2max[j+1]=c2max[j+1],c2max[j]
            c2[j],c2[j+1]=c2[j+1],c2[j]
'''

cut=0
for i in G:
    if cut==0:
        for j in i[lm:]:
            cut+=1
    else:
        for j in i:
            #herd immunity
            if j.irate>=60:
                c5.append(j)

            #lockdown
            if 
    


'''












