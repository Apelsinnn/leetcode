import re


def sortSentence(text: str) -> str:
    array = [(word[-1], word[:-1]) for word in text.split(' ')]
    array.sort()
    return ' '.join([element[1] for element in array])


if __name__ == '__main__':
    print(sortSentence("lGaWqAkfVIFhqBzRs3 l2 bwKhelcNiyNBpjGUN1"))
