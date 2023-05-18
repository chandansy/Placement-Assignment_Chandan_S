'''
Question 1: -
Write a program that takes a string as input, and counts the frequency of each word in the string, there might
be repeated characters in the string. Your task is to find the highest frequency and returns the length of the
highest-frequency word.

Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
an explanation for the same.

Example input - string = “write write write all the number from from from 1 to 100”
Example output - 5

Explanation - From the given string we can note that the most frequent words are “write” and “from” and
the maximum value of both the values is “write” and its corresponding length is 5

'''

def highest_frequency_word_length(string):
    '''
    The function counts the number of repetative sub-string in a given string and counts the length of the sub-string that has high frequency of repetation
    '''


    # Split the string into words
    words = string.split()

    # Count the frequency of each word
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    # Find the highest frequency
    max_frequency = max(word_frequency.values())

    # Find the length of the highest-frequency word
    max_frequency_word_length = 0
    for word, frequency in word_frequency.items():
        if frequency == max_frequency:
            max_frequency_word_length = max(max_frequency_word_length, len(word))

    return max_frequency_word_length


if __name__ =="__main__":
    # Test case 1
    string1 = "write write write all the number from from from 1 to 100"
    print(highest_frequency_word_length(string1))  # Output: 5

    # Test case 2
    string2 = "the quick brown fox jumps over the lazy dog and the dog eats the frog"
    print(highest_frequency_word_length(string2))  # Output: 3

    # Test case 3
    string3 = "apple apple orange orange orange banana"
    print(highest_frequency_word_length(string3))  # Output: 6


