"""
Command line runner for the Music Recommender Simulation.
"""

from .recommender import load_songs, recommend_songs


def show_results(profile_name, user_prefs, songs):
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n============================================================")
    print(f"Profile: {profile_name}")
    print("============================================================\n")

    print(f"{'Title':<22} {'Score':<8} Reason")
    print("-" * 75)

    for song, score, explanation in recommendations:
        print(f"{song['title']:<22} {score:<8.2f} {explanation}")

    print()


def main():
    songs = load_songs("data/songs.csv")

    pop_profile = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8
    }

    lofi_profile = {
        "genre": "lofi",
        "mood": "calm",
        "energy": 0.3
    }

    rock_profile = {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.9
    }

    show_results("Happy Pop", pop_profile, songs)
    show_results("Chill Lofi", lofi_profile, songs)
    show_results("High-Energy Rock", rock_profile, songs)


if __name__ == "__main__":
    main()