import tkinter as tk
from tkinter import messagebox, simpledialog
from ChatWithStaff import ChatWithStaff
import json


class CaloriePage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.calorie_goal = None
        self.pounds_to_lose_per_30_days = None
        self.pounds_to_gain_per_30_days = None
        self.maintain_weight = None
        self.meals = {
            'Breakfast': {
                'items': [],
                'frame': None
            },
            'Lunch': {
                'items': [],
                'frame': None
            },
            'Dinner': {
                'items': [],
                'frame': None
            },
            'Snacks': {
                'items': [],
                'frame': None
            }
        }
        self.available_food = self.load_food_data()
        self.create_widgets()

    def load_food_data(self):
        with open('food_data.json', 'r') as file:
            food_data = json.load(file)
        return list(food_data.keys())  # Assume the keys are food names

    def create_widgets(self):
        # Logout button
        logout_button = tk.Button(self, text="Logout", command=self.logout)
        logout_button.grid(row=0, column=1, sticky="ne", padx=10, pady=10)
        # Button for Chat with Staff
        chat_button = tk.Button(self, text="Chat with Staff", command=self.go_to_chat)
        chat_button.grid(row=7, column=1, columnspan=2, pady=10, padx=(10,0))
        # Button for Chat with doc 
        chat_button = tk.Button(self, text="ChatWithDoc", command=self.go_to_chatwithdoc)
        chat_button.grid(row=7, column=2, columnspan=2, pady=10, padx=(10,0))
        # Button to navigate to FAQ page
        faq_button = tk.Button(self, text="FAQ", command=self.go_to_faq)
        faq_button.grid(row=8, column=1, columnspan=2, pady=10, padx=(10, 0))


        # Label to display calorie goal
        self.goal_label = tk.Label(self,
                                   text=f"Calorie Goal: {self.calorie_goal}",
                                   font=("Arial", 16))
        self.goal_label.grid(row=0,
                             column=0,
                             columnspan=2,
                             sticky="w",
                             padx=10,
                             pady=10)
        

        
        self.pounds_to_lose_label = tk.Label(self,
                                          text=f"Predicted Pounds to Lose per 30 days: {self.pounds_to_lose_per_30_days}",
                                          font=("Arial", 16))
        self.pounds_to_lose_label.grid(row=1,
                                   column=0,
                                   columnspan=2,
                                   sticky="w",
                                   padx=10,
                                   pady=10)
        self.pounds_to_Gain_label = tk.Label(self,
                                     text=f"Predicted Pounds to Gain per 30 days: {self.pounds_to_gain_per_30_days}",
                                     font=("Arial", 16))
        self.pounds_to_Gain_label.grid(row=1,
                                        column=0,
                                        columnspan=2,
                                        sticky="w",
                                        padx=10,
                                        pady=10)
        self.maintain_weight_label = tk.Label(self,
                                     text=f"Maintaining Weight: {self.maintain_weight}",
                                        font=("Arial", 16))
        self.maintain_weight_label.grid(row=1,
                                        column=0,
                                        columnspan=2,
                                        sticky="w",
                                        padx=10,
                                        pady=10)


        # Frame for displaying meal sections
        self.meal_sections_frame = tk.Frame(self)
        self.meal_sections_frame.grid(row=3,
                                      column=0,
                                      columnspan=2,
                                      padx=10,
                                      pady=10)

        # Add meal sections
        for i, meal_category in enumerate(self.meals.keys()):
            self.add_meal_section(meal_category, row=i + 2)

        # Label to display total calories, proteins, fats, and carbs
        self.total_calories_label = tk.Label(self, text="", font=("Arial", 16))
        self.total_calories_label.grid(row=len(self.meals) + 2,
                                        column=0,
                                        columnspan=2,
                                        pady=10)

        # Button to save progress
        save_button = tk.Button(self, text="Save",
                                command=self.save)  # Change here
        save_button.grid(row=len(self.meals) + 3, column=0, columnspan=2, pady=10)

        # Update the total label initially
        self.update_total_calories_label()
    #go to next section
    def go_to_chat(self):
        # Navigate to the ChatWithStaff page
        self.controller.show_page("ChatWithStaff")
    def go_to_chatwithdoc(self):
        # Navigate to the chatwithdoc page
        self.controller.show_page("ChatWithDoc")
    def go_to_faq(self):
        # Navigate to the FAQPage
        self.controller.show_page("FAQPage")

    def add_meal_section(self, meal_category, row):
        section_frame = tk.Frame(self.meal_sections_frame)
        section_frame.grid(row=row, column=0, columnspan=2, padx=10, pady=(0, 10))

        # Label for meal category
        category_label = tk.Label(section_frame,
                                  text=meal_category,
                                  font=("Arial", 14, "bold"))
        category_label.grid(row=0, column=0, pady=(0, 5), sticky="w")

        # Dropdown for selecting food
        food_selection = tk.StringVar()
        food_selection.set("Select Food")
        food_dropdown = tk.OptionMenu(section_frame, food_selection,
                                      *self.available_food)
        food_dropdown.grid(row=0, column=1, pady=(0, 5), sticky="e")

        # Entry for entering servings
        servings_entry = tk.Entry(section_frame, width=5)  # Adjust width here
        servings_entry.insert(0, "1")  # Default servings
        servings_entry.grid(row=0, column=2, pady=(0, 5), padx=(10, 0))

        # Label for servings
        servings_label = tk.Label(section_frame, text="servings")
        servings_label.grid(row=0, column=3, pady=(0, 5), padx=(5, 0), sticky="w")

        # Button to add food
        add_food_button = tk.Button(
            section_frame,
            text="+ Add Food",
            command=lambda category=meal_category, food_selection=
            food_selection, servings_entry=servings_entry: self.add_food(
                category, food_selection, servings_entry))
        add_food_button.grid(row=0,
                             column=4,
                             pady=(0, 5),
                             padx=(10, 0),
                             sticky="w")

        # Frame to display added food
        meal_frame = tk.Frame(section_frame)
        meal_frame.grid(row=1,
                        column=0,
                        columnspan=5,
                        padx=10,
                        pady=(0, 5),
                        sticky="w")

        # Save the meal frame for later use
        self.meals[meal_category]['frame'] = meal_frame

    def set_calorie_goal(self, calorie_goal, pounds_to_lose_per_30_days, pounds_to_gain_per_30_days, maintain_weight):
        self.calorie_goal = int(calorie_goal)
        self.pounds_to_lose_per_30_days = pounds_to_lose_per_30_days 
        self.pounds_to_gain_per_30_days = pounds_to_gain_per_30_days 

        # Configure calorie goal label
        self.goal_label.config(text=f"Calorie Goal: {self.calorie_goal}")


        
        if pounds_to_lose_per_30_days:
            self.maintain_weight_label.config(text="")
            self.pounds_to_lose_label.config(text=f"Predicted Pounds to Lose per 30 days: {self.pounds_to_lose_per_30_days}")
            self.pounds_to_Gain_label.config(text="")
        elif pounds_to_gain_per_30_days:
            self.maintain_weight_label.config(text="")
            self.pounds_to_lose_label.config(text="")
            self.pounds_to_Gain_label.config(text=f"Predicted Pounds to Gain per 30 days: {self.pounds_to_gain_per_30_days}")
        elif maintain_weight:
            self.maintain_weight_label.config(text="Maintaining Weight")
            self.pounds_to_Gain_label.config(text="")
            self.pounds_to_lose_label.config(text="")
        else:
            self.maintain_weight_label.config(text="")
            self.pounds_to_lose_label.config(text="")
            self.pounds_to_Gain_label.config(text="")
            

    def add_food(self, meal_category, food_selection, servings_entry):
        food_name = food_selection.get()
        if food_name == "Select Food":
            tk.messagebox.showerror("Error", "Please select a food item.")
            return

        servings = int(servings_entry.get())
        if servings <= 0:
            tk.messagebox.showerror("Error", "Please enter a valid servings.")
            return

        with open('food_data.json', 'r') as file:
            food_data = json.load(file)

        food_info = food_data.get(food_name)
        if food_info is None:
            tk.messagebox.showerror("Error",
                                    "Information not found for selected food item.")
            return

        calories = food_info.get('calories')
        proteins = food_info.get('proteins')
        fats = food_info.get('fats')
        carbs = food_info.get('carbs')

        if calories is None or proteins is None or fats is None or carbs is None:
            tk.messagebox.showerror(
                "Error",
                "Nutritional information incomplete for selected food item.")
            return

        total_calories = calories * servings
        total_proteins = proteins * servings
        total_fats = fats * servings
        total_carbs = carbs * servings

        self.meals[meal_category]['items'].append({
            'name': food_name,
            'calories': total_calories,
            'servings': servings,
            'proteins': total_proteins,
            'fats': total_fats,
            'carbs': total_carbs
        })
        self.update_total_calories_label()  # Update total calories count
        self.update_meals_display()  # Update the display of added meals
        # Reset food selection dropdown back to "select food"
        food_selection.set("Select Food")
        # Reset servings entry back to default
        servings_entry.delete(0, tk.END)
        servings_entry.insert(0, "1")

    def update_meals_display(self):
        for meal_category, meal_data in self.meals.items():
            meal_frame = meal_data['frame']
            # Clear previous meals
            for widget in meal_frame.winfo_children():
                widget.destroy()

            # Display added meals with delete buttons
            for index, meal in enumerate(meal_data['items']):
                meal_text = f"{meal['name']} - Calories: {meal['calories']} - Servings: {meal['servings']} - Proteins: {meal['proteins']}g - Fats: {meal['fats']}g - Carbs: {meal['carbs']}g"
                meal_label = tk.Label(meal_frame, text=meal_text)
                meal_label.grid(row=index, column=0, sticky="w", padx=30)

                # Delete button for each meal
                delete_button = tk.Button(
                    meal_frame,
                    text="Delete",
                    command=lambda meal_category=meal_category, index=index: self.
                    delete_meal(meal_category, index))
                delete_button.grid(row=index, column=1)

    def delete_meal(self, meal_category, index):
        # Remove the selected meal from the meals list
        del self.meals[meal_category]['items'][index]
        # Update the display after deletion
        self.update_total_calories_label()
        self.update_meals_display()

    def update_total_calories_label(self):
        total_calories = 0
        total_proteins = 0
        total_fats = 0
        total_carbs = 0

        for meal_data in self.meals.values():
            for meal in meal_data['items']:
                total_calories += meal['calories']
                total_proteins += meal['proteins']
                total_fats += meal['fats']
                total_carbs += meal['carbs']

        self.total_calories_label.config(
            text=
            f"Total Calories: {total_calories} | Total Proteins: {total_proteins}g | Total Fats: {total_fats}g | Total Carbs: {total_carbs}g"
        )

    def save(self):
        total_calories = sum(meal['calories'] for meal_data in self.meals.values()
                             for meal in meal_data['items'])
        if total_calories < 1200:
            message = "Based on the food you ate today, you are not eating enough for safe weight loss. The National Institute of Health recommends no less than 1200 Calories. Your information is saved for today."
            color = "red"
        elif total_calories > self.calorie_goal:
            message = "Remember, to lose weight you need to eat exactly or under your goal, but it's okay, just keep trying and don't give up! Your information is saved for today."
            color = "black"
        else:
            message = "Congrats on keeping on track! Your information is saved for today."
            color = "black"

        messagebox.showinfo("Result", message)

    def logout(self):
        # Perform logout actions
        print("Logout")
        self.controller.show_page("LoginPage")
    def show_page(self, page_name):
        for page, frame in self.pages.items():
            if page == page_name:
                frame.pack(fill=tk.BOTH, expand=True)
            else:
                frame.pack_forget()



# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    root.state('zoomed')  # Maximize the window
    calorie_page = CaloriePage(root, None)
    calorie_page.pack(fill=tk.BOTH,
                       expand=True)  # Fill and expand the entire window
    root.mainloop()