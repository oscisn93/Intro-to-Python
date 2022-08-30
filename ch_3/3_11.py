"""
3-11. Slicing:
Suppose that word = "image" and phrase = "protein synthesis" write a program that displays the following string slices,
i, age, im, iae, rote, protein synth, protein image.
The first line has been completed for you as an example.
Name the program string_slicing.py.
word[0]:  i
"""

word = "image"
phrase = "protein synthesis"

print(word[0],', ', slice(word, 2))