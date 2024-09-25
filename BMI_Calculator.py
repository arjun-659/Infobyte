import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to classify BMI based on the calculated value
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Function to handle button click and perform BMI calculation
def calculate_and_display_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        # Input validation
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive values.")
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        
        # Display result in the result label
        result_text.set(f"Your BMI is: {bmi:.2f}\nCategory: {category}")
    
    except ValueError as e:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height.")

# Set up the main application window
app = tk.Tk()
app.title("BMI Calculator")
app.geometry("400x300")

# Heading label
heading_label = tk.Label(app, text="BMI Calculator", font=("Arial", 18))
heading_label.pack(pady=10)

# Weight label and input
weight_label = tk.Label(app, text="Enter your weight (kg):")
weight_label.pack(pady=5)
entry_weight = tk.Entry(app)
entry_weight.pack(pady=5)

# Height label and input
height_label = tk.Label(app, text="Enter your height (m):")
height_label.pack(pady=5)
entry_height = tk.Entry(app)
entry_height.pack(pady=5)

# Button to trigger BMI calculation
calculate_button = tk.Button(app, text="Calculate BMI", command=calculate_and_display_bmi)
calculate_button.pack(pady=20)

# Result display label
result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, font=("Arial", 14))
result_label.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
