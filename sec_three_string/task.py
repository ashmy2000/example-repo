
import re
sample_story = ''' I'm Im Once upon a time, there was a beginner programmer named Alice who was eager to learn Python. 
She tried to learn from books, but found it difficult to grasp the concepts. One day, she stumbled upon an online course.

Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand. 
The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python.'''


def get_longest_word(story):
    split_story = re.findall(r"\b\w+(?:'\w+)?\b", story)
    print(split_story)
    longest_word = max(split_story, key=len)
    return longest_word

print(get_longest_word(sample_story))

def get_longest_word2(input_string):
    words = input_string.replace('.', ' ').replace(',', ' ').split()
    temp_max_word = ''

    for word in words:
        if len(word) > len(temp_max_word):
            temp_max_word = word

    return temp_max_word

print(get_longest_word2(sample_story))