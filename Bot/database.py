import sqlite3

def get_db():
    """Erstellt die Datenbank mit einer Tabelle für Channel-IDs."""
    conn = sqlite3.connect('motivabot.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS allowed_channels (
            channel_id INTEGER PRIMARY KEY  -- Jeder Kanal ist eindeutig
        )
    ''')
    return conn


def is_allowed(channel_id: int) -> bool:
    """Prüft, ob ein Kanal in der Whitelist ist."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM allowed_channels WHERE channel_id=?", (channel_id,))
        return cursor.fetchone() is not None
    
def add_channel(channel_id: int):
    """Fügt einen Kanal zur Whitelist hinzu."""
    with get_db() as conn:
        conn.execute("INSERT OR IGNORE INTO allowed_channels VALUES (?)", (channel_id,))
        conn.commit()