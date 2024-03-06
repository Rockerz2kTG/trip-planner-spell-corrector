import re
from collections import Counter
from nltk.corpus import words as nltk_words

class TripPlannerSpellCorrector:
    def __init__(self):
        # Load English words from NLTK corpus
        self.word_set = set(nltk_words.words())

    def correct_spelling(self, sentence):
        # Tokenize sentence into words
        words = re.findall(r'\b\w+\b', sentence.lower())
        corrected_sentence = []

        # Iterate through each word in the sentence
        for word in words:
            # Check if the word is misspelled
            if word not in self.word_set:
                # Find the most probable correct word based on edit distance
                corrected_word = self.get_correct_word(word)
                corrected_sentence.append(corrected_word)
            else:
                corrected_sentence.append(word)

        return ' '.join(corrected_sentence)

    def get_correct_word(self, word):
        # Generate possible corrections for the misspelled word
        suggestions = self.get_word_suggestions(word)
...         if suggestions:
...             # Return the most probable correct word
...             return max(suggestions, key=self.word_probability)
... 
...     def get_word_suggestions(self, word):
...         # Generate possible corrections for the misspelled word
...         letters = 'abcdefghijklmnopqrstuvwxyz'
...         splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
...         deletes = [left + right[1:] for left, right in splits if right]
...         transposes = [left + right[1] + right[0] + right[2:] for left, right in splits if len(right) > 1]
...         replaces = [left + c + right[1:] for left, right in splits if right for c in letters]
...         inserts = [left + c + right for left, right in splits for c in letters]
... 
...         corrections = set(deletes + transposes + replaces + inserts)
...         return [word for word in corrections if word in self.word_set]
... 
...     def word_probability(self, word):
...         # Return probability of a word being correct
...         return self.word_set[word]
... 
... # Example usage
... if __name__ == "__main__":
...     spell_corrector = TripPlannerSpellCorrector()
... 
...     # Example sentences with potential spelling errors
...     sentences = [
...         "Planet a trip from louis well to colum bus",
...         "Plummeted from louis ville to lewisville airport",
...         "Planet krypton want to louisville to columbus",
...         "Go to dash board page"
...     ]
... 
...     # Correct the spelling of each sentence and print the result
...     for sentence in sentences:
...         corrected_sentence = spell_corrector.correct_spelling(sentence)
...         print(f"Input: {sentence}")
...         print(f"Output: {corrected_sentence}")
