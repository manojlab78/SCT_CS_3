import tkinter as tk
from tkinter import messagebox
import re


def check_strength():
    password = entry.get()

    if password == "":
        messagebox.showwarning("Input Error", "Please enter a password")
        return

    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Use at least 8 characters")

    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        strength += 1
    else:
        feedback.append("Use both uppercase and lowercase")

    if re.search("[0-9]", password):
        strength += 1
    else:
        feedback.append("Add numbers")

    if re.search("[@#$%^&+=]", password):
        strength += 1
    else:
        feedback.append("Add special characters")

    # Result
    if strength == 4:
        result = "Strong Password 💪"
        color = "green"
    elif strength == 3:
        result = "Medium Password ⚠️"
        color = "orange"
    else:
        result = "Weak Password ❌"
        color = "red"

    result_label.config(text=result, fg=color)

    if feedback:
        messagebox.showinfo("Suggestions", "\n".join(feedback))


def toggle_password():
    if entry.cget('show') == '*':
        entry.config(show='')
    else:
        entry.config(show='*')


def clear():
    entry.delete(0, tk.END)
    result_label.config(text="")


# GUI WINDOW
root = tk.Tk()
root.title("🔐 Password Strength Checker - Manoj")
root.geometry("400x300")   # 👈 IMPORTANT (ensures window visible)

# UI
tk.Label(root, text="Enter Password", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=check_strength, bg="blue", fg="white").pack(pady=10)

tk.Button(root, text="Show/Hide", command=toggle_password).pack()

tk.Button(root, text="Clear", command=clear, bg="red", fg="white").pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()