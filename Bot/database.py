import sqlite3
import os

def get_db():
    """Erweitert die Datenbank für Abonnements"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'motiXChannels.db')
    conn = sqlite3.connect(db_path)
    
    # Tabelle für erlaubte Channels
    conn.execute('''
        CREATE TABLE IF NOT EXISTS allowed_channels (
            email TEXT,
            channel_id INTEGER PRIMARY KEY,
            subscription_date TEXT,
            paypal_agreement_id TEXT,
            active BOOLEAN DEFAULT 1
        )
    ''')


def is_allowed(channel_id: int) -> bool:
    """Prüft ob ein Kanal aktiv ist"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 1 FROM allowed_channels 
            WHERE channel_id=? AND active=1
        ''', (channel_id,))
        return cursor.fetchone() is not None

def add_channel(email: str, channel_id: int, agreement_id: str = None):
    """Fügt einen neuen Kanal hinzu"""
    with get_db() as conn:
        conn.execute('''
            INSERT INTO allowed_channels 
            (email, channel_id, subscription_date, paypal_agreement_id)
            VALUES (?, ?, datetime('now'), ?)
        ''', (email, channel_id, agreement_id))
        conn.commit()