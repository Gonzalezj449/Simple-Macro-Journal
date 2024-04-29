import tkinter as tk
import json

def login():
    # Retrieve username and password from entry fields
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password match any account
    if username in accounts and accounts[username] == password:
        login_success_label.config(text="Login successful")
    else:
        login_success_label.config(text="Incorrect login")

def create_account():
    global account_creation_in_progress
    if not account_creation_in_progress:
        account_creation_in_progress = True
        # Retrieve username and password from entry fields
        username = username_entry.get()
        password = password_entry.get()
        
        # Check if username and password are not empty
        if username and password:
            # Check if username already exists
            if username in accounts:
                print("Username already exists. Please choose another one.")
            else:
                # Add new account to dictionary
                accounts[username] = password
                # Save accounts dictionary to file
                save_accounts()
                print("Account created successfully.")
                # Show success message
                account_created_label.config(text="Account created successfully.")
        else:
            print("Please enter both username and password.")
            account_creation_in_progress = False

def staff_login():
    global staff_login_success_label  # Make staff_login_success_label global
    
    # Retrieve username and password from entry fields
    username = staff_username_entry.get()
    password = staff_password_entry.get()

    # Pre-saved staff username and password
    staff_username = "admin"
    staff_password = "password"

    # Check if username and password match pre-saved staff credentials
    if username == staff_username and password == staff_password:
        staff_login_success_label.config(text="Staff login successful")
    else:
        staff_login_success_label.config(text="Incorrect staff username or password")

def save_accounts():
    with open("accounts.json", "w") as f:
        json.dump(accounts, f)

def create_account_window():
    global username_entry
    global password_entry
    # Create a new window for creating an account
    account_window = tk.Toplevel(root)
    account_window.title("Create Account")
    
    # Frame for username and password entry
    entry_frame = tk.Frame(account_window)
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

    # Create account button
    create_account_button = tk.Button(account_window, text="Create Account", command=create_account, font=custom_font)
    create_account_button.pack(pady=10)

    # Label to display account creation status
    global account_created_label
    account_created_label = tk.Label(account_window, text="", font=custom_font)
    account_created_label.pack()

def staff_login_window():
    global staff_username_entry
    global staff_password_entry
    global staff_login_success_label
    
    # Create a pop-up window for staff login
    staff_login_window = tk.Toplevel(root)
    staff_login_window.title("Staff Login")

    # Frame for staff username and password entry
    staff_login_frame = tk.Frame(staff_login_window)
    staff_login_frame.pack(pady=10)

    # Staff Username entry
    staff_username_label = tk.Label(staff_login_frame, text="Username:", font=custom_font)
    staff_username_label.grid(row=0, column=0, padx=5)

    staff_username_entry = tk.Entry(staff_login_frame, font=custom_font)
    staff_username_entry.grid(row=0, column=1, padx=5)

    # Staff Password entry
    staff_password_label = tk.Label(staff_login_frame, text="Password:", font=custom_font)
    staff_password_label.grid(row=1, column=0, padx=5)

    staff_password_entry = tk.Entry(staff_login_frame, show="*", font=custom_font)
    staff_password_entry.grid(row=1, column=1, padx=5)

    # Staff login button
    staff_login_button = tk.Button(staff_login_frame, text="Staff Sign In", command=staff_login, font=custom_font)
    staff_login_button.grid(row=2, columnspan=2, pady=10)

    # Label to display staff login status
    staff_login_success_label = tk.Label(staff_login_frame, text="", font=custom_font)
    staff_login_success_label.grid(row=3, columnspan=2)

# Load accounts from file
try:
    with open("accounts.json", "r") as f:
        accounts = json.load(f)
except FileNotFoundError:
    # If the file doesn't exist, create an empty dictionary
    accounts = {}

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
create_account_button = tk.Button(button_frame, text="Create Account", command=create_account_window, font=custom_font)
create_account_button.grid(row=0, column=1, padx=5)

# Staff login button
staff_login_button = tk.Button(button_frame, text="Staff sign in", command=staff_login_window, font=custom_font)
staff_login_button.grid(row=0, column=2, padx=5)

# Label to display login success
login_success_label = tk.Label(root, text="", font=custom_font)
login_success_label.pack()

# Flag to track if account creation is in progress
account_creation_in_progress = False

root.mainloop()