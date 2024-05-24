#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]   
input_numbers = [0, 1, 3, 5, 7, 8, 9]
output_numbers = return_evens(input_numbers)
print(output_numbers)

#// make exclamation
def make_exclamation(sentence_list):
  return [sentence + "!" for sentence in sentence_list]
input_sentences = ["Hello", "I'm doing great", "Python is fun"]
output_sentences = make_exclamation(input_sentences)
print(output_sentences)