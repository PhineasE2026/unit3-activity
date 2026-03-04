from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = {
        'q1': request.form.get("q1"),
        'q2': request.form.get("q2"),
        'q3': request.form.get("q3")
    }


    politicians = [
        {
            "name": "Benjamin Netanyahu",
            "image": "images/netanyahu.jpg",
            "description": "You are spiritually Jewish"
        },
        {
            "name": "Donald Trump",
            "image": "images/trump.jpg",
            "description": "You are"
        },
        {
            "name": "Barack Obama",
            "image": "images/obama.webp",
            "description": "Measured, polished, and message-focused."
        },
        {
            "name": "Zohran Mamdani",
            "image": "images/mamdani.jpg",
            "description": "Ideological, activist, and insurgent-style."
        },
        {
            "name": "Xi Jinping",
            "image": "images/xi_jinping.jpg",
            "description": "Centralized, disciplined, and control-oriented."
        },
    ]
    
    return render_template('result.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)