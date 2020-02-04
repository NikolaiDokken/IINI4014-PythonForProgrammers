def readFile(filename):
    file = open(filename, "r")
    return file.read()


def stripWord(word):
    """
    Method that strips a word from punctuation, and makes it lowercase
    word: String: word that is to be stripped
    """
    word = word.replace(",", "")
    word = word.replace("\"", "")
    word = word.replace(":", "")
    word = word.replace(".", "")
    word = word.lower()
    return word


def avgWordsPerSentence(filename):
    '''
    Finds the average amount of words per sentence in a file
    filename: String: Name of textfile
    return: float: avg words per sentence
    '''
    content = readFile(filename)
    amtSentences = len(content.split("."))
    amtWords = len(content.split())
    return amtWords / amtSentences


def percenteageEasyWords(filename):
    '''
    Finds percentage of \"easy\" words in a text
    filename: String: name of textfile
    Assume that easy words has a frequency higher than 0.2%
    return: float: percentage of easy words
    '''

    amtWords = len(readFile(filename).split())
    freqsDict = getWordFreqs(filename)
    amtEasyWords = 0
    for key in freqsDict:
        # print(freqsDict[key] / amtWords)
        if (freqsDict[key] / amtWords > 0.002):
            amtEasyWords += 1
    # print(amtEasyWords)
    return (amtEasyWords / amtWords)*100


def percenteageDifficultWords(filename):
    '''
    Finds percentage of \"diffucult\" words in a text
    filename: String: name of textfile
    Assume that easy words has a frequency lower than or equal to 0.02%
    return: float: percentage of easy words
    '''

    amtWords = len(readFile(filename).split())
    freqsDict = getWordFreqs(filename)
    amtDifficultWords = 0
    for key in freqsDict:
        # print(freqsDict[key] / amtWords)
        if (freqsDict[key] / amtWords <= 0.002):
            amtDifficultWords += 1
    # print(amtEasyWords)
    return (amtDifficultWords / amtWords)*100


def percenteageDifferentWords(filename):
    '''
    Finds percentage of different words in a text
    filename: String: name of textfile
    return: float: percentage of different words
    '''

    amtWords = len(readFile(filename).split())
    freqsDict = getWordFreqs(filename)
    amtDifferentWords = 0
    for key in freqsDict:
        # print(freqsDict[key] / amtWords)
        if (freqsDict[key] == 1):
            amtDifferentWords += 1
    # print(amtEasyWords)
    return (amtDifferentWords / amtWords)*100


def getWordFreqs(filename):
    """
    Gets the frequency of all words in a text file
    filename: String: the name of the file that is to be read
    """
    # opens the file in read mode
    content = readFile(filename)

    # List with all the words in a file
    wordList = content.split()
    # Dictionary with a word as key, and the frequency as value
    freqsDict = {}
    # Foor loop that increases value by 1 if word exist in dictionary, or adds the word
    for word in wordList:
        word = stripWord(word)

        if (word in freqsDict):
            freqsDict[word] += 1
        else:
            freqsDict[word] = 1

    return freqsDict


def avgSentencesPerParagraph(filename):
    '''
    Finds the average amount of words per sentence in a file
    filename: String: Name of textfile
    return: float: avg words per sentence
    '''
    content = readFile(filename)
    amtSentences = len(content.split("."))
    amtParagraphs = len(content.split("\n\n"))
    return amtSentences / amtParagraphs


def main():
    print("Average words per sentence", avgWordsPerSentence('test.txt'))
    print("Percentage of easy words", percenteageEasyWords('test.txt'), "%")
    print("Percentage of diffucult words",
          percenteageDifficultWords('test.txt'), "%")
    print("Percentage of different words",
          percenteageDifferentWords('test.txt'), "%")
    print("Average sentences per paragraph",
          avgSentencesPerParagraph('test.txt'))


main()
