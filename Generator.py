from nltk import *
import nltk
import random
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords

def removePunctuation(wordFile):
    content = [w for w in wordFile if w.isalpha()]
    return content

corpus_root = r'Country'
fileLists = PlaintextCorpusReader(corpus_root, '.*\.txt')

allWords = []

# get each word in assigned genre and add to list
for fileid in fileLists.fileids():
    for word in fileLists.words(fileid):
        allWords.append(word.lower())

allWords = removePunctuation(allWords)

bigramList = ngrams(allWords, 2)
trigramList = ngrams(allWords, 3)

# create MEGALIST out of bigrams and trigrams in allWords
megaList = []
megaList += bigramList
megaList += trigramList

# create conditional frequency distribution out of all bigrams in trigrams
cfd = nltk.ConditionalFreqDist([(tuple(a), b) for *a, b in megaList])

# find random starting word out of every word available
wordList = [random.choice(allWords)]

for i in range(50):
    # check if word(s) have a trigram equivalent,
    # if not, check if second word has bigram equivalent
    # add random chosen result to list
    for i in range(2, 1, -1):
        if tuple(wordList[-i:]) in cfd:
            wordList.append(random.choice(list(cfd[tuple(wordList[-i:])].keys())))
            break
        else:
            continue

# iterate through list to produce clean output
for word in wordList:
    print(word, end=" ")
