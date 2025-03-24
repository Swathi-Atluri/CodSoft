# Book Recommendation System

## Objective
The objective of this project is to build a simple book recommendation system that takes user input in the form of keywords (e.g., "fantasy adventure magic") and recommends the top 5 books from a dataset that best match the description. The system uses text similarity techniques to match the user’s input against book descriptions and genres, providing a straightforward and user-friendly interface.

## About the Dataset
The dataset used in this project is `goodreads_data.csv`, located at `/kaggle/input/best-books-10k-multi-genre-data/goodreads_data.csv`. It contains information about 10,000 books sourced from Goodreads, a popular book review and recommendation platform. The dataset includes the following columns:

- **Book**: The title of the book.
- **Author**: The author of the book.
- **Description**: A brief description of the book.
- **Genres**: A list of genres associated with the book (stored as a string, e.g., `['Fantasy', 'Fiction']`).
- **Avg_Rating**: The average rating of the book on Goodreads.
- **Num_Ratings**: The number of ratings the book has received.
- **URL**: The Goodreads URL for the book (not used in this project).

The dataset is used to match user-provided keywords against the `Description` and `Genres` columns to recommend relevant books.

## Packages Used and Their Purposes
The following Python packages are used in this project:

- **pandas**: Used for loading, manipulating, and preprocessing the dataset. It provides the DataFrame structure to handle tabular data efficiently.
- **scikit-learn**:
  - `TfidfVectorizer` (from `sklearn.feature_extraction.text`): Converts text data (book descriptions and genres) into numerical features using the TF-IDF (Term Frequency-Inverse Document Frequency) technique, which helps in measuring the importance of words.
  - `cosine_similarity` (from `sklearn.metrics.pairwise`): Calculates the similarity between the user’s input and each book’s text features to rank books by relevance.

## Preprocessing Done
The dataset undergoes the following preprocessing steps to prepare it for the recommendation system:

1. **Load the Dataset**: The CSV file is loaded into a pandas DataFrame using `pd.read_csv()`.
2. **Check for Required Columns**: The code ensures that the `Description` and `Genres` columns exist in the dataset, raising a `KeyError` if they are missing.
3. **Handle Missing Values**: Missing values in the `Description` and `Genres` columns are filled with empty strings using `fillna('')` to avoid errors during text processing.
4. **Clean the Genres Column**: The `Genres` column contains string representations of lists (e.g., `['Fantasy', 'Fiction']`). The square brackets and quotes are removed using `str.replace()` with a regular expression (`r"[\[\]']"`) to convert it into a clean string (e.g., `Fantasy Fiction`).
5. **Combine Text Features**: The `Description` and `Genres` columns are combined into a single `combined_text` column by concatenating them with a space in between. This combined text is used for vectorization.

## Logic Part of the Code
The recommendation system follows these steps to generate book recommendations:

1. **Text Vectorization**:
   - A `TfidfVectorizer` is initialized with English stop words removed (to ignore common words like "the", "and") and a maximum of 5,000 features (to limit the vocabulary size for efficiency).
   - The `combined_text` column of the dataset is transformed into a TF-IDF matrix, where each row represents a book, and each column represents a word’s TF-IDF score.

2. **User Input**:
   - The program prompts the user to enter keywords describing the book they’re looking for (e.g., "fantasy adventure magic").
   - A loop allows the user to make multiple queries, with the option to type `exit` to quit the program.
   - Basic input validation ensures the user doesn’t provide an empty input.

3. **Recommendation Generation**:
   - The user’s input is vectorized using the same `TfidfVectorizer` to ensure consistency with the dataset’s TF-IDF matrix.
   - Cosine similarity is calculated between the user’s input vector and the TF-IDF matrix of all books. This measures how similar the user’s input is to each book’s combined text.
   - The books are ranked by their similarity scores in descending order, and the top 5 are selected.

4. **Output**:
   - The top 5 books are displayed in a simple table using pandas’ `to_string()` method, showing the `Book`, `Author`, `Avg_Rating`, and `Similarity` score (rounded to 2 decimal places).
   - The program then prompts the user for another query or to exit.
