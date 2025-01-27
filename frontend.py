from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    selected_time = request.form.get('time_of_day')
    return redirect(url_for('display_greeting',time_of_day=selected_time))

@app.route('/greet')
def display_greeting():
    time_of_day = request.args.get('time_of_day','Morning')
    return f"Good {time_of_day.capitalize()}! This Page is work in Progress."


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)