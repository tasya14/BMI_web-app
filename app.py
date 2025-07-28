# app.py
from flask import Flask, render_template, request

class BMICalculatorApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def calculate_bmi(self, weight, height_cm):
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        return round(bmi, 2)

    def interpret_bmi(self, bmi):
        if bmi < 18.5:
            return "Kurus"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Gemuk"
        else:
            return "Obesitas"

    def setup_routes(self):
        @self.app.route("/", methods=["GET", "POST"])
        def index():
            bmi = None
            category = None
            if request.method == "POST":
                try:
                    weight = float(request.form["weight"])
                    height = float(request.form["height"])
                    bmi = self.calculate_bmi(weight, height)
                    category = self.interpret_bmi(bmi)
                except ValueError:
                    category = "Input tidak valid"
            return render_template("index.html", bmi=bmi, category=category)

# Ini yang dibaca gunicorn
app = BMICalculatorApp().app
