from tkinter import *
import  random



root=Tk()
root.geometry("500x500")
root.configure(bg="Lavender")
root.title('Rock_paper_scissor')


l1=Label(root,text="Rock Paper Scissor Game ",font=("Arial",25),fg="blue",bg="Lavender")
l1.grid(pady=10,padx=50,columnspan=3)
l2=Label(root,text="Player             VS          Computer",font=("Arial",18),fg="black",bg="Lavender")
l2.grid(pady=20,padx=50,columnspan=3)



x=StringVar()
e=Entry(root,font=("Arial",29 ),width=18,textvariable=x,fg="red")
e.grid(pady=20,columnspan=3)


def show(q):
  
  a=random.randint(1,3)
  print(a) 
  l2=Label(root,text=f"{q}                  VS                     {a}",font=("Arial",18),fg="black",bg="Lavender")
  l2.grid(pady=20,padx=50,columnspan=3,row=4)
  if(q==a):
    x.set("********* Drow *********")
  elif((q==1 and a==3) or (q==2 and a==1) or (q==3 and a==2)):
    x.set("****** Player Win ******")
  else:
    x.set(" *** Computer Win ***")



b1=Button(root,text="ROCK",font=("Arial",20),width=8,bg="MediumSlateBlue",fg="White",command=lambda:show(1))
b1.grid(pady=20,row=5,column=0)
b2=Button(root,text="PAPER",font=("Arial",20),width=8,bg="MediumSlateBlue",fg="White",command=lambda:show(2))
b2.grid(pady=20,row=5,column=1)
b3=Button(root,text="SCISSOR",font=("Arial",20),width=8,bg="MediumSlateBlue",fg="White",command=lambda:show(3))
b3.grid(pady=20,row=5,column=2)


root.mainloop()
