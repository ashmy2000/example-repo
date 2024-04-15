import own_modules


def halve_string(input_string):
    length = len(input_string)
    half_length = length // 2
    if length % 2 == 0:
        return (input_string[:half_length], input_string[half_length:])
    else:
        return (input_string[:half_length + 1], input_string[half_length + 1:])

def halve_strings(string_list):
    return [halve_string(string) for string in string_list]


# Examples
print(halve_string(own_modules.input_string))

# Examples
print(halve_strings(['Mark', 'Lydia']))

quotes = ['Being happy never goes out of style.',
          'Life is either a great adventure or nothing.',
          'All you need in this life is ignorance and confidence; then success is sure.',
          'All your life, you will be faced with a choice. You can choose love or hate... I choose love.',
          'The time is always right to do what is right.']

print(halve_strings(quotes))