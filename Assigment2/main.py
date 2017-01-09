import os, re


class WordCount():
    def __init__(self, fileName):
        self.commonWords = self.getCommon()
        self.speach = self.getSpeachWords(fileName)

    '''
        Get List of common words from file,
        returned as a python dictionary to
        improve efficiency while using the
        python in oprerator.

        O(1) against O(N) in python List
    '''
    def getCommon(self):
        commonWords = {}
        with open('data/common.txt', 'r') as commonFile:
            for line in commonFile:
                commonWords[line.strip().lower()] = 0
        return commonWords


    '''
        Get speach, delete all special characters and add into
        dictionary
    '''
    def getSpeachWords(self, filename):
        speach = {}
        filepath = os.path.join(filename)
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                for line in file:
                    line = re.compile(r"[^a-zA-Z0-9\s']+").sub(r' ', line).lower().strip()
                    for word in line.split(' '):
                        if word not in self.commonWords:
                            if word in speach:
                                speach[word] += 1
                            else:
                                speach[word] = 1
        if '' in speach: del speach['']  #Delete any blank spaces that were added
        return speach

    def printSorted(self):
        words = sorted(self.speach.items(), key= lambda x: x[1], reverse=True)
        for x in words:
            print '{0} - {1}'.format(x[0], x[1])


def main():
    file = raw_input('Enter your file name: ')
    file = os.path.join('data/', file)
    if os.path.exists(file) == False:
        raise IOError('File does not exists')
    wc = WordCount(file)
    wc.printSorted()






if __name__ == '__main__':
    main()
