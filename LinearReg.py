'''two strings need to be imported from the dataset
one, the first is x, which acts as the x axis
the other is the y axis
the x and y axes' arguments have to be lists
i have passed them both as method params'''
import csv
import health_data as hd
import numpy as np
from sklearn.linear_model import LinearRegression
def linReg(t,pred=[0.0]):
    pred=np.array(pred).reshape(-1,1)
    x=t[0]
    y=t[1]
    x=np.array(x).reshape(-1,1)
    y=np.array(y)
    model=LinearRegression().fit(x,y)
    #a tuple is returned from this method
    #t[0]=R^2, t[1]=intercept and t[2]=slope
    print("hello")
    t=(model.intercept_,model.coef_,model.predict(pred))
    return t
def getInfo():
    arr1=hd.getDiseases()
    temp=hd.getColumn(5)
    arr2=[]
    
    #for i in temp:
        #n=i/10
        #arr2.append(n)




def makeTupleList(n1,n2,name):
    l1=hd.getColumn(n1,name)
    l2=hd.getColumn(n2,name)
    lt=[]
    for i in range(len(l1)):
        val=None
        if l2[i][0]=="A":
            val=1
        else:
            val=0
        lt+=[(l1[i],val,)]
    return lt
def getArray(lt):
    x,y=[],[]
    for i in lt:
        x+=[i[0]]
        y+=[i[1]]
    return (x,y)

'''def quicksortbelike(l):
    length=len(l)
    if length<=1:
        return l
    else:
        pivot=l.pop()
    itemg=[]
    iteml=[]
    for item in l:
        if item[0] > pivot[0]:
            itemg.append(item)
        else:
            iteml.append(item)

    return quicksortbelike(iteml) + [pivot] + quicksortbelike(itemg)
def selSort(l):
    for i in range(len(l)):
        dat=l[i][0]
        ind=i
        for j in range(i+1,len(l)):
            if l[j][0]<dat:
                dat=l[j][0]
                ind=j
        l[ind],l[i]=l[i],l[ind]'''
def implement(n1,n2,name="COVID_Dataset_2.CSV"):
    l=makeTupleList(n1,n2,name)
    t=getArray(l)
    t1=linReg(t)
    print(t1)
    return
implement(5,9)
    
    

        

