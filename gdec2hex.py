import tkinter
from tkinter import messagebox
tk = tkinter.Tk()
tk.geometry("200x200")
def onclick():
    try:
        dec = int(ent.get())
    except:
        messagebox.showinfo("str","please insert an integer")
        return
    rem = dec
    quit = 1
    hex  = ''
    while quit != 0:
        quit = rem // 16
        rem = rem % 16
        if rem == 15:
            rem = "f"
        if rem == 14:
            rem = "e"
        if rem == 13:
            rem = 'd'
        if rem == 12:
            rem = 'c'
        if rem == 11:
            rem = 'b'
        if rem == 10:
            rem = 'a'
        #print(rem)
        hex = hex + str(rem)
        rem = quit

    messagebox.showinfo("hex","decimal: %i\nhexadecimal: %s"%(dec,hex[::-1]))
ent = tkinter.Entry(tk)
ent.pack()
btn = tkinter.Button(tk,command = onclick,text = "convert to hex")
btn.pack()
#dec = int(input("enter your decimal number:"))

tk.mainloop()