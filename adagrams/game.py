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

SCORE_CHART = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

ALPHABET = list(LETTER_POOL.keys())

def draw_letters():

    alphabet_pool = dict(LETTER_POOL)
    results = []

    while len(results) < 10:

        random_num = randint(0, 25)

        letter = ALPHABET[random_num]

        if alphabet_pool[letter] > 0:
            results.append(letter)
            alphabet_pool[letter] -= 1

    return results


def uses_available_letters(word, letter_bank):
    
    cap_word = change_to_uppercase(word)
    letter_tracker = create_letter_tracker(letter_bank)
    result = True

    for letter in cap_word:
        if letter in letter_tracker and letter_tracker[letter] > 0:
            letter_tracker[letter] -= 1
        else:
            result = False
            break

    return result


def score_word(word):
    score = 0

    cap_word = change_to_uppercase(word)

    for letter in cap_word:
        if letter in SCORE_CHART:
            score += SCORE_CHART[letter]

    if len(cap_word) >= 7:
        score += 8

    return score

def get_highest_word_score(word_list):

    word_chart = create_word_chart(word_list)
    winners = []

    for word in word_chart.keys():

        winner_score =  winners[0]["score"] if winners else 0
        word_info = {
                "word": word,
                "score": word_chart[word]["score"],
                "length": len(word)
                }

        if not winners or winner_score == word_info["score"]:
            winners.append(word_info)
        elif word_chart[word]["score"] > winners[0]["score"]:
            winners = [word_info]

    results = None

    if len(winners) > 1:
        results = settle_score_tie(winners)
    else:
        results = (winners[0]["word"], winners[0]["score"])
    
    return results

# vvv helper functions below vvv

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

def create_word_chart(word_list):

    word_chart = {}

    for word in word_list:
        word_chart[word] = {
            "score": score_word(word),
            "length": len(word)
        }

    return word_chart

def settle_score_tie(word_list):

    check_ten = None
    highest_index = 0

    for i in range(len(word_list)):

        length_one = word_list[i]["length"]
        length_two = word_list[highest_index]["length"]
        

        if length_one == 10 and not check_ten:
            check_ten = word_list[i]
        elif length_one < length_two:
            highest_index = i

    results = None

    if check_ten:
        results = (check_ten["word"], check_ten["score"])
    else:
        results = (word_list[highest_index]["word"], word_list[highest_index]["score"])

    return results