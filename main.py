from csv import reader

FIND_WORDS = "find_words.txt"
FRENCH_DICTIONARY = "french_dictionary.csv"
T8 = "t8.shakespeare-Copy.txt"

def csvToDict(file:str) -> dict:
    dictionary = dict()
    with open(file, "r") as csvFile:
        csvData = reader(csvFile)
        for row in csvData:
            # print(row)
            dictionary[row[0]] = row[1]
    return dictionary

def readFindWords(file:str) -> list:
    findWordsList = list()
    with open(file, 'r') as findWordsFile:
        lines = findWordsFile.readlines()
        for line in lines:
            findWordsList.append(line.strip("\n"))
    return findWordsList

def replaceWords(findWords:list, frenchDictionary:dict):
    with open(T8, 'r') as t8:
        fileData = t8.read()
    for i in findWords:
        fileData = fileData.replace(i, frenchDictionary[i])
    with open(T8, 'w') as t8:
        t8.write(fileData)

def main():
    replaceWords(readFindWords(FIND_WORDS), csvToDict(FRENCH_DICTIONARY))

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)