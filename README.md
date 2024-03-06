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

### Methods

### 'correct_spelling(sentence: str) -> str'

- Tokenizes the input sentence into words.
- Checks each word for misspelling and suggests corrections if necessary.
- Returns the corrected sentence.

### 'get_correct_word(word: str) -> str'

- Finds the most probable correct word based on edit distance and word probability.
- Returns the most probable correct word.

### 'get_word_suggestions(word: str) -> List[str]'

- Generates possible corrections for the misspelled word.
- Returns a list of suggested corrections.

### 'word_probability(word: str) -> float'

- Returns the probability of a word being correct based on its presence in the NLTK word set.

### Installation

To install TripPlannerSpellCorrector, you can clone the repository:

```bash
git clone https://github.com/your_username/trip-planner-spell-corrector.git

Contributions
Contributions to enhance the spell corrector or add new features are welcome. Feel free to submit pull requests or raise issues in the repository.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
Riyaz Ahamed K K
