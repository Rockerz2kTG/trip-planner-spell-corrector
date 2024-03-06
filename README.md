# trip-planner-spell-corrector
Spell Correction and context understanding for Trip Planner Flow

## TripPlannerSpellCorrector

The `TripPlannerSpellCorrector` class is initialized with a set of English words loaded from the NLTK corpus.
The correct_spelling method tokenizes the input sentence into words, checks if each word is misspelled, and suggests corrections if necessary.
The get_correct_word method finds the most probable correct word based on edit distance and the probability of the word being correct.
The get_word_suggestions method generates possible corrections for the misspelled word.
The word_probability method returns the probability of a word being correct based on its presence in the NLTK word set.
In the example usage section, the script demonstrates how to use the TripPlannerSpellCorrector class to correct the spelling of example sentences related to trip planning.

# Trip Planner Spell Corrector

The Trip Planner Spell Corrector is a Python script designed to identify and correct misspelled words in sentences related to trip planning. It utilizes natural language processing techniques to suggest corrections based on context and common trip planning terms.

## Features

- Corrects misspelled words in sentences related to trip planning.
- Utilizes the NLTK corpus of English words for spell correction.
- Considers context and common trip planning terms to enhance correction accuracy.

## Usage

1. Ensure you have Python installed on your system.
2. Install the necessary dependencies by running: pip install nltk
3. Download the NLTK English words corpus by running: python -m nltk.downloader words
4. Copy the provided `trip_planner_spell_corrector.py` file into your project directory.
5. Initialize a `TripPlannerSpellCorrector` object and use the `correct_spelling` method to correct misspelled sentences.

### Example Usage

```python
from trip_planner_spell_corrector import TripPlannerSpellCorrector

spell_corrector = TripPlannerSpellCorrector()

# Example sentences with potential spelling errors
sentences = [
 "Planet a trip from louis well to colum bus",
 "Plummeted from louis ville to lewisville airport",
 "Planet krypton want to louisville to columbus",
 "Go to dash board page"
]

# Correct the spelling of each sentence and print the result
for sentence in sentences:
 corrected_sentence = spell_corrector.correct_spelling(sentence)
 print(f"Input: {sentence}")
 print(f"Output: {corrected_sentence}")


