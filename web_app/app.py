from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/calculate', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def result():
    first = request.form['first']
    second = request.form['second']

    if not first.isdigit() or not second.isdigit():
        return 'Введенные значения не являютя целыми числами <a href="/calculate"> Назад </a>'

    first = int(first)
    second = int(second)
    operation = request.form['operation']
    numb = 0

    if operation == 'add':
        numb = first + second

    elif operation == 'sub':
        numb = first - second

    elif operation == 'mul':
        numb = first * second

    elif operation == 'div':
        if second == 0:
            return 'Ошибка: деление на 0 <a href="/calculate"> Назад </a>'
        numb = first / second


    return render_template('result.html', finil_value=numb)

if __name__ == '__main__':
    app.run()