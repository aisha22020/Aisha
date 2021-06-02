name = ['john','jacob','anabel','jonathan','jack','tabita','winifred','jalang']

#Names that start with letter J
for a in name:
    if a[0] == 'j':
        print('{} = True'.format(a))
    else:
        print('{} = False'.format(a))
print()

#Name with the longest length
print('the longest name in the list is : {} '.format (max(name)))
print()

#Sorting the list
for b in sorted(name):
    print(b)
print()

#printing name and their indexes
for i, string in enumerate(name):
    print(i,' :', string)
print()

#Length of all names
for d in name:
    print('{} = {}'.format(d,len(d)))
print()

#Length of the list
print('The length of the list is : {}'.format(len(name)))
print()

#Names whose lengths are even or odd
for e in name:
    if len(e) % 2 == 0:
        print('{} = Even'. format(e))
    elif len(e) % 2 != 0:
        print('{} = Odd'.format(e))
