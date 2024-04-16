# Page3.py
import tkinter as tk

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        welcome_label = tk.Label(self, text="Welcome to your dashboard!", font=("Arial", 20))
        welcome_label.pack(pady=20)

        logout_button = tk.Button(self, text="Logout", command=lambda: self.controller.show_page("LoginPage"), font=("Arial", 16))
        logout_button.pack(pady=10)
