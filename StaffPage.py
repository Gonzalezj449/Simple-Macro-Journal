# StaffPage.py
import tkinter as tk

class StaffLoginPage(tk.Frame):
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

        login_button = tk.Button(self, text="Staff Log In", command=self.staff_login, font=("Arial", 16))
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.login_message_label = tk.Label(self, text="", font=("Arial", 16))
        self.login_message_label.grid(row=3, column=0, columnspan=2)

    def staff_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "password":
            self.login_message_label.config(text="Staff login successful")
            self.controller.show_page("StaffDashB")
        else:
            self.login_message_label.config(text="Incorrect staff username or password")
