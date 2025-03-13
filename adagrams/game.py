from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

alphabet = list(LETTER_POOL.keys())
print(alphabet)

# meow meow
def draw_letters():

    alphabet_pool = dict(LETTER_POOL)
    results = []

    print(alphabet_pool)

    while len(results) < 10:

        random_num = randint(0, 25)

        letter = alphabet[random_num]

        if alphabet_pool[letter] > 0:
            results.append(letter)
            alphabet_pool[letter] -= 1

    print(results, alphabet_pool)
    return results


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass