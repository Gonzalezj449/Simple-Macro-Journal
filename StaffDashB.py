# StaffDashB.py
import tkinter as tk

class StaffDashB(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        dashboard_label = tk.Label(self, text="Staff Dashboard", font=("Arial", 20))
        dashboard_label.pack(pady=20)

        logout_button = tk.Button(self, text="Logout", command=lambda: self.controller.show_page("LoginPage"), font=("Arial", 16))
        logout_button.pack(pady=10)

        # Additional widgets can be added here as needed
