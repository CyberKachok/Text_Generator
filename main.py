import nltk
import random
import re
file = open("corpus.txt", "r", encoding="utf-8")
text = file.read()
file.close()
# Break the corpus into individual words
tokens_list = nltk.WhitespaceTokenizer().tokenize(text)
trigram = list(nltk.ngrams(tokens_list, 3))
# Make trigram dict of heads and tails with counting
freq_dict = {}
for head, body, tail in trigram:
    freq_dict.setdefault(head + " " + body + " ", {})
    freq_dict[head + " " + body + " "].setdefault(tail, 0)
    freq_dict[head + " " + body + " "][tail] += 1
# Make a list of 'heads' that start with capitalized words
uppercase_list = re.findall(r"[A-Z]+[a-z]*['-]*[A-Za-z]*\s\w+\s", str(freq_dict.keys()))[:-1]


# add tail to string and create new head
def byte_the_tail():
    global head, string
    probabilities = list(freq_dict[head].values())
    words = list(freq_dict[head].keys())
    string += " " + str(head.split()[-1]) if len(string.split()) != 0 else str(head)[:-1]
    # create new head
    head = random.choices(words, weights=probabilities)[0]
    head = string.split()[-1] + " " + head + " "


# control loop
for i in range(10):
    stop_the_loop = False
    # choose first head of the sentence
    head = random.choice(uppercase_list)
    string = ""
    while not stop_the_loop:
        if len(string.split()) < 4:
            byte_the_tail()
        else:
            if re.search(r"[.!?]", head[-2]) is not None:
                stop_the_loop = True
            byte_the_tail()
    print(string)
