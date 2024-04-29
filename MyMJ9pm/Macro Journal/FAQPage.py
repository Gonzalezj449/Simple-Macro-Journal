import tkinter as tk
from tkinter import ttk  # For a better look of the widgets

class FAQPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create a Text widget to display the FAQ content
        self.FAQ = tk.Label(self, text="Frequently Asked Questions (FAQ)",font=24)
        self.FAQ.grid(row=0, column=0)

        self.text_widget = tk.Text(self, wrap="word", state='disabled', bg=self.controller.bg_color if hasattr(self.controller, 'bg_color') else 'white')
        self.text_widget.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        navigate_button = tk.Button(self, text="Go Back", command=lambda: self.controller.show_page("CaloriePage"))
        navigate_button.grid(row=2, column=0, pady=10)

        # Adding a scrollbar
        scrollbar = ttk.Scrollbar(self, command=self.text_widget.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.text_widget['yscrollcommand'] = scrollbar.set

        # Add FAQ content
        self.load_faq_content()

    def load_faq_content(self):
        faqs = [
            ("How do I track my daily calories?", "You can track your daily calories by entering the food items you consume throughout the day into the app. Use the 'Add Food' feature to input each meal."),
            ("Can I set calorie goals?", "Yes, you can set daily calorie goals. Go to the 'Settings' page and select 'Set Goals' to specify your desired calorie intake."),
            ("How are the calories calculated?", "Calories are calculated using the USDA National Nutrient Database which provides detailed nutritional information for various food items."),
            ("What if I eat a food not listed in the app?", "If you consume a food not listed in the app, you will have to contact the staff and request the item to be inputted in."),
            ("Can this app help me lose weight?", "While this app can assist in tracking your calorie intake, effective weight loss should be combined with exercise and dietary adjustments based on professional medical advice."),
        ]

        self.text_widget.config(state='normal')  # Enable the text widget to modify its contents
        for question, answer in faqs:
            self.text_widget.insert('end', f"Q: {question}\nA: {answer}\n\n")
        self.text_widget.config(state='disabled')  # Disable the text widget to prevent user editing

if __name__ == "__main__":
    app = tk.Tk()
    app.bg_color = '#f0f0f0'  # Background color example
    page = FAQPage(app, app)
    page.pack(expand=True, fill='both')
    app.mainloop()