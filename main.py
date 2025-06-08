from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Bot-Informationen
bot_info = {
    'name': 'MotivX',
    'description': 'Der ultimative Motivations-Bot für deinen Discord-Server!',
    'features': [
        {
            'title': 'Dayly Motivation',
            'description': 'With /mt Command you say what your issue is and the bot is genareating a quote to help you.'
        },
        {
            'title': 'Future plan Goals Tracker',
            'description': 'A goal Tracking System to help you reach your goals🔥.'
        },
        {
            'title': 'Future plan Reward System',
            'description': 'Get Poins for your Goals and See your self on the leaderboard.'
        }
    ],
    'price': '5.00€',
    'support_links': {
        'youtube': 'Youtube',
        'instagram': 'Instagram',
        'X': 'X',
        'Discord': 'Discord',
        'reddit': 'Reddit',
        "gitHub": 'GitHub',
        'donate': 'Donate'
    }
}

@app.route('/')
def home():
    return render_template('index.html', bot=bot_info)

@app.route('/get_bot', methods=['GET', 'POST'])
def get_bot():
    if request.method == 'POST':
        # Hier würde die Logik für den Bot-Kauf stehen
        email = request.form.get('email')
        return redirect(url_for('success', email=email))
    return render_template('get_bot.html', bot=bot_info)

@app.route('/success')
def success():
    email = request.args.get('email', '')
    print(f"Erfolgreicher Kauf für {email}")
    return render_template('success.html', email=email, bot=bot_info)

@app.route('/support')
def support():
    return render_template('support.html', bot=bot_info)

if __name__ == '__main__':
    app.run(debug=True)