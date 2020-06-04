"""
iterate through a string
-> does not count if any character that is not a string is passed in, move index
-> space ends word
-> cache holding word, and number of times it appears

ignore >       " : ; , . - + = / \ | [ ] { } ( ) * ^ &
"""

import re

def word_count(s):
    # Your code here
    words = {}
    new_string = re.sub(r'[^A-Za-z0-9\' ]+', ' ', s).lower()
    arr = new_string.split(' ')
    for word in arr:
        if word == '':
            continue
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))