import os, re
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


class WordCount():
    def __init__(self, fileName):
        self.totalWords = 0
        self.commonWords = self.getCommon()
        self.speach = self.getSpeachWords(fileName)
        self.lexicon= self.getLexicon()
        self.fileName = fileName

    '''
        Get List of common words from file,
        returned as a python dictionary to
        improve efficiency while using the
        python in oprerator.

        O(1) against O(N) in python List
    '''
    def getCommon(self):
        commonWords = {}
        with open('common.txt', 'r') as commonFile:
            for line in commonFile:
                commonWords[line.strip().lower()] = 0
        return commonWords

    def getLexicon(self):
        lexicon = {}
        with open('sent_lexicon.csv', 'r') as lexiconFile:
            for line in lexiconFile:
                temp = line.strip().split(',')
                lexicon[temp[0]] = float(temp[1])
        return lexicon


    '''
        Get speach, delete all special characters and add into
        dictionary
    '''
    def getSpeachWords(self, filename):
        speach = {}
        wordCount = 0
        filepath = os.path.join(filename)
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                for line in file:
                    line = re.compile(r"[^a-zA-Z\s']+").sub(r' ', line).lower().strip()
                    #line = re.compile(r"[^(\w+-)*\w+('\w+)?]").sub(r' ', line).lower().strip()
                    for word in line.split(' '):
                        if word not in self.commonWords and word != '':
                            if word in speach:
                                speach[word] += 1
                            else:
                                speach[word] = 1
                            wordCount +=1


        if '' in speach: del speach['']  #Delete any blank spaces that were added
        self.totalWords = wordCount
        return speach

    def printSorted(self):
        words = sorted(self.speach.items(), key= lambda x: x[1], reverse=True)
        for x in words:
            print '{0} - {1}'.format(x[0], x[1])

    def stats(self):

        values = [[self.lexicon[x]] * self.speach[x] for x in self.speach.keys() if x in self.lexicon]
        values = [item for sublist in values for item in sublist]

        #values = [self.lexicon[x] * self.speach[x] for x in self.speach.keys() if x in self.lexicon]

        # Create a numpy array and get values

        stats = np.array(values)
        print 'Mean Sentiment Score: {}'.format(stats.mean())
        print 'Variance: {}'.format(stats.var())
        print 'Standard Deviation: {}'.format(stats.std())


        WordsLexicon = len(values)
        WordsNotLexicon = len(self.speach) - WordsLexicon
        print 'Total Words: {}'.format(self.totalWords)
        print 'Words Found in Lexicon: {}'.format(WordsLexicon)
        print 'Words Not in Lexicon: {}'.format(WordsNotLexicon)

        buckets = [0]*5
        for x in values:
            if x <= -.6:
                buckets[0] += 1
            elif x > -.6 and x <= -.2:
                buckets[1] += 1
            elif x > -.2 and x <= .2:
                buckets[2] += 1
            elif x > .2 and x <= .6:
                buckets[3] += 1
            else:
                buckets[4] += 1

        buckets = [float(x)/len(values) for x in buckets]

        xlabels = ['Negative', 'Weak Negative', 'Neutral', 'Weak Positive', 'Positive']
        plt.xlabel('Sentiment')
        plt.ylabel('Percent of words')
        plt.xticks([ i + .4 for i in range(5)], xlabels)
        plt.title('Sentiment Distribution for {}'.format(self.fileName))
        plt.bar([x for x in range(5)], buckets, .8)
        plt.grid(True)
        plt.show()


def main():
    file = raw_input('Enter the name of your file: ')
    if os.path.exists(file) == False:
        raise IOError('File does not exists')
    wc = WordCount(file)
    wc.stats()


if __name__ == '__main__':
    main()
