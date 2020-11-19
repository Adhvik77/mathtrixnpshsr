import LinearRegEditable as lr
import healthDataEditable as hd
import tkinterfinal as tf
from tkinter import *
#import ishaan's file

class results:
    
    def __init__(self,win):
        #now displaying data
        
        self.lb1=Label(win, text='According to your age, your chances of survival are:')
        self.lb2=Label(win, text='According to your health conditions, your chances of survival are:')
        self.lb3=Label(win, text='Overall, your chances of survival are:')
        '''self.lbl4=Label(win, text='Do you have abnormal BP? [TRUE/FALSE]')
        self.lbl5=Label(win, text='Do you have respiratory disorders? [TRUE/FALSE]')
        self.lbl6=Label(win, text='Enter your x coordinate')
        self.lbl7=Label(win, text='Enter your y coordinate')'''

        #creating textboxes
        self.tt1=Entry(bd=3)
        self.tt2=Entry(bd=3)
        self.tt3=Entry(bd=3)
        '''self.t4=Entry(bd=3)
        self.t5=Entry(bd=3)
        self.t6=Entry(bd=3)
        self.t7=Entry(bd=3)'''
        
        #insertion
        self.tt1.insert(END, str(result_age*100)+"%")
        self.tt2.insert(END, str(result_disease*100)+"%")
        self.tt3.insert(END, str(result_final*100)+"%")
        '''p1=PhotoImage(file='Unknown.png')
        Label(win,image=p1).place(x=60,y=90)'''
        #placing
        self.lb1.place(x=0, y=400)
        self.lb2.place(x=0, y=450)
        self.lb3.place(x=0, y=500)
        '''self.lbl4.place(x=0, y=100)
            self.lbl5.place(x=0, y=150)
            self.lbl6.place(x=0, y=250)
            self.lbl7.place(x=0, y=300)'''
            
        self.tt1.place(x=405, y=400)
        self.tt2.place(x=405, y=450)
        self.tt3.place(x=405, y=500)
        '''self.t4.place(x=350, y=150)
            self.t5.place(x=270, y=200)
            self.t6.place(x=150, y=250)
            self.t7.place(x=150, y=300)'''
        
def final():
    windowf=Tk()
    mywin=results(windowf)
    windowf.title('COVID Data Results')
    windowf.geometry("2560x1600")
    canvas = Canvas(windowf, width = 464, height = 315)      
    canvas.pack()      
    img = PhotoImage(file="unknown-1.png")      
    canvas.create_image(20,20, anchor=NW, image=img) 
    windowf.mainloop()

res=tf.main()
#print(res)
age=[int(res[1])]
disease=[int(res[2]),int(res[3]),int(res[4])]
indep=age+disease
#print(age,disease,indep)
#print(lr.implement(disease,age,indep,5,9))
result_disease,result_age,result_final=lr.implement(disease,age,indep)
#print(result_disease,result_age,result_final)

final()
