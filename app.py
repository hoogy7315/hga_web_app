from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        date = request.form['date']
        time = request.form['time']
        message = request.form['message']

        # TEMP: Print submitted data to the terminal
        print("New appointment booked:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Date: {date}")
        print(f"Time: {time}")
        print(f"Message: {message}")

        return "Appointment submitted successfully!"
    else:
        return render_template('appointment.html')

if __name__ == '__main__':
    app.run()
