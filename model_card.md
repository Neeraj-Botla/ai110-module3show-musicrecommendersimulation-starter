# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Intended Use

This recommender is designed to suggest songs based on a user's favorite genre, mood, and preferred energy level. It is intended as a classroom project to demonstrate how recommendation systems work.

The system assumes the user has a favorite genre, a favorite mood, and a preferred energy level. It is not designed for real-world music streaming services but instead serves as a simple educational simulation.

---

## 3. How the Model Works

The recommender compares every song in the dataset with the user's preferences.

Each song contains information such as:

- Genre
- Mood
- Energy
- Tempo
- Valence
- Danceability
- Acousticness

The user's profile stores:

- Favorite genre
- Favorite mood
- Preferred energy level

Each song receives points based on how closely it matches the user's preferences.

Scoring rules:

- Genre match = +2 points
- Mood match = +1 point
- Energy similarity = up to +1 point

After scoring every song, the songs are sorted from highest score to lowest score. The top five songs become the recommendations.

---

## 4. Data

The project uses a small CSV file containing songs with different genres and moods.

Each song includes:

- Title
- Artist
- Genre
- Mood
- Energy
- Tempo
- Valence
- Danceability
- Acousticness

The dataset is small and does not include listening history, lyrics, popularity, playlists, or user ratings.

---

## 5. Strengths

The recommender performs well when the user's preferences closely match the available songs.

It can quickly identify songs with matching genres, moods, and similar energy levels.

For the default user profile, the recommendations matched expectations because songs with the correct genre and mood appeared near the top of the list.

---

## 6. Limitations and Bias

The recommender only considers a few song features.

It does not understand lyrics, artists, listening history, or changing user preferences.

Because genre is worth more points than mood or energy, the recommender may favor songs from the same genre repeatedly. This can create a filter bubble where users receive similar recommendations every time.

The small dataset also limits recommendation quality.

---

## 7. Evaluation

I tested the recommender using several user profiles.

- Happy Pop
- Chill Lofi
- High-Energy Rock

I compared the recommended songs for each profile to see whether the rankings changed as expected.

The biggest observation was that changing the preferred genre had the largest impact on the recommendations because genre received the highest weight.

---

## 8. Future Work

Future improvements include:

- Adding a much larger song dataset.
- Using listening history.
- Including artist preferences.
- Considering popularity and release year.
- Improving recommendation explanations.
- Increasing diversity in the recommendation list.
- Allowing users to change scoring weights.

---

## 9. Personal Reflection

This project helped me understand how recommendation systems use simple data to make personalized suggestions. Even though the algorithm is simple, it can still produce recommendations that feel useful.

Using AI tools helped me understand CSV processing, scoring logic, sorting, and recommendation algorithms. I also learned that AI-generated code should always be reviewed and tested before using it.

The biggest lesson from this project was that recommendation quality depends heavily on both the scoring rules and the quality of the data. A better dataset usually leads to better recommendations.
