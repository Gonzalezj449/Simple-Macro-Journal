import tkinter as tk
from ChatWithUserForDoc import ChatWithUserForDoc  # Import the ChatWithUserForDoc class

class DocDashB(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Label for the title
        title_label = tk.Label(self, text="Doctor Dashboard", font=("Arial", 20))
        title_label.pack(pady=20)

        # Button to go to the ChatWithUserForDoc page
        chat_button = tk.Button(self, text="Chat with User", command=self.go_to_chat)
        chat_button.pack(pady=10)

        logout_button = tk.Button(
            self,
            text="Logout",
            command=lambda: self.controller.show_page("LoginPage"),
            font=("Arial", 10),
            width=10)
        logout_button.pack(pady=10) #FIXED Logout button
        
    def go_to_chat(self):
        # Navigate to the ChatWithUserForDoc page
        self.controller.show_page("ChatWithUserForDoc")

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Your Application")
        self.geometry("600x400")
        self.pages = {}
        self.create_pages()
        self.show_page("DocDashB")

    def create_pages(self):
        self.pages["DocDashB"] = DocDashB(self, self)  # Pass self as the controller
        self.pages["ChatWithUserForDoc"] = ChatWithUserForDoc(self)  # Add ChatWithUserForDoc page

    def show_page(self, page_name):
        for page, frame in self.pages.items():
            if page == page_name:
                frame.pack(fill=tk.BOTH, expand=True)
            else:
                frame.pack_forget()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
