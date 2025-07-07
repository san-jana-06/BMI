# Weight_kg=float(input("Enter weight in kg"))
# Height_meter=float(input("Enter Height in Meters"))
# BMI=Weight_kg/Height_meter*Height_meter
# print("BMI is:",BMI)

from tkinter import*
from tkinter import ttk

#Dark Mode Colors
co0="#E1E1E1" #Light gray text
co1="#FF9FDF" #black background
co2="#BB86FC" #purple for button
co3="#A4F7C6" #Dark gray frames frames
co4="lightblue"  #blue for highlights

root=Tk()
root.title('BMI Calculator')
root.geometry('450x400')
root.config(bg=co1)
 
style=ttk.Style(root)
style.theme_use("clam")
#frames
frame_top=Frame(root,width=360,height=70,bg=co4,pady=10,padx=10)
frame_top.grid(row=0,column=0,sticky=NSEW)

frame_bottom=Frame(root,width=360,height=320,bg=co3,pady=20,padx=20)
frame_bottom.grid(row=1,column=0,sticky=NSEW)

#configuring Top frame----
app_name=Label(frame_top,text="BMI Calculator",width=23,height=1,padx=0,relief="flat",anchor="center",font=('Helvetic 20 bold'),bg=co4,fg='black')
app_name.place(x=0,y=15)

#function to calculate BMI
def calculate():
    try:
        weight=float(e_weight.get())
        height=float(e_height.get())**2
        result=weight/height
        if result<18.5:
            l_result_text['text']="your BMI is: Underweight"
        elif result<24.9:
            l_result_text['text']="Your BMI is: Normal"
        elif result<29.9:
            l_result_text['text']="your BMI is: Overweight"
        else:
            l_result_text[' text']="Your BMI is: Obesity"
        l_result['text']=("{:.2f}".format(result))
    except ValueError:
        l_result_text['text']="Enter a valid  number"
        l_result['text']="----"
       
        
#configuring bottom frame----
l_weight=Label(frame_bottom,text="Enter your weigth(kg)",width=23,height=1,padx=0,relief='flat',anchor="center",font=('Helvetic 12 bold'),bg=co1,fg='black')
l_weight.grid(row=0,column=0,sticky=NSEW,pady=10,padx=10)
e_weight=Entry(frame_bottom,width=15,font=('Helvetica 12'),justify="center",relief='flat',bg=co1,fg="black")
e_weight.grid(row=0,column=1,pady=10,padx=10)

l_height=Label(frame_bottom,text="Enter your heigth(m)",width=23,height=1,padx=0,relief="flat",anchor="center",font=('Helvetic 12 bold'),bg=co1,fg='black')
l_height.grid(row=1,column=0,sticky=NW,pady=10,padx=10)
e_height=Entry(frame_bottom,width=15,font=('Helvetica 12'),justify="center",relief='flat',bg=co1,fg="black")
e_height.grid(row=1,column=1,pady=10,padx=10)

l_result=Label(frame_bottom,text="-----",width=8,height=0,padx=6,pady=12,relief="flat",anchor="center",font=('Helvetic 20 bold'),bg=co2,fg='black')
l_result.grid(row=2,column=0,pady=30,padx=20,columnspan=2)

l_result_text=Label(frame_bottom,text="",width=37,height=1,relief="flat",anchor="center",font=('Helvetic 12 bold italic'),bg=co3,fg='black')
l_result_text.grid(row=3,column=0,pady=10,padx=10,columnspan=2)

b_calculate=Button(frame_bottom, command=calculate,text="Calculate",width=34,height=1,overrelief=SOLID,bg=co2,fg='black',font=('Helvetica 12 bold'),anchor="center")
b_calculate.grid(row=4,column=0,pady=10,padx=10,columnspan=2)


root.mainloop()
