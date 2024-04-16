# Main Application Example
import tkinter as tk
from Page1 import LoginPage
from Page2 import CreateAccountPage
from StaffPage import StaffLoginPage
from Page3 import Page3 
from StaffDashB import StaffDashB

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Application Title")
        self.setup_pages()

    def setup_pages(self):
        self.pages = {
            "LoginPage": LoginPage(parent=self, controller=self),
            "CreateAccountPage": CreateAccountPage(parent=self, controller=self),
            "StaffLoginPage": StaffLoginPage(parent=self, controller=self),
            "Page3": Page3(parent=self, controller=self),
            "StaffDashB": StaffDashB(parent=self, controller=self)
        }
        for page in self.pages.values():
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page("LoginPage")

    def show_page(self, page_name):
        self.pages[page_name].tkraise()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()




