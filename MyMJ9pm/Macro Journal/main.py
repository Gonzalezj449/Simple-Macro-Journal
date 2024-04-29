import tkinter as tk
from LoginPage import LoginPage
from CreateAccountPage import CreateAccountPage
from StaffLoginPage import StaffLoginPage
from CalculateCaloriegoal import CalculateCaloriegoal
from StaffDashB import StaffDashB
from CaloriePage import CaloriePage
from ChatWithStaff import ChatWithStaff
from ChatWithUser import ChatWithUser
from FAQPage import FAQPage
from DoctorLogin  import DoctorLogin
from DocDashB import DocDashB
from ChatWithDoc import ChatWithDoc
from ChatWithUserForDoc import ChatWithUserForDoc

class MainApplication(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("My Macro Journal")
        self.setup_pages()

    def setup_pages(self):
        self.pages = {
            "LoginPage": LoginPage(parent=self, controller=self),
            "CreateAccountPage": CreateAccountPage(parent=self, controller=self),
            "StaffLoginPage": StaffLoginPage(parent=self, controller=self),
            "CalculateCaloriegoal": CalculateCaloriegoal(parent=self, controller=self),
            "StaffDashB": StaffDashB(parent=self, controller=self),
            "CaloriePage": CaloriePage(parent=self, controller=self),
            "ChatWithStaff": ChatWithStaff(parent=self),
            "FAQPage": FAQPage(parent=self, controller=self),    
            "ChatWithUser": ChatWithUser(parent=self),
            "DoctorLogin": DoctorLogin(parent=self, controller=self),
            "DocDashB": DocDashB(parent=self, controller=self), 
            "ChatWithDoc": ChatWithDoc(parent=self),
            "ChatWithUserForDoc": ChatWithUserForDoc(parent=self)

        }
        for page in self.pages.values():
            if page:
                page.grid(row=0, column=0, sticky="nsew")

        self.show_page("LoginPage")

    def show_page(self, page_name):
        if page_name in self.pages:
            page = self.pages[page_name]
            page.tkraise()
        else:
            raise ValueError("Invalid page name")

    def show_calorie_page(self, calories,pounds_to_lose_per_30_days, pounds_to_gain_per_30_days, maintain_weight):
        if "CaloriePage" in self.pages:
            page = self.pages["CaloriePage"]
            page.set_calorie_goal(calories,pounds_to_lose_per_30_days, pounds_to_gain_per_30_days, maintain_weight)
            self.show_page("CaloriePage")
            # Maximize the window
            self.state('zoomed')
        else:
            raise ValueError("CaloriePage not found in pages")


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
