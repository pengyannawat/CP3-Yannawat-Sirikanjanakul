# สร้างโปรแกรมคำนวณดัชนีมวลกาย (BMI) = น้ำหนัก(kg) / ส่วนสูง^2(m) จาก Lecture99
# Exercise เพิ่มการแสดงผลระบุเกณฑ์จากค่าBMIที่คำนวณได้

from tkinter import *
import math

def leftCLickOnButton(event):
    print(HeightTextBox.get())
    print(WeightTextBox.get())
    H = math.pow(float(HeightTextBox.get())/100,2)
    W = float(WeightTextBox.get())
    BMI = W/H
    print("BMI ของคุณคือ ", BMI)
    if BMI >= 30:
        labelResult.configure(text=BMI)
        labelResult2.configure(text="อ้วนมาก")
    elif BMI >= 25:
        labelResult.configure(text=BMI)
        labelResult2.configure(text="อ้วน")
    elif BMI >= 23:
        labelResult.configure(text=BMI)
        labelResult2.configure(text="น้ำหนักเกิน")
    elif BMI >= 18.6:
        labelResult.configure(text=BMI)
        labelResult2.configure(text="น้ำหนักปกติ")
    else:
        labelResult.configure(text=BMI)
        labelResult2.configure(text="ผอมเกินไป")

Window = Tk()  # สร้างหน้าต่างชื่อ Window

labelHeight = Label(Window, text = "ส่วนสูง(cm.)", font =("TH SarabunPSK",16))
labelHeight.grid(row=0,column=0)
HeightTextBox = Entry(Window)
HeightTextBox.grid(row=0,column=1)
labelWeight = Label(Window, text = "น้ำหนัก(kg.)", font =("TH SarabunPSK",16))
labelWeight.grid(row=1,column=0)
WeightTextBox = Entry(Window)
WeightTextBox.grid(row=1,column=1)
calculateButton = Button(Window, text = "คำนวณ", font =("TH SarabunPSK",18), fg = "blue", bg = "yellow", width = 20) # สร้างปุ่มButton"คำนวณ"
calculateButton.grid(row=3,column=0)
calculateButton.bind('<Button-1>', leftCLickOnButton)
labelResult = Label(Window, text = "ค่าBMI", font =("TH SarabunPSK",18))
labelResult.grid(row=3,column=1)
labelResult2 = Label(Window, text = "หลักเกณฑ์", font =("TH SarabunPSK",18))
labelResult2.grid(row=4,column=1)


Window.mainloop()