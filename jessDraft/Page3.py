#page3
import tkinter as tk

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        welcome_label = tk.Label(self, text="Welcome to your dashboard!", font=("Arial", 20))
        welcome_label.pack(pady=20)

        # Input fields
        weight_label = tk.Label(self, text="Weight (kg):")
        weight_label.pack()
        self.weight_entry = tk.Entry(self)
        self.weight_entry.pack()

        height_label = tk.Label(self, text="Height (cm):")
        height_label.pack()
        self.height_entry = tk.Entry(self)
        self.height_entry.pack()

        age_label = tk.Label(self, text="Age:")
        age_label.pack()
        self.age_entry = tk.Entry(self)
        self.age_entry.pack()

        # Activity Level selection
        activity_label = tk.Label(self, text="Activity Level:")
        activity_label.pack()
        self.activity_var = tk.StringVar(self)
        self.activity_var.set("Select Activity Level")  # Default option
        activity_options = ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extremely Active"]
        activity_menu = tk.OptionMenu(self, self.activity_var, *activity_options)
        activity_menu.pack()

        goal_label = tk.Label(self, text="Goal (lose/gain):")
        goal_label.pack()
        self.goal_entry = tk.Entry(self)
        self.goal_entry.pack()

        calculate_button = tk.Button(self, text="Calculate", command=self.calculate_calories, font=("Arial", 16))
        calculate_button.pack(pady=10)

        logout_button = tk.Button(self, text="Logout", command=lambda: self.controller.show_page("LoginPage"), font=("Arial", 16))
        logout_button.pack(pady=10)

    def calculate_calories(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            age = int(self.age_entry.get())
            activity_level = self.get_activity_level_factor()
            goal = self.goal_entry.get().lower()

            if goal not in ['lose', 'gain']:
                raise ValueError("Goal should be 'lose' or 'gain'.")

            # Calculate BMR (Basal Metabolic Rate)
            if goal == 'lose':
                bmr = 10 * weight + 6.25 * height - 5 * age - 161
            elif goal == 'gain':
                bmr = 10 * weight + 6.25 * height - 5 * age + 5

            # Adjust BMR based on activity level
            calories_needed = bmr * activity_level

            # Display result
            result_label = tk.Label(self, text=f"Calories needed per day: {calories_needed:.2f}", font=("Arial", 12))
            result_label.pack(pady=10)

        except ValueError as e:
            # Display error if input is invalid
            error_label = tk.Label(self, text=str(e), font=("Arial", 12), fg="red")
            error_label.pack(pady=10)

    def get_activity_level_factor(self):
        activity_level = self.activity_var.get()
        if activity_level == "Sedentary":
            return 1.2
        elif activity_level == "Lightly Active":
            return 1.375
        elif activity_level == "Moderately Active":
            return 1.55
        elif activity_level == "Very Active":
            return 1.725
        elif activity_level == "Extremely Active":
            return 1.9
        else:
            raise ValueError("Invalid activity level")

# Example usage
if __name__ == "__main__":
    app = tk.Tk()
    page = Page3(app, None)
    page.pack()
    app.mainloop()
