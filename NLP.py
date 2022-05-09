# strip_punctuation removes characters considered punctuation from everywhere in the word.
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(word):
    new_word=""
    for c in word:
        if c not in punctuation_chars:
            new_word= new_word+c
    return new_word