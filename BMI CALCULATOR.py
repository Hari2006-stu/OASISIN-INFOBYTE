from tkinter import *
from tkinter import ttk, messagebox
# Summa
def reset_entry():
    height_tf.delete(0, 'end')
    weight_tf.delete(0, 'end')

def calculate_bmi():
    try:
        kg = float(weight_tf.get())
        m = float(height_tf.get()) / 100
        if m <= 0 or kg <= 0:
            raise ValueError
        bmi = round(kg / (m * m), 1)
        bmi_index(bmi)
    except ValueError:
        messagebox.showerror('Input Error', 'Please enter valid numeric values for height and weight.')

def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('BMI Result', f'BMI = {bmi} is Underweight')
    elif 18.5 <= bmi <= 24.9:
        messagebox.showinfo('BMI Result', f'BMI = {bmi} is Normal')
    elif 25 <= bmi <= 29.9:
        messagebox.showinfo('BMI Result', f'BMI = {bmi} is Overweight')
    elif bmi >= 30:
        messagebox.showinfo('BMI Result', f'BMI = {bmi} is Obese')
    else:
        messagebox.showerror('BMI Result', 'Something went wrong!')

def on_enter(e): e.widget['style'] = 'Hover.TButton'
def on_leave(e): e.widget['style'] = 'TButton'

ws = Tk()
ws.title('BMI Calculator')
ws.geometry('360x220')
ws.configure(bg='#2e2e2e')

style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', background='#2e2e2e', foreground='white', font=('Segoe UI', 10))
style.configure('TEntry', fieldbackground='#3e3e3e', foreground='white')
style.configure('TButton', background='#007acc', foreground='white', font=('Segoe UI', 10), padding=6)
style.map('TButton', background=[('active', '#005f99')])
style.configure('Hover.TButton', background='#005f99', foreground='white')

frame = ttk.Frame(ws, padding=15)
frame.pack(expand=True)

ttk.Label(frame, text="Enter Height (cm)").grid(row=0, column=0, sticky=W, pady=5)
height_tf = ttk.Entry(frame, width=20)
height_tf.grid(row=0, column=1, pady=5)

ttk.Label(frame, text="Enter Weight (kg)").grid(row=1, column=0, sticky=W, pady=5)
weight_tf = ttk.Entry(frame, width=20)
weight_tf.grid(row=1, column=1, pady=5)

btn_frame = ttk.Frame(frame)
btn_frame.grid(row=2, columnspan=2, pady=15)

btn_cal = ttk.Button(btn_frame, text='Calculate', command=calculate_bmi)
btn_cal.pack(side=LEFT, padx=5)
btn_cal.bind("<Enter>", on_enter)
btn_cal.bind("<Leave>", on_leave)

btn_reset = ttk.Button(btn_frame, text='Reset', command=reset_entry)
btn_reset.pack(side=LEFT, padx=5)
btn_reset.bind("<Enter>", on_enter)
btn_reset.bind("<Leave>", on_leave)

btn_exit = ttk.Button(btn_frame, text='Exit', command=ws.destroy)
btn_exit.pack(side=RIGHT, padx=5)
btn_exit.bind("<Enter>", on_enter)
btn_exit.bind("<Leave>", on_leave)

ws.mainloop()