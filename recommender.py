import math
from collections import Counter

MOVIES = {
    "The Dark Knight": "action crime thriller superhero",
    "Inception": "sci-fi thriller action mind-bending",
    "Interstellar": "sci-fi drama space adventure",
    "The Matrix": "sci-fi action cyberpunk",
    "Titanic": "romance drama historical",
    "The Notebook": "romance drama",
    "Toy Story": "animation family comedy adventure",
    "Finding Nemo": "animation family adventure comedy",
    "The Godfather": "crime drama mafia",
    "Pulp Fiction": "crime thriller dark-comedy",
    "Avengers: Endgame": "action superhero sci-fi adventure",
    "Joker": "crime drama thriller psychological",
    "La La Land": "romance musical drama",
    "Mad Max: Fury Road": "action adventure post-apocalyptic",
    "Coco": "animation family musical adventure",
}

def vec(text):
    return Counter(text.split())

def cosine(a, b):
    dot = sum(a[k] * b[k] for k in a if k in b)
    na = math.sqrt(sum(v*v for v in a.values()))
    nb = math.sqrt(sum(v*v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0

def recommend(liked, n=3):
    profile = Counter()
    for m in liked:
        profile.update(vec(MOVIES[m]))
    scores = [(cosine(profile, vec(t)), m) for m, t in MOVIES.items() if m not in liked]
    return [m for s, m in sorted(scores, reverse=True)[:n]]

if __name__ == "__main__":
    print("Movies:", ", ".join(MOVIES))
    entered = [x.strip().lower() for x in input("Enter movies you like (comma-separated): ").split(",")]
    liked = [m for m in MOVIES if m.lower() in entered]
    if not liked:
        print("No valid movies entered.")
    else:
        print("Recommended for you:")
        for i, m in enumerate(recommend(liked), 1):
            print(f"{i}. {m}")
