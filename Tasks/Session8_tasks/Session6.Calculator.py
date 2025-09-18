from tkinter import *

window = Tk()

window.title("Calculator")

window.config(bg='grey',pady=10,padx=0) 
window.resizable(height=False,width=False) 
window.geometry('350x470')
label = Label(window,text="Welcome!",font=("Arial",24,"bold"),fg="black",bg="grey")
label.pack()

# label=Label(window,text="Welcome!",font=("Arial",12,"bold"),fg="black",bg="grey")
# label.place(x=0,y=2)

# label2=Label(window,text="Welcome!",font=("Arial",12,"bold"),fg="black",bg="grey")
# label.place(x=0,y=4)



click_count = 1
num1 = 0
num2 = 0
total = 0
last_op = []
nums = []





def btn_click(btn):
   global last_op
   global nums

   if len(nums) == len(last_op):
        nums.append(btn)


   elif len(nums) > len(last_op):
        old_num = nums[-1]
        new_num = old_num + btn
        nums[-1] = new_num
       
   label.config(text=nums[-1])
   print(nums)
   print(last_op)
   
        

def calc(op):
    global last_op
    global nums
    global total

    if len(nums) > len(last_op):
        last_op.append(op)

        if len(nums) >= 2:
            if last_op[-1] == "+":
                total = int(nums[-2]) + int(nums[-1])
                if last_op[-1] == last_op[-2]:
                    label.config(text=total)
                    nums[-1] = str(total)

            elif last_op[-1] == "_":
                total = int(nums[-2]) - int(nums[-1])
                if last_op[-1] == last_op[-2]:
                    label.config(text=total)
                    nums[-1] = str(total)

            elif last_op[-1] == "X":
                total = int(nums[-2]) * int(nums[-1])
                if last_op[-1] == last_op[-2]:
                    label.config(text=total)
                    nums[-1] = str(total)

            elif last_op[-1] == "/":
                total = int(nums[-2]) / int(nums[-1])
                if last_op[-1] == last_op[-2]:
                    label.config(text=total)
                    nums[-1] = str(total)

            elif last_op[-1] == "delete":
                nums[-1].pop()
                print(nums)
                
            elif last_op[-1] == "C":
                nums = []
                last_op = []
                label.config(text="0")
                print(nums)
                print(last_op)

            if last_op[-1] == "=":
                label.config(text=total)
                print(total)
            else: pass
        else: pass


    else:
        pass





btn1 = Button(window,font=("Arial",12,"bold"),bg="black",fg="white",text="1")
btn1.place(x=0,y=220,width=87.5,height=60)
btn1.config(command=lambda:btn_click(btn='1'))

btn2 = Button(window,font=("Arial",12,"bold"),bg="black",fg="white",text="2")
btn2.place(x=87.5,y=220,width=87.5,height=60)
btn2.config(command=lambda:btn_click(btn='2'))

btn3 = Button(window,font=("Arial",12,"bold"),bg="black",fg="white",text="3")
btn3.place(x=175,y=220,width=87.5,height=60)
btn3.config(command=lambda:btn_click(btn='3'))

btn16 = Button(window,font=("Arial",12,"bold"),bg="#393d3f",fg="white",text="X") # (X)
btn16.place(x=262.5,y=220,width=87.5,height=60)
btn16.config(command=lambda:calc(op=btn16['text']))

btn4 = Button(window,font=("Arial",12,"bold"),bg="black",fg="white",text="4")
btn4.place(x=0,y=280,width=87.5,height=60)
btn4.config(command=lambda:btn_click(btn='4'))

btn5 = Button(window,font=("Arial",12,"bold"),bg="black",fg="white",text="5")
btn5.place(x=87.5,y=280,width=87.5,height=60)
btn5.config(command=lambda:btn_click(btn='5'))

btn6 = Button(window,font=("Arial",12,"bold"),bg="black",fg="white",text="6")
btn6.place(x=175,y=280,width=87.5,height=60)
btn6.config(command=lambda:btn_click(btn='6'))

btn17 = Button(window,font=("Arial",12,"bold"),bg="#393d3f",fg="white",text="_") # (_)
btn17.place(x=262.5,y=280,width=87.5,height=60)
btn17.config(command=lambda:calc(op=btn17['text']))

btn7 = Button(window,font=("Arial",12,"bold"),bg="black",fg="white",text="7")
btn7.place(x=0,y=340,width=87.5,height=60)
btn7.config(command=lambda:btn_click(btn='7'))

btn8 = Button(window,font=("Arial",12,"bold"),bg="black",fg="white",text="8")
btn8.place(x=87.5,y=340,width=87.5,height=60)
btn8.config(command=lambda:btn_click(btn='8'))

btn9 = Button(window,font=("Arial",12,"bold"),bg="black",fg="white",text="9")
btn9.place(x=175,y=340,width=87.5,height=60)
btn9.config(command=lambda:btn_click(btn='9')) 

btn10 = Button(window,font=("Arial",12,"bold"),bg="#393d3f",fg="white",text="+") # (+)
btn10.place(x=262.5,y=340,width=87.5,height=60)
btn10.config(command=lambda:calc(op=btn10['text'])) 

btn11 = Button(window,font=("Arial",12,"bold"),bg="black",fg="white",text=".") # (.)
btn11.place(x=0,y=400,width=87.5,height=60)
btn11.config(command=lambda:btn_click(btn=btn11)) 

btn0 = Button(window,font=("Arial",12,"bold"),bg="black",fg="white",text="0") 
btn0.place(x=87.5,y=400,width=87.5,height=60)
btn0.config(command=lambda:btn_click(btn='0')) 

btn12 = Button(window,font=("Arial",12,"bold"),bg="#393d3f",fg="white",text="/") # (/)
btn12.place(x=175,y=400,width=87.5,height=60)
btn12.config(command=lambda:calc(op=btn12['text'])) 

btn13 = Button(window,font=("Arial",12,"bold"),bg="lightgrey",fg="black",text="=") # (=)
btn13.place(x=262.5,y=400,width=87.5,height=60)
btn13.config(command=lambda:calc(op=btn13['text']))

btn14 = Button(window,font=("Arial",12,"bold"),bg="#393d3f",fg="white",text="delete") # (delete)
btn14.place(x=262.5,y=180,width=87.5,height=40)
btn14.config(command=lambda:calc(op=btn14['text']))

btn15 = Button(window,font=("Arial",12,"bold"),bg="#393d3f",fg="white",text="C") # (c)
btn15.place(x=175,y=180,width=87.5,height=40)
btn15.config(command=lambda:calc(op=btn15['text']))


window.mainloop()






#         if result == "X":
#             total = num1 * num2
#             label.config(text=total)
    
#         if result == "/":
#             total = num1 / num2
#             label.config(text=total)
    
#         if result == "=":
#             label.config(text=total)
    
#         if result == "C":
#             num1 = 0
#             num2 = 0
#             label.config(text=total)

#         if result == "delete":
#             if num2 != 0:
#                 num2 = 0
#             elif num1 != 0:
#                 num1 = 0
            
# def btn_equal():
#    pass

# def btn_delete():
#    global num1
#    global num2
#    global click_count
#    if num2 != 0:
#         num2 = 0
#         click_count -= 1
#    elif num1 != 0:
#        num1 = 0    

# def btn_minus():
#     global num1
#     global num2
#     global click_count
#     if click_count >= 1:
#         total = num1 - num2
#         print(total)
#         label.config(text=total)
#         click_count = 0
#         num1 = total
#         num2 = 0
#     else:
#         pass

# def btn_multiply():
#     global num1
#     global num2
#     global click_count
#     if click_count >= 1:
#         total = num1 * num2
#         print(total)
#         label.config(text=total)
#         click_count = 0
#         num1 = total
#         num2 = 0
#     else:
#         pass

# def btn_divide():
#    global num1
#    global num2
#    global click_count
#    if click_count >= 1:
#         total = num1 / num2
#         print(total)
#         label.config(text=total)
#         click_count = 0
#         num1 = total
#         num2 = 0
#    else:
#         pass