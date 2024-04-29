import tkinter as tk

class FoodList(tk.Frame):
    def __init__(self, parent, controller, food_items):
        super().__init__(parent)
        self.controller = controller
        self.food_items = food_items  # Received food items from StaffDashB
        self.create_widgets()

    def create_widgets(self):
        # Title label
        title_label = tk.Label(
            self,
            text="Food List",
            font=("Arial", 20)
        )
        title_label.pack(pady=10)

        # Listbox to display received food items
        self.food_listbox = tk.Listbox(self, width=60, height=15)
        self.food_listbox.pack(pady=10)
        self.update_food_listbox()

        # Button to add selected item to user's list
        add_button = tk.Button(self, text="Add to My List", command=self.add_to_my_list)
        add_button.pack(pady=10)

        # Button to go back to Staff Dashboard
        back_button = tk.Button(self, text="Back to Dashboard", command=self.go_back)
        back_button.pack(pady=10)

    def update_food_listbox(self):
        # Clear existing items
        self.food_listbox.delete(0, tk.END)

        # Add received food items with details to the listbox
        for food_name, food_details in self.food_items.items():
            self.food_listbox.insert(tk.END, f"{food_name} - "
                                               f"Calories: {food_details['calories']}, "
                                               f"Protein: {food_details['protein']}, "
                                               f"Total Fats: {food_details['fats']}, "
                                               f"Total Carbs: {food_details['carbs']}")

    def add_to_my_list(self):
        # Get the selected item from the listbox
        selected_index = self.food_listbox.curselection()
        if selected_index:
            selected_food = self.food_listbox.get(selected_index)
            # Add selected food item to user's list (You can define your logic here)
            print("Added to My List:", selected_food)
        else:
            print("Please select a food item to add to your list.")

if __name__ == "__main__":
    app = tk.Tk()
    page = FoodList(app, None)
    page.pack()
    app.mainloop()