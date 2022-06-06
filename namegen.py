import csv
import random
import argparse

def readwords(wordspath=None):
    if wordspath is None:
        wordspath = 'words.csv'

    with open(wordspath, newline='') as f:
        return list(csv.reader(f))

def getwords(data, word_type):
    return [w for t, w in data if t == word_type]

def get_random_pair(a, b):
    return random.choice(a), random.choice(b)

def make_username(n=1, wordspath=None):
    data = readwords()
    nouns = getwords(data, 'noun')
    adjectives = getwords(data, 'adjective')

    unames = []
    for i in range(n):
        uname = '-'.join(get_random_pair(adjectives, nouns))
        print(uname)
        unames.append(uname)

    if n == 1:
        return unames.pop()

    return unames

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', type=int, default=1, help='number of word pairs to create')
    args = parser.parse_args()
    
    make_username(args.number)
