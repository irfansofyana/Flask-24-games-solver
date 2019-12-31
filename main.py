from flask import Flask, render_template, request, redirect
import solver

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

def getSolution(numbers):
    return solver.findAllSolution(solver.preProcess(numbers))

@app.route('/', methods=['POST'])
def getInput():
    numbers = []
    numbers.append(request.form['firstNumber'])
    numbers.append(request.form['secondNumber'])
    numbers.append(request.form['thirdNumber'])
    numbers.append(request.form['fourthNumber'])
    res = getSolution(numbers)
    return render_template('result.html', firstNumber = numbers[0], secondNumber = numbers[1],
    thirdNumber = numbers[2], fourthNumber = numbers[3], hasil=res, banyak=len(res))

if __name__ == "__main__":
    app.run(debug=True)
