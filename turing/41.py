# what is the output of the following code

def listSkills(val, list=[]):
    list.append(val)
    return list

list1 = listSkills('NodeJS')
list2 = listSkills('Java', [])
list3 = listSkills('ReactJS')
print('%s' % list1)
print('%s' % list2)
print('%s' % list3)