import requests
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Mini-KI-Modell laden
model = SentenceTransformer('paraphrase-albert-small-v2')

# 2. Hole Zitate von der API
def fetch_quotes():
    try:
        response = requests.get("https://zenquotes.io/api/quotes/100")  # 50 zufällige Zitate
        return [quote['q'] for quote in response.json()]
    except:
        return ["There is a proplem right know we will try to be as fast as posiple back"]  # Fallback

# 3. Finde das passendste Zitat mit KI
def find_best_quote(user_input, quotes):
    # Encode alles
    input_embed = model.encode(user_input)
    quote_embeds = model.encode(quotes)
    
    # Berechne Ähnlichkeiten
    similarities = cosine_similarity([input_embed], quote_embeds)[0]
    best_idx = np.argmax(similarities)
    
    return quotes[best_idx]

# 4. Hauptfunktion
def generate_quote(user_input):
    quotes = fetch_quotes()
    best_quote = find_best_quote(user_input, quotes)
    return f"💡 {best_quote}"