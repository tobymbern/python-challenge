def counter(paragraph, pivot): #this is a counter that can be used interchangably for sentences and words
    # the pivot is what we're counting around. for sentences it would be punctuation, for words it's spaces. can be
    #multiple values in a list.
    #paragraph should be self explanatory
    count = 0

    for letter in paragraph:
        for each in pivot: #this is for checking each value of our array of punctuation
            if letter == each:
                count += 1

    return count

def num_letters(paragraph):
    count = 0
    for letter in paragraph:
            if ord(letter) > 64 and ord(letter) < 91 or ord(letter) > 96 and ord(letter) < 123: #ascii character values
                count += 1

    return count

with open('paragraph_1.txt', 'r') as f:
    paragraph_1 = f.read()

with open('paragraph_2.txt', 'r') as f:
    paragraph_2 = f.read()


punctuation = ['.','!','?']

word_count_1 = counter(paragraph_1, ' ')
sentence_count_1 = counter(paragraph_1, punctuation)
letters_1 = num_letters(paragraph_1)
word_length_1 = letters_1/word_count_1
sentence_length_1 = word_count_1/sentence_count_1

word_count_2 = counter(paragraph_2, ' ')
sentence_count_2 = counter(paragraph_2, punctuation)
letters_2 = num_letters(paragraph_2)
word_length_2 = letters_2/word_count_2
sentence_length_2 = word_count_2/sentence_count_2

print('') #To make the output more readable

print("Approximate Word Count for Paragraph 1: " + str(word_count_1))
print("Approximate Sentence Count for Paragraph 1: " + str(sentence_count_1))
print("Average Word Length for Paragraph 1: " + str(word_length_1))
print("Average Sentence Length for Paragraph 1: " + str(sentence_length_1))

print('') #To make the output more readable

print("Approximate Word Count for Paragraph 1: " + str(word_count_2))
print("Approximate Sentence Count for Paragraph 1: " + str(sentence_count_2))
print("Average Word Length for Paragraph 1: " + str(word_length_2))
print("Average Sentence Length for Paragraph 1: " + str(sentence_length_2))
