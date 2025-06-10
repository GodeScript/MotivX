from flask import Flask, render_template, request, redirect, url_for
from threading import Thread

from Bot.database import add_channel
from Bot.Bot import run_bot
from bot_token import token

app = Flask(__name__)

# Bot-Informationen
bot_info = {
    'name': 'MotivX',
    'description': 'The ultimat Motivation-Bot for evry Discord Server!',
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
        'tiktok': 'TikTok',
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
        email = request.form.get('email')
        channel_id = request.form.get('channel_id')
        return redirect(url_for('success', email=email, channel_id=channel_id))
    return render_template('get_bot.html', bot=bot_info)

@app.route('/success')
def success():
    email = request.args.get('email', '')
    channel_id = request.args.get('channel_id', '')
    add_channel(str(email), int(channel_id))
    return render_template('success.html', email=email, bot=bot_info)

@app.route('/support')
def support():
    return render_template('support.html', bot=bot_info)
    
def start_programm():
    # Start the Bot in a separate thread
    bot_thread = Thread(target=run_bot, args=(token, ))
    bot_thread.start()
    
    # Start the Web in a separate thread
    app.run(debug=True)
    
start_programm()