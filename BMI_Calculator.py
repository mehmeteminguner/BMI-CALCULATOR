import tkinter
gui = tkinter.Tk()
gui.title("BMI CALCULATOR")
gui.config(padx=100,pady=100)





def bmi_calculation():
    w = w_input.get()
    h = h_input.get()
    if w == "" or h == "":
        results_label.config(text="Please enter both your weight and height")
    else:
        try:
            bmi = float(w) / ((float(h) / 100)) ** 2
            result_str = writer(bmi)
            results_label.config(text=result_str)

        except:
            results_label.config(text="Enter a valid number!")







w_input_label = tkinter.Label(text="Please enter your weight in kilograms")
w_input_label.pack()
w_input = tkinter.Entry(width=30)
w_input.pack()
h_input_label = tkinter.Label(text="Please enter your height in centimeters")
h_input_label.pack()
h_input = tkinter.Entry(width=30)
h_input.pack()
CalculatorButton = tkinter.Button(text="Calculate",command=bmi_calculation)
CalculatorButton.pack()
results_label = tkinter.Label()
results_label.pack()








def writer(bmi):
    result_str = f"Your BMI is: {round(bmi,3)}  "
    if bmi <= 16:
        result_str += "Better get some food to eat pal!"
    elif 16 < bmi <= 17:
        result_str += "Just better then a minecraft skeleton"
    elif 17 < bmi <= 18.5:
        result_str += "Fine"
    elif 18.5 < bmi <= 25:
        result_str += "Bruh you good"
    elif 25 < bmi <= 30:
        result_str += "Just heavier then an average person"
    elif 30 < bmi <= 35:
        result_str += "Level 1 obesity"
    elif 35 < bmi <= 40:
        result_str += "Diabeto from The Family Guy"
    else:
        result_str += "You are the obesity itself"
    return result_str

gui.mainloop()