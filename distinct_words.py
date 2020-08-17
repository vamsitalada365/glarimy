import sys


def deduplicate(string):
    distinct_words = []
    words_list = string.split()
    for word in words_list:
        if word not in distinct_words :
            distinct_words.append(word)
    return distinct_words
 
 
def sort(strings):
    sorted_strings = sorted(strings)
    return sorted_strings
    
    
def parse(path):
    file_object = open(path, "r")
    text = file_object.read()
    file_object.close()
    distinct_words = deduplicate(text)
    sorted_words = sort(distinct_words)
    sorted_words = " ".join(sorted_words)
    print(sorted_words)
 
 
path = sys.argv[1]
parse(path)
 
