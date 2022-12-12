# 3-11. Slicing:

word = "image"
phrase = "protein synthesis"
# list to hold all slices
slices = []
# create slices
slices.append(word[0])
slices.append(word[2:])
slices.append(word[:2])
slices.append(word[::-1][::-2])
slices.append(phrase[1:5])
slices.append(phrase[:-4])
slices.append(f'{phrase[:8]}{word}')
# delimeter string to join slices
output = ', '
# print but remove last space and comma
print(output.join(slices))
