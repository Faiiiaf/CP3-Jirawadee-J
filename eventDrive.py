from tkinter import *
import math

def leftclick(event):
    result= float(textbox2.get())/math.pow(float(textbox.get())/100,2)
    labelResult.configure(text=result)
    if result > 29.9:
        labelBMI.configure(text="อ้วนมาก พบแพทย์ด่วน!", fg="red")
    elif result > 24.9:
        labelBMI.configure(text="อ้วนเกินควรออกกำลังกาย", fg="orange")
    elif result > 22.9:
        labelBMI.configure(text="น้ำหนักเกินเกณฑ์", fg="yellow")
    elif result > 18.5:
        labelBMI.configure(text="น้ำหนักปกติ", fg="green")
    else:
        labelBMI.configure(text="ผอมเกินไป", fg="red")




main = Tk()
labelhight = Label(main,text="ส่วนสูง (cm.)",font=('FC Vision Rounded[Non-cml.]Bold',10))
labelhight.grid(row=1,column=1)
textbox = Entry(main)
textbox.grid(row=1,column=2)
labelweight = Label(main,text="น้ำหนัก (kg.)",font=('FC Vision Rounded[Non-cml.]Bold',10))
labelweight.grid(row=2,column=1)
textbox2 = Entry(main)
textbox2.grid(row=2,column=2)
button = Button(main,text = "คำนวณ",font=('FC Vision Rounded[Non-cml.]Bold',10))
button.grid(row=3,column=2)
button.bind('<Button-1>',leftclick)
labelResult = Label(main,text = "ผลลัพธ์",font=('FC Vision Rounded[Non-cml.]Bold',10))
labelResult.grid(row=4,column=2)

labelBMI = Label(main,text = "",font=('FC Vision Rounded[Non-cml.]Bold',10))
labelBMI .grid(row=4,column=1)

main.mainloop()
