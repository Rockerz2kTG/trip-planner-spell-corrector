# trip-planner-spell-corrector
Spell Correction and context understanding for Trip Planner Flow

TripPlannerSpellCorrector
The TripPlannerSpellCorrector class is designed to assist in correcting misspelled words commonly found in trip planning scenarios. It utilizes NLTK (Natural Language Toolkit) corpus to load a set of English words for reference.

Features
Corrects misspelled words in trip planning related sentences.
Utilizes edit distance and word probability to suggest corrections.
Easy to integrate and use in trip planning applications.

Usage
from trip_planner_spell_corrector import TripPlannerSpellCorrector

# Initialize the spell corrector
spell_corrector = TripPlannerSpellCorrector()

# Example usage
sentence = "I want to vist Paris and Lonon next week."
corrected_sentence = spell_corrector.correct_spelling(sentence)
print(corrected_sentence)
# Output: "I want to visit Paris and London next week."

Methods
'correct_spelling(sentence: str) -> str'
Tokenizes the input sentence into words.
Checks each word for misspelling and suggests corrections if necessary.
Returns the corrected sentence.
'get_correct_word(word: str) -> str'
Finds the most probable correct word based on edit distance and word probability.
Returns the most probable correct word.
'get_word_suggestions(word: str) -> List[str]'
Generates possible corrections for the misspelled word.
Returns a list of suggested corrections.
'word_probability(word: str) -> float'
Returns the probability of a word being correct based on its presence in the NLTK word set.

Installation
Clone the repository:
git clone https://github.com/your_username/trip-planner-spell-corrector.git

Install the required dependencies:
pip install -r requirements.txt

Contributions
Contributions to enhance the spell corrector or add new features are welcome. Feel free to submit pull requests or raise issues in the repository.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
Your Name

Acknowledgments
This project utilizes the NLTK corpus for English word reference.
