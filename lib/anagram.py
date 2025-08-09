# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        matches = []
        for candidate in candidates:
            # Convert to lowercase
            candidate_lower = candidate.lower()

            # Skip identical word
            if candidate_lower == self.word:
                continue

            # Compare sorted letters
            if sorted(candidate_lower) == sorted(self.word):
                matches.append(candidate)

        return matches
