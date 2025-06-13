from flask import Flask, render_template, request, redirect, url_for, session
from threading import Thread
import paypalrestsdk
from datetime import datetime, timedelta

from Bot.database import add_channel
from Bot.Bot import run_bot
from tokens.bot_token import token

from tokens.app_secret_key import secret_key

from tokens.paypal import canfig

app = Flask(__name__)
app.secret_key = secret_key

paypalrestsdk.configure(canfig)

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
        # Daten in Session speichern
        session['email'] = request.form.get('email')
        session['channel_id'] = request.form.get('channel_id')
        
        # Erstelle Abonnement-Plan
        billing_plan = paypalrestsdk.BillingPlan({
            "name": "MotivX Monthly Subscription",
            "description": "€5 every 30 days for MotivX Bot access",
            "type": "INFINITE",
            "payment_definitions": [{
                "name": "30-Day Payment",
                "type": "REGULAR",
                "frequency": "DAY",
                "frequency_interval": "30",
                "amount": {
                    "value": "5.00",
                    "currency": "EUR"
                },
                "cycles": "0"  # Unendlich wiederholend
            }],
            "merchant_preferences": {
                "return_url": url_for('payment_success', _external=True),
                "cancel_url": url_for('payment_cancelled', _external=True),
                "auto_bill_amount": "YES",
                "initial_fail_amount_action": "CONTINUE",
                "max_fail_attempts": "3"
            }
        })

        if billing_plan.create():
            # Aktiviere den Plan
            if billing_plan.activate():
                # Erstelle Abonnement-Vereinbarung
                start_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
                
                agreement = paypalrestsdk.BillingAgreement({
                    "name": "MotivX Premium Access",
                    "description": f"Zugang für Channel {session['channel_id']}",
                    "start_date": start_date,
                    "plan": {
                        "id": billing_plan.id
                    },
                    "payer": {
                        "payment_method": "paypal",
                        "payer_info": {
                            "email": session['email']
                        }
                    }
                })

                if agreement.create():
                    for link in agreement.links:
                        if link.rel == "approval_url":
                            return redirect(link.href)
        
        return render_template('payment_error.html', bot=bot_info)
    
    return render_template('get_bot.html', bot=bot_info)

@app.route('/payment/success')
def payment_success():
    token = request.args.get('token')
    agreement = paypalrestsdk.BillingAgreement.find(token)
    
    if agreement.execute():
        # Erstzahlung erfolgreich - Daten speichern
        add_channel(
            email=session['email'],
            channel_id=session['channel_id'],
            paypal_agreement_id=agreement.id
        )
        return render_template('success.html', email=session['email'], bot=bot_info)
    
    return render_template('payment_error.html', bot=bot_info)

@app.route('/payment/cancelled')
def payment_cancelled():
    return render_template('payment_cancelled.html', bot=bot_info)

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