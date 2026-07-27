# 🎵 Music Recommender Simulation

## Project Summary

This project is a simple music recommendation system that suggests songs based on a user's preferences. The program compares each song with the user's favorite genre, mood, and preferred energy level. Every song receives a score, and the songs with the highest scores are recommended.

This project demonstrates how recommendation systems can turn song data and user preferences into personalized suggestions.

---

## How The System Works

Each song in the dataset contains the following features:

- Title
- Artist
- Genre
- Mood
- Energy
- Tempo
- Valence
- Danceability
- Acousticness

The user profile stores:

- Favorite genre
- Favorite mood
- Preferred energy level

The recommender checks every song in the CSV file and compares it with the user's preferences.

### Algorithm Recipe

- Genre match = +2 points
- Mood match = +1 point
- Energy similarity = up to +1 point

The energy score is based on how close the song's energy is to the user's preferred energy.

After every song receives a score, the songs are sorted from highest score to lowest score. The top five songs are displayed with their final scores and explanations.

The data flow is:

```text
User Preferences
      ↓
Load Songs from CSV
      ↓
Score Every Song
      ↓
Sort Songs by Score
      ↓
Display Top 5 Recommendations
```

---

## Getting Started

### Setup

1. Create a virtual environment. This step is optional.

```bash
python -m venv .venv
```

2. Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the program:

```bash
python -m src.main
```

### Running Tests

Run the tests with:

```bash
pytest
```

---

## Sample Recommendation Output

User profile:

```text
Genre: pop
Mood: happy
Energy: 0.8
```

Program output:

```text
Loading songs from data/songs.csv...

Top recommendations:

Sunrise City - Score: 3.98
Because: Genre match (+2), Mood match (+1), Energy similarity (+0.98)

Gym Hero - Score: 2.87
Because: Genre match (+2), Energy similarity (+0.87)

Rooftop Lights - Score: 1.96
Because: Mood match (+1), Energy similarity (+0.96)

Night Drive Loop - Score: 0.95
Because: Energy similarity (+0.95)

Storm Runner - Score: 0.89
Because: Energy similarity (+0.89)
```

---

## Experiments You Tried

I tested the recommender using different types of user preferences.

The first profile preferred happy pop music with high energy. The system ranked songs with a matching pop genre and happy mood near the top.

The second profile preferred chill music with lower energy. The recommendations changed because songs with energy values closer to the user's target received higher scores.

The third profile preferred intense rock music with high energy. Rock songs ranked higher because the genre match was worth two points.

I also considered changing the importance of the scoring rules. Reducing the genre weight would make mood and energy more important. Increasing the energy weight would cause songs with similar energy levels to rank higher, even when their genres did not match.

---

## Limitations and Risks

This recommender has several limitations.

- It uses a small song catalog.
- It only compares a few song features.
- It does not use listening history, likes, skips, or playlists.
- It does not understand lyrics or song language.
- The genre weight may be too strong and cause the same genres to appear repeatedly.
- Users may get trapped in a filter bubble because the system mainly recommends songs similar to their existing preferences.

The recommendations are only simulations and should not be treated as a complete understanding of a person's musical taste.

---

## Reflection

This project helped me understand how recommendation systems turn data into predictions. Even a simple scoring system can produce results that feel personalized. The program does not truly understand music, but it can compare numbers and categories to find songs that match a user's preferences.

Using AI tools helped me understand how to load CSV data, calculate scores, sort recommendations, and explain the results. I still needed to check the generated code and make sure the scoring rules matched my project plan. I also learned that bias can appear when one feature, such as genre, receives more weight than the others. A larger and more diverse dataset would make the recommendations more useful and fair.

For more information, read the completed [Model Card](model_card.md).


