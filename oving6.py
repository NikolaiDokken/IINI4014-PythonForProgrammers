def swap(lines, lesser, greater):
    """
    Swaps to elements in an array
    lines: any: array of elements where two of them are to be swapped
    lesser: int: index of lesser element
    greater: int: index of greater element
    """
    temp = lines[lesser]
    lines[lesser] = lines[greater]
    lines[greater] = temp


def readFile(filename):
    """
    Reads all lines from a file and stores them in an array
    filename: String: name of file to be read. One word per line.
    """
    lines = []
    f = open(filename, "r")
    if (f.mode == "r"):
        lines = f.read().splitlines()
    return lines


def bubbleSort(filename):
    """
    Bubblesort sorting algorithm, sorts by increasing word lenght
    filename: String: name of the file containing words to sort
    """
    words = readFile(filename)
    # Makes sure the longest words are placed last
    for x in range(len(words), 1, -1):
        # Inner loop compares one word with the next in the array
        # Switch places if the first one is longer
        for i in range(0, x-1):
            if (len(words[i]) > len(words[i+1])):
                swap(words, i, i+1)
            elif (len(words[i]) == len(words[i+1])):
                # Handles words of equal length
                if (words[i] > words[i+1]):
                    swap(words, i, i+1)
    return words


def main():
    result = bubbleSort("test.txt")
    for x in result:
        print(x)


main()
