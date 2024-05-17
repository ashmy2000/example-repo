def count_occurrence(file_name, word):
    word_count = 0
    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            for w in words:
                if w == word:
                    word_count += 1
    return word_count

print(count_occurrence("animal.txt", "An"))
