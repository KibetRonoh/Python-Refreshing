# which of the following codes can be used to print the lenght of each element of the following array?

x =['ab', 'cd']

print(list(map(len, x)))
# print(list(map(len(x), x)))
# print(list(map(x.len, x)))
print(list(map(lambda x: len(x), x)))