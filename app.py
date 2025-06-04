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
    port = int(os.environ.get('PORT', 10000))  # 10000 is a fallback for local testing
    app.run(host='0.0.0.0', port=port)

