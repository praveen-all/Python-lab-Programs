import tkinter as tk
root=tk.Tk()
def calculate_bmi():
    wieght=float(weight_entry.get())
    height=float(height_entry.get())
    bmi=round(wieght/(height**2),2)
    bmi_label.config(text=f"BMI:{bmi}")
    


root.title("BMI Calculator")
weight_label=tk.Label(root,text="Weight(kg):")
weight_label.grid(row=0,column=0)
weight_entry=tk.Entry(root)
weight_entry.grid(row=0,column=1)

height_Lable=tk.Label(root,text="Height (m):")
height_Lable.grid(row=1,column=0)
height_entry=tk.Entry(root)
height_entry.grid(row=1,column=1)

calculate_btn=tk.Button(root,text="Calculate BMI",command=calculate_bmi)
calculate_btn.grid(row=2,column=0,columnspan=2)
bmi_label=tk.Label(root,text="")
bmi_label.grid(row=3,column=0,columnspan=2)

root.mainloop()

