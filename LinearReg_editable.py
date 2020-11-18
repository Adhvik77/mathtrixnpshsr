'''two strings need to be imported from the dataset
one, the first is x, which acts as the x axis
the other is the y axis
the x and y axes' arguments have to be lists
i have passed them both as method params'''
import csv
import health_data as hd
import numpy as np
from sklearn.linear_model import LinearRegression
def linReg(tup,pred=[0.0]):
    pred=np.array(pred).reshape(-1,1)
    x=tup[0]
    y=tup[1]
   ''' x1=t[0]
    x2=t[2]
    x3=t[3]
    x4=t[4]
    y=t[1]
    arrX=[]
    x=np.array(arr)#.reshape(-1,1)
    y=np.array(y)'''
    model=LinearRegression().fit(x,y)
    #a tuple is returned from this method
    #t[0]=R^2, t[1]=intercept and t[2]=slope
    print("hello")
    t=(model.intercept_,model.coef_,model.predict(pred))
    return t

def makeTupleList(n1,n2,name):
    l1=hd.getColumn(n1,name)
    l2=hd.getColumn(n2,name)
    dis=hd.getDiseases(name)
    l3=dis[0]
    l4=dis[1]
    l5=dis[2]
    lt=[]
    for i in range(len(l1)):
        val=None
        if l2[i][0]=="A":
            val=1
        else:
            val=0
        lt+=[(l1[i],val,l3[i],l4[i],l5[i])]
    return lt
def getArray(t):
    arrx,arry=[],[]
    x1=t[0]
    x2=t[2]
    x3=t[3]
    x4=t[4]
    arry=t[1]

    for i in range(len(x1)):
        x.append([x1[i],x2[i],x3[i],x4[i]])
    
    x=np.array(arrx)#.reshape(-1,1)
    y=np.array(arry)
    
    return (x,y)


def implement(n1,n2,name="COVID_Dataset_2.CSV"):
    l=makeTupleList(n1,n2,name)
    t=getArray(l)
    t1=linReg(t)
    print(t1)
    return
implement(5,9)

'''def getInfo():
    arr1=hd.getDiseases()
    temp=hd.getColumn(5)
    arr2=[]
    
    #for i in temp:
        #n=i/10
        #arr2.append(n)'''
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
