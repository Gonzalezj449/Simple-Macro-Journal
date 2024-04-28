import tkinter as tk
import tkinter.messagebox as tkmsg
import json

class PersonalPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Assuming username is available as self.controller.username
        username = self.controller.username if self.controller and hasattr(self.controller, 'username') else "Unknown User"

        # Displaying the username at the top
        username_label = tk.Label(self, text=f"Username: {username}", font=("Arial", 20))
        username_label.pack(pady=(10, 20))

        dashboard_label = tk.Label(self, text="Change Password?", font=("Arial", 20))
        dashboard_label.pack(pady=20)

        # Old password entry
        old_password_label = tk.Label(self, text="Enter old password:")
        old_password_label.pack(pady=(5, 0))
        self.old_password_entry = tk.Entry(self, show="*")
        self.old_password_entry.pack(pady=(0, 5))

        # New password entry
        new_password_label = tk.Label(self, text="Enter new password:")
        new_password_label.pack(pady=(5, 0))
        self.new_password_entry = tk.Entry(self, show="*")
        self.new_password_entry.pack(pady=(0, 5))

        # Confirm new password entry
        confirm_password_label = tk.Label(self, text="Confirm new password:")
        confirm_password_label.pack(pady=(5, 0))
        self.confirm_password_entry = tk.Entry(self, show="*")
        self.confirm_password_entry.pack(pady=(0, 10))

        # Button to change password
        change_password_button = tk.Button(self, text="Change Password", command=self.change_password)
        change_password_button.pack(pady=10)

        # Button to navigate to another page
        navigate_button = tk.Button(self, text="Go Back")#, command=lambda: self.controller.show_page("OtherPage"))
        navigate_button.pack(pady=10)

    def change_password(self):
        old_password = self.old_password_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if new_password != confirm_password:
            tkmsg.showerror("Error", "New passwords do not match.")
            return

        if self.update_password_in_file(old_password, new_password):
            tkmsg.showinfo("Success", "Password successfully updated.")
        else:
            tkmsg.showerror("Error", "Old password is incorrect.")

    def update_password_in_file(self, old_password, new_password):
        filename = "accounts.json"
        try:
            with open(filename, 'r+') as file:
                accounts = json.load(file)
                username = self.controller.username if self.controller and hasattr(self.controller, 'username') else None
                if accounts.get(username) != old_password:
                    return False
                accounts[username] = new_password
                file.seek(0)
                json.dump(accounts, file, indent=4)
                file.truncate()
            return True
        except Exception as e:
            tkmsg.showerror("Error", f"An unexpected error occurred: {str(e)}")
            return False

if __name__ == "__main__":
    app = tk.Tk()
    app.controller = type('MockController', (object,), {'username': 'pee'})()  # Mock-up for testing
    page = PersonalPage(app, app.controller)
    page.pack()
    app.mainloop()