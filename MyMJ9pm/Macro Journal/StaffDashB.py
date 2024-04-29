import tkinter as tk
import json
from ChatWithUser import ChatWithUser  # Import the ChatWithUser class

class StaffDashB(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.food_items = {}  # Dictionary to store food items
        self.load_food_data()  # Load saved food data
        self.create_widgets()

    def create_widgets(self):
        # Dashboard label
        dashboard_label = tk.Label(
            self,
            text="Staff Dashboard",
            font=("Arial", 20)
        )
        dashboard_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Food details labels and entry fields
        self.name_label = tk.Label(self, text="Food Name:")
        self.name_label.grid(row=1, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.calorie_label = tk.Label(self, text="Total Calories:")
        self.calorie_label.grid(row=2, column=0, padx=10, pady=5)
        self.calorie_entry = tk.Entry(self)
        self.calorie_entry.grid(row=2, column=1, padx=10, pady=5)

        self.proteins_label = tk.Label(self, text="Total proteins:")
        self.proteins_label.grid(row=3, column=0, padx=10, pady=5)
        self.proteins_entry = tk.Entry(self)
        self.proteins_entry.grid(row=3, column=1, padx=10, pady=5)

        self.fats_label = tk.Label(self, text="Total Fats:")
        self.fats_label.grid(row=4, column=0, padx=10, pady=5)
        self.fats_entry = tk.Entry(self)
        self.fats_entry.grid(row=4, column=1, padx=10, pady=5)

        self.carbs_label = tk.Label(self, text="Total Carbs:")
        self.carbs_label.grid(row=5, column=0, padx=10, pady=5)
        self.carbs_entry = tk.Entry(self)
        self.carbs_entry.grid(row=5, column=1, padx=10, pady=5)

        # Message label for displaying feedback
        self.message_label = tk.Label(self, text="", fg="green")
        self.message_label.grid(row=6, column=0, columnspan=2, pady=5)

        # Buttons for food management with equal width
        button_width = 15
        self.add_button = tk.Button(self, text="Add Food", command=self.add_food, width=button_width)
        self.add_button.grid(row=7, column=0, columnspan=2, pady=5)

        self.remove_button = tk.Button(self, text="Remove Food", command=self.remove_food, width=button_width)
        self.remove_button.grid(row=8, column=0, columnspan=2, pady=5)

        self.edit_button = tk.Button(self, text="Edit Food", command=self.edit_food, width=button_width)
        self.edit_button.grid(row=9, column=0, columnspan=2, pady=5)

        self.clear_button = tk.Button(self, text="Clear List", command=self.clear_list, width=button_width)
        self.clear_button.grid(row=10, column=0, columnspan=2, pady=5)

        # Listbox to display added food items
        self.food_listbox = tk.Listbox(self, width=70, height=10)
        self.food_listbox.grid(row=11, column=0, columnspan=2, padx=10, pady=5)

        # Button to send food list to customer
        self.send_button = tk.Button(self, text="Save Food List", command=self.send_food_list, width=button_width)
        self.send_button.grid(row=12, column=0, columnspan=2, pady=10)

        # Button to go to the ChatWithUser page
        self.chat_button = tk.Button(self, text="Chat with User", command=self.go_to_chat, width=button_width)
        self.chat_button.grid(row=13, column=0, columnspan=2, pady=10)

        logout_button = tk.Button(
            self,
            text="Logout",
            command=lambda: self.controller.show_page("LoginPage"),
            font=("Arial", 10),
            width=button_width)
        logout_button.grid(row=16, column=0, columnspan=2, pady=10)

        # Update food listbox initially
        self.update_food_listbox()

    def add_food(self):
        # Retrieve food name, calories, proteins, total fats, and total carbs from entry fields
        food_name = self.name_entry.get()
        food_calories = self.calorie_entry.get()
        proteins = self.proteins_entry.get()
        fats = self.fats_entry.get()
        carbs = self.carbs_entry.get()

        # Validate input
        if food_name and food_calories and proteins and fats and carbs:
            try:
                # Convert calories, proteins, fats, and carbs to float
                food_calories = float(food_calories)
                proteins = float(proteins)
                fats = float(fats)
                carbs = float(carbs)

                # Check if the food item already exists
                if food_name in self.food_items:
                    self.message_label.config(text="Food already added", fg="red")
                    return

                # Add food item and its details to the dictionary
                self.food_items[food_name] = {
                    "calories": food_calories,
                    "proteins": proteins,  # Ensure 'proteins' key is included
                    "fats": fats,
                    "carbs": carbs
                }

                # Update food listbox
                self.update_food_listbox()

                # Clear the entry fields
                self.name_entry.delete(0, tk.END)
                self.calorie_entry.delete(0, tk.END)
                self.proteins_entry.delete(0, tk.END)
                self.fats_entry.delete(0, tk.END)
                self.carbs_entry.delete(0, tk.END)

                # Save food data
                self.save_food_data()

                # Display success message
                self.message_label.config(text="Food added successfully", fg="green")
            except ValueError:
                # Display error message if any field is not a valid number
                self.message_label.config(text="Invalid input", fg="red")
        else:
            # Display error message if any field is empty
            self.message_label.config(text="Please fill in all fields", fg="red")

    def remove_food(self):
        # Retrieve selected food item from listbox
        selected_index = self.food_listbox.curselection()
        if selected_index:
            selected_food = self.food_listbox.get(selected_index)
            # Remove selected food item from the dictionary
            food_name = selected_food.split(" - ")[0]
            del self.food_items[food_name]

            # Update food listbox
            self.update_food_listbox()

            # Save food data
            self.save_food_data()

            # Display success message
            self.message_label.config(text="Food removed successfully", fg="green")

    def edit_food(self):
        # Retrieve selected food item from listbox
        selected_index = self.food_listbox.curselection()
        if selected_index:
            selected_food = self.food_listbox.get(selected_index)
            # Populate entry fields with selected food item details
            food_name, food_details = selected_food.split(" - ")
            food_calories = self.food_items[food_name]["calories"]
            proteins = self.food_items[food_name]["proteins"]
            fats = self.food_items[food_name]["fats"]
            carbs = self.food_items[food_name]["carbs"]
            self.name_entry.delete(0, tk.END)
            self.calorie_entry.delete(0, tk.END)
            self.proteins_entry.delete(0, tk.END)
            self.fats_entry.delete(0, tk.END)
            self.carbs_entry.delete(0, tk.END)
            self.name_entry.insert(0, food_name)
            self.calorie_entry.insert(0, food_calories)
            self.proteins_entry.insert(0, proteins)
            self.fats_entry.insert(0, fats)
            self.carbs_entry.insert(0, carbs)

            # Change button function to 'Save Changes'
            self.add_button.config(text="Save Changes", command=lambda: self.update_food(selected_food))

    def update_food(self, selected_food):
        # Retrieve updated food name, calories, proteins, total fats, and total carbs
        food_name = self.name_entry.get()
        food_calories = self.calorie_entry.get()
        proteins = self.proteins_entry.get()
        fats = self.fats_entry.get()
        carbs = self.carbs_entry.get()

        # Validate input
        if food_name and food_calories and proteins and fats and carbs:
            try:
                # Convert calories, proteins, fats, and carbs to float
                food_calories = float(food_calories)
                proteins = float(proteins)
                fats = float(fats)
                carbs = float(carbs)

                # Remove selected food item from the dictionary
                del self.food_items[selected_food.split(" - ")[0]]

                # Add updated food item and its details to the dictionary
                self.food_items[food_name] = {
                    "calories": food_calories,
                    "proteins": proteins,
                    "fats": fats,
                    "carbs": carbs
                }

                # Update food listbox
                self.update_food_listbox()

                # Clear the entry fields
                self.name_entry.delete(0, tk.END)
                self.calorie_entry.delete(0, tk.END)
                self.proteins_entry.delete(0, tk.END)
                self.fats_entry.delete(0, tk.END)
                self.carbs_entry.delete(0, tk.END)

                # Change button function back to 'Add Food'
                self.add_button.config(text="Add Food", command=self.add_food)

                # Save food data
                self.save_food_data()

                # Display success message
                self.message_label.config(text="Food updated successfully", fg="green")
            except ValueError:
                # Display error message if any field is not a valid number
                self.message_label.config(text="Invalid input", fg="red")
        else:
            # Display error message if any field is empty
            self.message_label.config(text="Please fill in all fields", fg="red")

    def update_food_listbox(self):
        # Clear existing items
        self.food_listbox.delete(0, tk.END)

        # Add updated food items with details to the listbox
        for food_name, food_details in self.food_items.items():
            self.food_listbox.insert(tk.END, f"{food_name} - "
                                               f"Total Calories: {food_details['calories']}, "
                                               f"Total proteins: {food_details['proteins']}, "
                                               f"Total Fats: {food_details['fats']}, "
                                               f"Total Carbs: {food_details['carbs']}")

    def save_food_data(self):
        # Save food data to a JSON file
        with open("food_data.json", "w") as f:
            json.dump(self.food_items, f)

    def load_food_data(self):
        try:
            # Load saved food data from JSON file
            with open("food_data.json", "r") as f:
                self.food_items = json.load(f)
        except FileNotFoundError:
            # If the file doesn't exist, initialize with empty data
            self.food_items = {}

    def send_food_list(self):
        # Send food list to customer
        print("Food List Sent:", self.food_items)

    def clear_list(self):
        # Clear the food listbox and the stored food data
        self.food_listbox.delete(0, tk.END)
        self.food_items = {}
        self.save_food_data()
        # Display success message
        self.message_label.config(text="Food list cleared successfully", fg="green")

    def go_to_chat(self):
        # Navigate to the ChatWithUser page
        chat_page = self.controller.pages.get("ChatWithUser")
        if chat_page:
            # Pass any necessary information to the ChatWithUser page
            chat_page.load_messages()  # Load previous messages if any
            self.controller.show_page("ChatWithUser")

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Staff Dashboard")
        self.geometry("400x600")
        self.pages = {}
        self.create_pages()
        self.show_page("StaffDashB")

    def create_pages(self):
        self.pages["StaffDashB"] = StaffDashB(self, self)
        self.pages["ChatWithUser"] = ChatWithUser(self)

    def show_page(self, page_name):
        for page, frame in self.pages.items():
            if page == page_name:
                frame.pack(fill=tk.BOTH, expand=True)
            else:
                frame.pack_forget()


