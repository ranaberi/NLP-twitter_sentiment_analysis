# strip_punctuation removes characters considered punctuation from everywhere in the word.
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(word):
    new_word=""
    for c in word:
        if c not in punctuation_chars:
            new_word= new_word+c
    return new_word

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(sentences):
    lower_string=sentences.lower()                    ## As the list of positive words are in lower case
    str_punc_removed=strip_punctuation(lower_string)  ##For Punctuation Removal
    splitted_string=str_punc_removed.split()          ## For splitting the sentence into words
    
    
    pos_count=0
    for w in splitted_string:
        if w in positive_words:
            pos_count=pos_count+1
    return pos_count

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(sentences):
    neg_score = 0
    lower_sentences = sentences.lower()
    stripped_sentences = strip_punctuation(lower_sentences)
    words = stripped_sentences.split()
    
    for word in words:
        if word in negative_words:
            neg_score= neg_score+1
    return neg_score
