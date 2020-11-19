import tkinter as tk



def trial():
    

    ent1 = tk.Entry()
    ent1.grid(row=10,column=2)
        
    ent2 = tk.Entry()
    ent2.grid(row=12,column=2)
        
    ent3 = tk.Entry()
    
    ent3.grid(row=14,column=2)
    ent4 = tk.Entry()
    ent4.grid(row=16,column=2)
    ent5 = tk.Entry()
    ent5.grid(row=18,column=2)
    cls_btn = tk.Button(text='close', command=cls_win())
    cls_btn.grid(row = 30, column = 2)
    lbE = tk.Label(text='Enter your name')
    lbE.grid(row=10,column=1)
    lbD = tk.Label(text='Enter your age please:')
    lbD.grid(row=12,column=1)
    lbd = tk.Label(text='Do you have diabetes [TRUE/FALSE]')
    lbd.grid(row=14,column=1)
    lbL = tk.Label(text='Do you have abnormal BP [TRUE/FALSE]')
    lbL.grid(row=16,column=1)
    lbw = tk.Label(text='Do you have Respiratory Illness [TRUE/FALSE]')
    lbw.grid(row=18,column=1)

    name1 = float(ent1.get())
    name2= float(ent2.get())
    name3= float(ent3.get())
    name4= float(ent4.get())
    name5= float(ent5.get())
    return ent1,ent2,ent3,ent4,ent5
def cls_win():
    app.destroy()



app = tk.Tk()
w, h = app.winfo_screenwidth(), app.winfo_screenheight()
app.geometry("%dx%d+0+0" % (w, h))
app.title('trial')
trial()
app.mainloop()

'''if __name__ == '__main__':
    main()
import tkinter as tk

root = tk.Tk()

e1 = tk.Entry(root)
e1.pack()
e2 = tk.Entry(root)
e2.pack()

# This function is executed by the submit button
# it retrieves the outputs of both entry boxes
def submit():
    print e1.get()
    print e2.get()

tk.Button(root,text="submit",command=submit).pack()

root.mainloop()'''
