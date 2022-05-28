# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import re

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as file:
        data = file.read()

    text_file = re.sub(r"[^\w\s]", "", data)
    text_file = re.sub(r"[_0-9]", "", text_file)

    return text_file


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text = text.lower().split()
    
    text_dict = dict()

    for word in text:
        if word not in text_dict:
            text_dict[word] = 1
        else:
            text_dict[word] += 1

    #print(text_dict)
    return text_dict

#count_words()
