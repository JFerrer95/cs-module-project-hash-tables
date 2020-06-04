import random

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
words_that_can_follow = {}
words = words.split()

previousWord = None

for word in words:
    if previousWord is not None:
        if previousWord not in words_that_can_follow:
            words_that_can_follow[previousWord] = []
        words_that_can_follow[previousWord].append(word)
    previousWord = word


# TODO: construct 5 random sentences
# Your code here
startingWords = []
stopingWords = []
for word in words:
    if word[0].isupper() or word[0] == '"':
        startingWords.append(word)


for word in words:
    if word[-1] == '.' or word[-1] == '?' or word[-1] == '!':
        stopingWords.append(word)
    elif len(word) > 1 and ( word[-2] == '.' or word[-2] == '?' or word[-2] == '!' ):
        stopingWords.append(word)

for i in range(5):
    print(f'Sentance {i}: ')
    word = random.choice(startingWords)

    isStopped = False
    while isStopped == False:
        print(word, end=" ")

        if word not in stopingWords:
            nextWord = random.choice(words_that_can_follow[word])
            word = nextWord
        else:
            isStopped = True
    print("\n")