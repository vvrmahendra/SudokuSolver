from flask import Flask, render_template, request
from solver import Solver

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/getsol", methods = ['POST'])
def getsol():
    arr = [['.']*9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            value = request.form.get("b"+str(9*i+j))
            if (value.isdigit() and 0<int(value)<10):
                arr[i][j] = value
            elif value == "":
                pass
            else:
                return render_template("lol.html")

    A = Solver().solver(arr)
    if A == []:
        return render_template("lol.html")
    return render_template("solution.html", A = A)




if __name__ == "__main__":
    app.run("localhost", debug = True)