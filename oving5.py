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

def getWordFreqs(filename):
    """
    Gets the frequency of all words in a text file
    filename: String: the name of the file that is to be read
    """
    # opens the file in read mode
    file = open(filename, "r")
    content = ""
    if file.mode == 'r':
        content = file.read()
    
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

def getWordsLine(filename, word):
    """
    Gets the line number(s) where a word occurs
    filename: String: the name of the file that is to be read
    word: String: the word we want to find occurences of
    """
    word = stripWord(word)
    
    # Opens file, and reads line after line
    file = open(filename, "r")
    content = []
    if file.mode == 'r':
        content = file.readlines()
    # List of linenumbers where a word occurs
    occurrences = []
    
    # checks every line and adds the linenumber to the list if the word occurs in the line
    for i in range(len(content)):
        content[i] = content[i].lower()
        try:
            content[i].index(word)
            occurrences.append(i + 1)
        except:
            # error
            pass
    
    return occurrences

def main():
    print(getWordFreqs("test.txt"))
    print(getWordsLine("test.txt", "testWord"))

main()
