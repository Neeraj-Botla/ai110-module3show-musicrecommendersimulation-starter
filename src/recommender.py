import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Song:
    """
    Represents a song and its attributes.
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    """

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        results = []

        for song in self.songs:
            score = 0

            if song.genre == user.favorite_genre:
                score += 2

            if song.mood == user.favorite_mood:
                score += 1

            score += 1 - abs(song.energy - user.target_energy)

            results.append((score, song))

        results.sort(reverse=True, key=lambda x: x[0])

        answer = []

        for item in results[:k]:
            answer.append(item[1])

        return answer

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []

        if song.genre == user.favorite_genre:
            reasons.append("Genre match")

        if song.mood == user.favorite_mood:
            reasons.append("Mood match")

        return ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    """

    print(f"Loading songs from {csv_path}...")

    songs = []

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])

            songs.append(row)

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores one song.
    """

    score = 0
    reasons = []

    if song["genre"] == user_prefs["genre"]:
        score += 2
        reasons.append("Genre match (+2)")

    if song["mood"] == user_prefs["mood"]:
        score += 1
        reasons.append("Mood match (+1)")

    energy_score = 1 - abs(song["energy"] - user_prefs["energy"])

    if energy_score < 0:
        energy_score = 0

    score += energy_score
    reasons.append(f"Energy similarity (+{energy_score:.2f})")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Returns the best recommendations.
    """

    recommendations = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)

        explanation = ", ".join(reasons)

        recommendations.append((song, score, explanation))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations[:k]
