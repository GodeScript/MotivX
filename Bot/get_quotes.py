import random
from quotes import motivational_quotes  # Import the list of quotes from quotes.py

def get_random_quote(issue):
    """Returns a random motivational_quotesal quote."""
    if any(word in issue for word in [
        "about to give up", "can't take it", "too hard", "want to quit", 
        "exhausted", "my brain hurts", "mentally drained", "hit a wall"
    ]):
        quote = random.choice(motivational_quotes["mental_toughness"])

    # Hustle & Grind (for laziness, procrastination)
    elif any(word in issue for word in [
        "lazy", "procrastinate", "no motivational_quotes", "don't feel like working", 
        "others are ahead", "wasting time", "need to hustle", "behind schedule"
    ]):
        quote = random.choice(motivational_quotes["hustle"])

    # Success Principles (for ambition, goals)
    elif any(word in issue for word in [
        "want success", "how to be rich", "financial freedom", 
        "build wealth", "get ahead", "role models", "successful people"
    ]):
        quote = random.choice(motivational_quotes["success"])

    # Failure & Growth (for setbacks, mistakes)
    elif any(word in issue for word in [
        "i failed", "embarrassed", "messed up", "keep failing", 
        "rejected", "nobody believes in me", "wasted my chance"
    ]):
        quote = random.choice(motivational_quotes["failure"])

    # Mindset Shifts (for self-doubt, negativity)
    elif any(word in issue for word in [
        "i'm not good enough", "full of doubt", "imposter syndrome", 
        "negative thoughts", "hate myself", "no confidence"
    ]):
        quote = random.choice(motivational_quotes["mindset"])

    # Warrior Mentality (for fear, adversity)
    elif any(word in issue for word in [
        "scared", "too afraid", "can't handle pressure", "life is unfair", 
        "people doubt me", "naysayers", "haters", "bullied"
    ]):
        quote = random.choice(motivational_quotes["warrior"])

    # Business & Money (for entrepreneurship, money struggles)
    elif any(word in issue for word in [
        "business is failing", "broke", "need money", "how to invest", 
        "bad clients", "raise prices", "start a company"
    ]):
        quote = random.choice(motivational_quotes["business"])

    # Life Truths (for existential questions)
    elif any(word in issue for word in [
        "what's the point", "life is meaningless", "nobody cares", 
        "wasting my life", "midlife crisis", "existential dread"
    ]):
        quote = random.choice(motivational_quotes["life"])

    # Discipline (for consistency struggles)
    elif any(word in issue for word in [
        "no discipline", "keep slipping", "lost focus", "too distracted", 
        "addicted to", "bad habits", "can't stick to"
    ]):
        quote = random.choice(motivational_quotes["discipline"])

    # Default: General motivational_quotes
    else:
        quote = random.choice(motivational_quotes["motivational_quotes"])
    
    return quote