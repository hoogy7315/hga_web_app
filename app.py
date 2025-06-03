from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/appointment')
def appointment():
    return render_template('appointment.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's port if available
    app.run(host='0.0.0.0', port=port)


