# Movie Recommendation System

A content-based movie recommendation system built with Python and the TMDB 5000 Movies and Credits datasets. It recommends five movies similar to a movie selected by the user.

## How It Works

1. Load the TMDB movies and credits CSV files with Pandas.
2. Merge the datasets using the movie title.
3. Keep relevant fields such as genres, keywords, overview, cast, director, release year, and title.
4. Parse genres and keywords, select the top three cast members, and extract directors.
5. Combine the selected movie information into a single `tags` text field.
6. Convert text to lowercase and apply Porter stemming.
7. Use `CountVectorizer` to convert tags into numerical vectors.
8. Calculate pairwise cosine similarity between movies.
9. Save the processed movie data and similarity matrix for the application.
10. When a user selects a movie, return the five most similar movies, excluding the selected movie itself.

## Technologies

- Python
- Pandas
- NLTK (PorterStemmer)
- scikit-learn (`CountVectorizer`, `cosine_similarity`)
- Pickle
- Joblib
- Streamlit, if used by the app interface

## Suggested Project Structure

```text
Movie-Recommendation-System/
├── model_building/
│   ├── movie_recommendation.ipynb
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
├── app/
│   ├── app.py
│   ├── movies.pickle
│   └── similarites.joblib
├── README.md
├── requirements.txt
└── .gitignore
```

Adjust the filenames and folders above to match the files in your repository. Your code currently saves the similarity file as `similarites.joblib` (spelled `similarites`, without the second `i` in `similarities`); use the exact same filename in the app unless you rename it in both places.

## Dataset

The model-building code expects these input files:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

Place them where the notebook/script expects them, or update the file paths. Before sharing datasets, check their source, usage terms, and licensing.

## Installation

Use Python 3. Create a virtual environment if possible, then install the dependencies used by your project:

```bash
python -m pip install pandas nltk scikit-learn joblib
```

If your app uses Streamlit, also install it:

```bash
python -m pip install streamlit
```

You can save your project's exact dependencies in `requirements.txt` and install them with:

```bash
python -m pip install -r requirements.txt
```

## Generate the Saved Files

Run the model-building notebook/script from the directory containing the CSV files (or update its paths). It generates:

- `movies.pickle` — the processed movie DataFrame used by the app.
- `similarites.joblib` — the precomputed cosine-similarity matrix used to rank similar movies.

The application must load these files from the correct paths. Keep the filenames consistent between the model-building code and app code.

## Run the App

Run the command appropriate for your app. For a Streamlit app named `app.py`, for example:

```bash
streamlit run app/app.py
```

Update the command if your app file or folder has a different name. If the app loads the saved files using relative paths, ensure it is run from the expected working directory or use paths based on the script's directory.

## Example

The model-building code includes this example:

```python
recommend('avatar')
```

It prints five movie titles with the highest cosine similarity to *Avatar*, excluding the selected movie itself. The app can present those titles in its own interface.

## Important Notes

- The saved files are generated artifacts, not the source code. Include them in GitHub if the app requires them and they are reasonably sized; otherwise, document how to regenerate them.
- GitHub rejects individual files larger than 100 MB in ordinary Git pushes. Use Git LFS or another suitable storage method for larger artifacts.
- Only load pickle files from sources you trust: unpickling untrusted files can execute code.
- The similarity matrix grows quadratically with the number of movies, so it can use substantial memory as the dataset grows.
- Recommendations are based on content similarity, not user ratings or collaborative filtering.

## Future Improvements

- Add a screenshot or deployed demo link.
- Display movie posters and summaries in the app.
- Handle movie titles that are missing from the dataset.
- Document exact app usage and dependency versions.
- Add evaluation and user feedback to assess recommendation quality.

## Author

**Naveen Reddy Sagam**

GitHub: https://github.com/Naveen630342
