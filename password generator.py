import tkinter as tk
from tkinter import ttk
import secrets, string

def random_password(length=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    pools = []
    if use_lower: pools.append(string.ascii_lowercase)
    if use_upper: pools.append(string.ascii_uppercase)
    if use_digits: pools.append(string.digits)
    if use_symbols: pools.append(string.punctuation)

    if not pools:
        return "Select at least one option!"

    pwd = [secrets.choice(pool) for pool in pools]
    all_chars = ''.join(pools)
    pwd += [secrets.choice(all_chars) for _ in range(length - len(pools))]
    secrets.SystemRandom().shuffle(pwd)
    return ''.join(pwd)

def password_strength(pwd):
    score = 0
    if any(c.islower() for c in pwd): score += 1
    if any(c.isupper() for c in pwd): score += 1
    if any(c.isdigit() for c in pwd): score += 1
    if any(c in string.punctuation for c in pwd): score += 1
    if len(pwd) >= 12: score += 1
    return score

def generate():
    pwd = random_password(
        length_var.get(),
        lower_var.get(),
        upper_var.get(),
        digits_var.get(),
        symbols_var.get()
    )
    entry.delete(0, tk.END)
    entry.insert(0, pwd)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(entry.get())
    root.update()

def update_strength_bar(pwd):
    score = password_strength(pwd)
    strength_var.set(score * 20)
    if score <= 2:
        strength_bar.config(style="Red.Horizontal.TProgressbar")
        strength_label.config(text="Weak", fg="red")
    elif score in (3,4):
        strength_bar.config(style="Orange.Horizontal.TProgressbar")
        strength_label.config(text="Medium", fg="orange")
    else:
        strength_bar.config(style="Green.Horizontal.TProgressbar")
        strength_label.config(text="Strong", fg="green")

def on_entry_change(*args):
    pwd = entry.get()
    update_strength_bar(pwd)

def toggle_visibility():
    entry.config(show="" if show_var.get() else "*")

root = tk.Tk()
root.title("Password Generator")
root.geometry("420x400")

style = ttk.Style(root)
style.theme_use("default")
style.configure("Red.Horizontal.TProgressbar", troughcolor="white", background="red")
style.configure("Orange.Horizontal.TProgressbar", troughcolor="white", background="orange")
style.configure("Green.Horizontal.TProgressbar", troughcolor="white", background="green")

tk.Label(root, text="Password Length:").pack(pady=5)
length_var = tk.IntVar(value=12)
tk.Scale(root, from_=6, to=32, orient="horizontal", variable=length_var).pack(pady=5)

lower_var = tk.BooleanVar(value=True)
upper_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include lowercase (a-z)", variable=lower_var).pack(pady=2)
tk.Checkbutton(root, text="Include uppercase (A-Z)", variable=upper_var).pack(pady=2)
tk.Checkbutton(root, text="Include numbers (0-9)", variable=digits_var).pack(pady=2)
tk.Checkbutton(root, text="Include symbols (!@#$...)", variable=symbols_var).pack(pady=2)

tk.Button(root, text="Generate Password", command=generate).pack(pady=5)

entry_var = tk.StringVar()
entry = tk.Entry(root, width=40, justify="center", textvariable=entry_var)
entry.pack(pady=5)
entry_var.trace_add("write", on_entry_change)

show_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Show password", variable=show_var, command=toggle_visibility).pack(pady=2)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

strength_var = tk.IntVar(value=0)
strength_bar = ttk.Progressbar(root, orient="horizontal", length=200,
                               mode="determinate", variable=strength_var, maximum=100,
                               style="Red.Horizontal.TProgressbar")
strength_bar.pack(pady=5)

strength_label = tk.Label(root, text="Strength", font=("Arial", 12))
strength_label.pack()

root.mainloop()