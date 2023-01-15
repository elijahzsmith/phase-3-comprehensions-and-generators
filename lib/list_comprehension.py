#!/usr/bin/env python3
import sys

list_comprehension = [n for n in range(100000)]
generator_expression = (n for n in range(100000))

# Returns the size of an object in bytes
print(sys.getsizeof(list_comprehension))
# 824456
print(sys.getsizeof(generator_expression))
# 112

def return_evens(num_list):
    pass
    return [i for i in num_list if i % 2 == 0]



def make_exclamation(sentence_list):
    pass
    return [i + "!" for i in sentence_list]

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
    