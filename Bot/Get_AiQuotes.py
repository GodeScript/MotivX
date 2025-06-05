import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from quotes import motivational_quotes  # Importiere Zitat-Vorlagen aus separater Datei

# 1. Mini-KI-Modell (20MB, läuft auf 0.1 CPU)
model = SentenceTransformer('paraphrase-albert-small-v2')  # Kleinster verfügbarer Transformer

# 2. Dynamische Zitat-Erstellung (Beispiele - ersetzbar)

# 3. Echtzeit-Zitatgenerierung
def generate_quote(user_input):
    # 1. KI findet die passende Kategorie
    input_embed = model.encode(user_input)
    category_embeds = {cat: model.encode(cat) for cat in motivational_quotes.keys()}
    
    # 2. Wähle die ähnlichste Kategorie
    similarities = {
        cat: cosine_similarity([input_embed], [cat_embed])[0][0]
        for cat, cat_embed in category_embeds.items()
    }
    best_category = max(similarities, key=similarities.get)
    
    # 3. Generiere personalisiertes Zitat
    base_quote = np.random.choice(motivational_quotes[best_category])
    return f"{base_quote}"