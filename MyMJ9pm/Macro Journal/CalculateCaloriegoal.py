import tkinter as tk


class CalculateCaloriegoal(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Label for welcome message
        welcome_label = tk.Label(self,
                                 text="Enter your info to calculate your goal",
                                 font=("Arial", 20))
        welcome_label.pack(pady=20)

        # Input fields
        weight_label = tk.Label(self, text="Weight (lbs):")
        weight_label.pack()
        self.weight_entry = tk.Entry(self)
        self.weight_entry.pack()

        height_label = tk.Label(self, text="Height (in):")
        height_label.pack()
        self.height_entry = tk.Entry(self)
        self.height_entry.pack()

        age_label = tk.Label(self, text="Age:")
        age_label.pack()
        self.age_entry = tk.Entry(self)
        self.age_entry.pack()

        # Gender selection
        gender_label = tk.Label(self, text="Gender:")
        gender_label.pack()
        self.gender_var = tk.StringVar(self)
        self.gender_var.set("Male")  # Default option
        gender_options = ["Male", "Female"]
        for option in gender_options:
            gender_radio = tk.Radiobutton(self,
                                          text=option,
                                          variable=self.gender_var,
                                          value=option)
            gender_radio.pack()

        # Activity Level selection
        activity_label_text = "Activity Level:"
        activity_label = tk.Label(self,
                                  text=activity_label_text,
                                  font=("Arial", 12, "underline"))
        activity_label.pack()
        self.activity_var = tk.StringVar(self)
        self.activity_var.set("Select Activity Level")  # Default option
        activity_options = [
            "Lightly Active", "Moderately Active", "Very Active",
            "Extremely Active"
        ]
        for option in activity_options:
            activity_radio = tk.Radiobutton(self,
                                            text=option,
                                            variable=self.activity_var,
                                            value=option)
            activity_radio.pack()

        # Goal selection
        goal_label_text = "Goal:"
        goal_label = tk.Label(self,
                              text=goal_label_text,
                              font=("Arial", 12, "underline"))
        goal_label.pack()

        self.goal_var = tk.StringVar()
        self.goal_var.set("Maintain")  # Default option

        goals = [("Maintain", "Maintain"), ("Lose", "Lose"), ("Gain", "Gain")]
        for text, goal in goals:
            goal_radio = tk.Radiobutton(self,
                                        text=text,
                                        variable=self.goal_var,
                                        value=goal)
            goal_radio.pack()

        # Button for calculation
        calculate_button = tk.Button(self,
                                     text="Calculate",
                                     command=self.calculate_calories,
                                     font=("Arial", 16))
        calculate_button.pack(pady=10)

        # Button for logout
        logout_button = tk.Button(
            self,
            text="Logout",
            command=lambda: self.controller.show_page("LoginPage"),
            font=("Arial", 16))
        logout_button.pack(pady=10)

    def calculate_calories(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            age = int(self.age_entry.get())
            gender = self.gender_var.get()
            activity_level = self.get_activity_level_factor()
            goal = self.goal_var.get()
            
            # Validate inputs
            if weight <= 0 or height <= 0 or age <= 0:
                raise ValueError("Invalid input. Please enter valid values.")
            
            # Convert height from inches to meters
            height_meters = height * 0.0254
            # Convert weight from pounds to kilograms
            weight_kg = weight * 0.453592

            # Calculate BMR using Mifflin-St Jeor equation
           # Calculate BMR using Mifflin-St Jeor equation
            if gender == "Male":
                bmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
            elif gender == "Female":
                bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
            else:
                raise ValueError("Invalid gender")


            # Calculate TDEE (Total Daily Energy Expenditure) based on activity level
            tdee = bmr * activity_level

            # Adjust TDEE based on the deficit or surplus needed for weight loss or gain per day
            if goal == "Lose":
                adjusted_calorie_goal = tdee - 500  # 500 calories deficit per day for weight loss
                adjusted_calorie_goal = max(adjusted_calorie_goal, bmr)
            elif goal == "Gain":
                adjusted_calorie_goal = tdee + 300  # 300 calories surplus per day for weight gain
            else:
                adjusted_calorie_goal = tdee  # Maintain

            # Calculate pounds to lose or gain per 30 days
            pounds_to_lose_per_30_days = ((adjusted_calorie_goal - bmr) / 3500) * 30 if goal == "Lose" else None
            pounds_to_gain_per_30_days = ((adjusted_calorie_goal - bmr) / 3500) * 30 if goal == "Gain" else None
            maintain_weight = True if goal == "Maintain" else False

            if pounds_to_lose_per_30_days is not None:
                pounds_to_lose_per_30_days = round(pounds_to_lose_per_30_days, 1)
            if pounds_to_gain_per_30_days is not None:
                pounds_to_gain_per_30_days = round(pounds_to_gain_per_30_days, 1)

            # Display results
            self.controller.show_calorie_page(adjusted_calorie_goal, pounds_to_lose_per_30_days, pounds_to_gain_per_30_days,maintain_weight)

        except ValueError as e:
              error_label = tk.Label(self, text=str(e), font=("Arial", 12), fg="red")
              error_label.pack(pady=10)


    def get_activity_level_factor(self):
        activity_level = self.activity_var.get()
        if activity_level == "Lightly Active":
            return 1.375
        elif activity_level == "Moderately Active":
            return 1.55
        elif activity_level == "Very Active":
            return 1.725
        elif activity_level == "Extremely Active":
            return 1.9
        else:
            raise ValueError("Invalid activity level")

