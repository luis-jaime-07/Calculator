from flask import Flask, render_template, request

app = Flask(__name__)
history = []  # stores previous calculations

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    if request.method == "POST":
        if "clear" in request.form:  # check if Clear button pressed
            history.clear()
            result = ""
        else:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
                op_symbol = "+"
            elif operation == "subtract":
                result = num1 - num2
                op_symbol = "-"
            elif operation == "multiply":
                result = num1 * num2
                op_symbol = "*"
            elif operation == "divide":
                result = num1 / num2
                op_symbol = "/"

            # Save calculation to history
            history.append(f"{num1} {op_symbol} {num2} = {result}")

    return render_template("index.html", result=result, history=history)

if __name__ == "__main__":
    app.run(debug=True)
