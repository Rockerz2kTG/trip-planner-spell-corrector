# trip-planner-spell-corrector
Spell Correction and context understanding for Trip Planner Flow

## TripPlannerSpellCorrector

The `TripPlannerSpellCorrector` class is initialized with a set of English words loaded from the NLTK corpus.
The correct_spelling method tokenizes the input sentence into words, checks if each word is misspelled, and suggests corrections if necessary.
The get_correct_word method finds the most probable correct word based on edit distance and the probability of the word being correct.
The get_word_suggestions method generates possible corrections for the misspelled word.
The word_probability method returns the probability of a word being correct based on its presence in the NLTK word set.
In the example usage section, the script demonstrates how to use the TripPlannerSpellCorrector class to correct the spelling of example sentences related to trip planning.

### Usage

```python
from trip_planner_spell_corrector import TripPlannerSpellCorrector

# Initialize the spell corrector
spell_corrector = TripPlannerSpellCorrector()

# Example usage
sentence = "I want to vist Paris and Lonon next week."
corrected_sentence = spell_corrector.correct_spelling(sentence)
print(corrected_sentence)
# Output: "I want to visit Paris and London next week."
