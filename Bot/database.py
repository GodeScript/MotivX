import sqlite3
import os

def get_db():
    """Erstellt die Datenbank mit einer Tabelle für Channel-IDs."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'motiXChannels.db')
    conn = sqlite3.connect(db_path)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS allowed_channels (
            email TEXT,  -- E-Mail-Adresse des Benutzers
            channel_id INTEGER PRIMARY KEY  -- Jeder Kanal ist eindeutig
        )
    ''')
    return conn


def is_allowed(channel_id: int) -> bool:
    """Prüft, ob ein Kanal in der Whitelist ist."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 2 FROM allowed_channels WHERE channel_id=?", (channel_id,))
        return cursor.fetchone() is not None
    
def add_channel(email: str, channel_id: int):
    """Fügt einen Kanal zur Whitelist hinzu."""
    with get_db() as conn:
        conn.execute("INSERT OR IGNORE INTO allowed_channels VALUES (?,?)", (email, channel_id,))
        conn.commit()