
class SentimentStore:
    def __init__(self):
        # TODO: decide which data structure you need to track
        #       the sentiment of each word
        # TODO: decide which data structure you need to track
        #       the number of times each word has been seen
        self.totwords = 0
        self.poswords = {}
        self.negWords= {}
        self.uniWords = {}
    
    def getNumberOfWords(self):
        # TODO:
        return self.totwords

    def getNumberOfPositiveWords(self):
        # TODO:  return the number of unique words with positive scores
        lenghtofPos = len(self.poswords)
        return lenghtofPos

    def getNumberOfNegativeWords(self):
        # TODO:  return the number of unique words with negative scores
        lengthofNeg = len(self.negWords)
        return lengthofNeg

    def getTotalWordCount(self):

        # TODO:  return the total number of unique words in the store
        self.uniWords = dict(self.poswords)
        for key in self.negWords:
            self.uniWords.update({key: -1})
        return len(self.uniWords)

    def addWordScore(self, word, score):
        # TODO: add a word with a score
        #        - add score to our running total score for that word
        #        - add 1 to our count for number of times this word has been seen
        if score == -1:
            if word in self.negWords:
                self.negWords[word] -= 1

            else:
                self.negWords.update({word:score})
        else:
            if word in self.poswords:
                self.poswords[word] += 1
            else:
                self.poswords.update({word:score})

    def addStringScore(self, string, score):
        words = string.split(" ")
        #if len(words) < 50:
         #   score = 1.5
        testlist = []
        for word in words:
            if len(word) > 2: # ignore short words
                if len(testlist)<2:
                    testlist.append(word)
                if len(testlist)==2:
                    newtr = "".join(testlist)
                    self.addStringScore(newtr,score)

                    del testlist[0]
                    del testlist[0]

                self.addWordScore(word, score)
                #print(word)

                self.totwords+= 1

    def getWordSentiment(self, word):
        # TODO: return sentiment score for a given word,
        # TODO: return 0 if word not in store
        poscounter = 0
        negcounter = 0
        point = 0
        if word in self.poswords:

            poscounter += self.poswords[word]
        if word in self.negWords:
            negcounter += self.negWords[word]
        #print("Sentiment",poscounter+ negcounter)
        return poscounter+negcounter


    def getWordCount(self, word):
        # TODO: return how many times we have seen a word
        # TODO: return 0 if word not in store
        counter = 0
        pos = 0
        neg = 0
        if word in self.poswords:

            pos += self.poswords[word]
        if word in self.negWords:
            neg += self.negWords[word]
        #print(pos - neg)
        return pos - neg

    def getNormalizedWordSentiment(self, word):
        # This function is important - by normalizing the data we compensate
        # for the fact that some words occurs far more often than others.
        if self.getWordCount(word) != 0:
            return self.getWordSentiment(word) / self.getWordCount(word)
        else:
            return 0


    def getStringSentiment(self, s):
        score = 0
        count = 0
        tvaordsraket = []
        words = s.split(" ")
        for word in words:
            if len(word) > 2: # ignore short words
                if len(tvaordsraket)<2:
                    tvaordsraket.append(word)
                if len(tvaordsraket)==2:
                    newtr = "".join(tvaordsraket)
                    score += self.getNormalizedWordSentiment(newtr)
                    del tvaordsraket[0]
                    del tvaordsraket[0]



                count += 1
                word = word.lower()
                score += self.getNormalizedWordSentiment(word)
        return score / count
