"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n================ MUSIC RECOMMENDATIONS ================\n")

    print(f"{'Title':<22} {'Score':<8} Reason")
    print("-" * 75)

    for song, score, explanation in recommendations:
        print(f"{song['title']:<22} {score:<8.2f} {explanation}")

    print("\n=======================================================\n")


if __name__ == "__main__":
    main()