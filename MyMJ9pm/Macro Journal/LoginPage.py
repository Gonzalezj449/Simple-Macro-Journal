# Page1.py
import tkinter as tk
import json

# It's assumed that Page2.py and StaffPage.py are in the same directory and are structured appropriately.
from CreateAccountPage import CreateAccountPage
from StaffLoginPage import StaffLoginPage


class LoginPage(tk.Frame):

  def __init__(self, parent, controller):
    super().__init__(parent)
    self.controller = controller
    self.create_widgets()

  def create_widgets(self):
    username_label = tk.Label(self, text="Username:", font=("Arial", 16))
    username_label.grid(row=0, column=0, padx=10, pady=10)
    self.username_entry = tk.Entry(self, font=("Arial", 16))
    self.username_entry.grid(row=0, column=1, padx=10, pady=10)

    password_label = tk.Label(self, text="Password:", font=("Arial", 16))
    password_label.grid(row=1, column=0, padx=10, pady=10)
    self.password_entry = tk.Entry(self, show="*", font=("Arial", 16))
    self.password_entry.grid(row=1, column=1, padx=10, pady=10)

    login_button = tk.Button(self,
                             text="Log In",
                             command=self.login,
                             font=("Arial", 16))
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    self.login_message_label = tk.Label(self, text="", font=("Arial", 16))
    self.login_message_label.grid(row=3, column=0, columnspan=2)

    # Navigation buttons
    nav_frame = tk.Frame(self)
    nav_frame.grid(row=4, column=0, columnspan=2, pady=10)
    create_account_button = tk.Button(
        nav_frame,
        text="Create Account",
        command=lambda: self.controller.show_page("CreateAccountPage"),
        font=("Arial", 16))
    create_account_button.pack(side=tk.LEFT, padx=10)
    staff_login_button = tk.Button(
        nav_frame,
        text="Staff Login",
        command=lambda: self.controller.show_page("StaffLoginPage"),
        font=("Arial", 16))
    staff_login_button.pack(side=tk.LEFT, padx=10)
    self.doctor_login_button = tk.Button(self, text="Healthcare Login", command=lambda: self.controller.show_page("DoctorLogin"), font=("Arial", 14))
    self.doctor_login_button.grid(row=5, column=1, padx=10)


  def login(self):
    username = self.username_entry.get()
    password = self.password_entry.get()
    try:
      with open("accounts.json", "r") as f:
        accounts = json.load(f)
      if username in accounts and accounts[username] == password:
        self.login_message_label.config(text="Login successful")
        self.controller.show_page("CalculateCaloriegoal")
      else:
        self.login_message_label.config(text="Incorrect username or password")
    except FileNotFoundError:
      self.login_message_label.config(text="Login data not found")


































