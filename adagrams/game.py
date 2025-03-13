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

ALPHABET = list(LETTER_POOL.keys())


# meow meow
def draw_letters():

    alphabet_pool = dict(LETTER_POOL)
    results = []

    print(alphabet_pool)

    while len(results) < 10:

        random_num = randint(0, 25)

        letter = ALPHABET[random_num]

        if alphabet_pool[letter] > 0:
            results.append(letter)
            alphabet_pool[letter] -= 1

    print(results, alphabet_pool)
    return results


def uses_available_letters(word, letter_bank):
    
    cap_word = change_to_uppercase(word)
    letter_tracker = create_letter_tracker(letter_bank)
    result = True

    print(cap_word, letter_bank)

    for letter in cap_word:
        if letter in letter_tracker and letter_tracker[letter] > 0:
            letter_tracker[letter] -= 1
        else:
            result = False
            break

    return result


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

def change_to_uppercase(word):

    letters = {
        "a": "A",
        "b": "B",
        "c": "C",
        "d": "D",
        "e": "E",
        "f": "F",
        "g": "G",
        "h": "H",
        "i": "I",
        "j": "J",
        "k": "K",
        "l": "L",
        "m": "M",
        "n": "N",
        "o": "O",
        "p": "P",
        "q": "Q",
        "r": "R",
        "s": "S",
        "t": "T",
        "u": "U",
        "v": "V",
        "w": "W",
        "x": "X",
        "y": "Y",
        "z": "Z"
    }

    results = ""
    lower_case = list(letters.keys())

    for letter in word:
        if letter in lower_case:
            results += letters[letter]
        else:
            results += letter
    
    return results

def create_letter_tracker(letter_bank):

    letter_tracker = {}

    for letter in letter_bank:
        if letter in letter_tracker:
            letter_tracker[letter] += 1
        else:
            letter_tracker[letter] = 1

    return letter_tracker

# uses_available_letters("meow", ['m', 'e', 'o', 'w', ])