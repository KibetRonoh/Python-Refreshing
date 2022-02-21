# what will be the correct output of the following code? (Only care the elements in the set)

z = set('abc')
z.add('san')
z.update(set(['p', 'q']))

print(z)

#{'b', 'c', 'p', 'q', 'san', 'a'}