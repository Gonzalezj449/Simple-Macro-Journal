import tkinter as tk
from ChatWithStaff import ChatWithStaff  # Import the ChatWithStaff class
from ChatWithDoc import ChatWithDoc  # Import the ChatWithDoctor class

class DataEntryPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Label for the title
        title_label = tk.Label(self, text="Data Entry Page", font=("Arial", 20))
        title_label.pack(pady=20)

        # Button to go to the ChatWithStaff page
        chat_staff_button = tk.Button(self, text="Chat with Staff", command=self.go_to_staff_chat)
        chat_staff_button.pack(pady=10)

        # Button to go to the ChatWithDoctor page
        chat_doctor_button = tk.Button(self, text="Chat with Doctor", command=self.go_to_doctor_chat)
        chat_doctor_button.pack(pady=10)

        # Other widgets for data entry can be added here

    def go_to_staff_chat(self):
        # Navigate to the ChatWithStaff page
        self.controller.show_page("ChatWithStaff")

    def go_to_doctor_chat(self):
        # Navigate to the ChatWithDoctor page
        self.controller.show_page("ChatWithDoc")

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Your Application")
        self.geometry("600x400")
        self.pages = {}
        self.create_pages()
        self.show_page("DataEntryPage")

    def create_pages(self):
        self.pages["DataEntryPage"] = DataEntryPage(self, self)  # Pass self as the controller
        self.pages["ChatWithStaff"] = ChatWithStaff(self)  # Add ChatWithStaff page
        self.pages["ChatWithDoc"] = ChatWithDoc(self)  # Add ChatWithDoctor page

    def show_page(self, page_name):
        for page, frame in self.pages.items():
            if page == page_name:
                frame.pack(fill=tk.BOTH, expand=True)
            else:
                frame.pack_forget()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
