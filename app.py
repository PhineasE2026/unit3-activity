from flask import Flask, render_template, request
from collections import Counter
import random

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
            "image": "netanyahu.jpg",
            "description": "You are evil..."
        },
        {
            "name": "Donald Trump",
            "image": "trump.jpg",
            "description": "You are very Israeli"
        },
        {
            "name": "Barack Obama",
            "image": "obama.webp",
            "description": "You are fairly Israeli, but you are Aert"
        },
        {
            "name": "Zohran Mamdani",
            "image": "mamdani.jpg",
            "description": "The most Israeli politicianm, you are the most Israeli!"
        },
        {
            "name": "Xi Jinping",
            "image": "xi_jinping.jpg",
            "description": "you are not israel because you are China"
        },
    ]

    politician = {
        "tomato": "Donald Trump",
        "blueberry": "Xi Jinping",
        "olive": "Benjamin Netanyahu",
        "date": "Barack Obama",

        "germany": "Zohran Mamdani",
        "russia": "Donald Trump",
        "usa": "Benjamin Netanyahu",
        "brazil": "Xi Jinping",

        "football": "Benjamin Netanyahu",
        "american_football": "Barack Obama",
        "basketball": "Xi Jinping",
        "ice_hockey": "Zohran Mamdani",
    }

    options = [
        politician.get(user_input['q1']),
        politician.get(user_input['q2']),
        politician.get(user_input['q3'])
    ]
    options = [option for option in options if option]
    
    count = Counter(options)
    max_score = max(count.values())
    tied = [name for name, score in count.items() if score == max_score]
    winner_name = random.choice(tied)

    result = next(option for option in politicians if option['name'] == winner_name)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)