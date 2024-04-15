import tkinter as tk

def login():
    # Implement login functionality here
    print("Login")

def create_account():
    # Implement create account functionality here
    print("Create Account")

# Font and size 
custom_font = ("Arial", 16)

# Log in window 
root = tk.Tk()
width = 300
height = 200

# Set width and height 
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
 
x_position = 0 
y_position = 0

root.geometry(f"{width}x{height}+{x_position}+{y_position}")

root.title("Welcome Page")
root.minsize(width=500, height=800)
root.maxsize(width=500, height=800)

welcome_label = tk.Label(root, text="Welcome!", font=custom_font)
welcome_label.pack(pady=8)

instruction_label = tk.Label(root, text="Please sign in or create an account to continue.", font=custom_font)
instruction_label.pack(pady=6)

# Frame for username and password entry
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

# Username entry
username_label = tk.Label(entry_frame, text="Username:", font=custom_font)
username_label.grid(row=0, column=0, padx=5)

username_entry = tk.Entry(entry_frame, font=custom_font)
username_entry.grid(row=0, column=1, padx=5)

# Password entry
password_label = tk.Label(entry_frame, text="Password:", font=custom_font)
password_label.grid(row=1, column=0, padx=5)

password_entry = tk.Entry(entry_frame, show="*", font=custom_font)
password_entry.grid(row=1, column=1, padx=5)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Log in button
login_button = tk.Button(button_frame, text="Log In", command=login, font=custom_font)
login_button.grid(row=0, column=0, padx=5)

# Create account button
create_account_button = tk.Button(button_frame, text="Create Account", command=create_account, font=custom_font)
create_account_button.grid(row=0, column=1, padx=5)

root.mainloop()
