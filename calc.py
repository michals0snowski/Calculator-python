from tkinter import *
import ast

root =Tk()
root.title('Calculator by Michał Sosnowski')

# Wyświetlanie cyfr
i = 0
def get_number(num):
    global i
    display.insert(i,num)
    i+=1

# Działania
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length

display = Entry(root)
display.grid(row=1,columnspan=6)

# Reset
def clear_all():
    display.delete(0,END)

# Obliczanie
def calculate():
    entire_string = display.get()
    try:
        node = ast.parse(entire_string,mode="eval")
        result = eval(compile(node,'<string>','eval'))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")

# Funkcja cofnij
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"")

# Klawisze "1-9"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root,text=button_text,width=2,height=2,command=lambda text=button_text:get_number(text))
        button.grid(row=x+2,column=y)
        counter+=1

# Klawisz "0"
button = Button(root,text="0",width=2,height=2,command=lambda :get_number(0))
button.grid(row=5,column=1)

# Operatory działań
count = 0
operatios =["+", "-", "*", "/", "*3.14", "%", "(", "**", ")"]
for x in range(4):
    for y in range(3):
        if count<len(operatios):
            button = Button(root,text=operatios[count],width=2,height=2,command=lambda text=operatios[count]:get_operation(text))
            count+=1
            button.grid(row=x+2,column=y+3)

# Klawisz "AC"            
Button(root,text="AC",width=2,height=2,command=clear_all).grid(row=5,column=0)

# Klawisz "="
Button(root,text="=",width=2,height=2,command=calculate).grid(row=5,column=2)

# Klawisz kasowania
Button(root,text="del",width=2,height=2,command=lambda :undo()).grid(row=5,column=5)

root.mainloop()