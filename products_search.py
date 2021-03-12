import os
import numpy as np
import pandas as pd
import tkinter as tk
root=tk.Tk()
v=tk.StringVar()



def good():
    search1=v.get()
    a=pd.read_excel(r"C:\Users\g\Desktop\sales (1)\20150211 MSRP Products Price list.xls",None)
    sheetnames=list(a.keys())

    print("we have sheet as follow"%(sheetnames))
    for sheetname1 in sheetnames:
        print("now searching",sheetname1)
        b=pd.read_excel(r"C:\Users\g\Desktop\sales (1)\20150211 MSRP Products Price list.xls",sheet_name=sheetname1)
        for x in range(len(b.index)):
                
                for y in b.columns:
                    #print(type(b[y]))
                     
                    if search1 in str(b.loc[x,y]).lower():
                        
                        print(b.loc[x,:])
b1=tk.Entry(root,textvariable=v)
b1.pack()
b2=tk.Button(root,text="search",command=good)
b2.pack()

root.mainloop()
