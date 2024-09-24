from tkinter import*
import tkinter as tk
from tkinter import ttk
import tkinter.font as font 

root=tk.Tk()
root.title("Distance Converter")
# root.geometry("600x400")

font.nametofont("TkDefaultFont").configure(size=15)

root.columnconfigure(0,weight=1)

main=ttk.Frame(root,padding=(30,10))
main.grid()
#operation
meter_value=tk.StringVar()
feet_value=tk.StringVar(value="feet shown here")

def calculate_feet(*args):
    try:
        meters=float(meter_value.get())
        feet=meters*3.28084
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass

#widget
meter_level=ttk.Label(main,text="Meter:")
meter_txt=ttk.Entry(main,width=10,textvariable=meter_value,font=(None, 15))
meter_txt.focus()

feet_lvl=ttk.Label(main,text="Feet:")
feet_txt=ttk.Label(main,textvariable=feet_value)

calc_button=ttk.Button(main,text="Calculate",command=calculate_feet)

#Layout
meter_level.grid(row=1,column=0,sticky="w", padx=5, pady=5)
meter_txt.grid(row=1,column=1,sticky="ew", padx=5, pady=5)
feet_lvl.grid(row=2,column=0,sticky="w", padx=5, pady=5)
feet_txt.grid(row=2,column=1, sticky="ew",padx=5, pady=5)
calc_button.grid(column=0, row=3, columnspan=2, sticky="EW", padx=5, pady=5)


root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)
root.mainloop()

#madisonobr990@hotmail.com
#EWESA%DD7h7=dbP