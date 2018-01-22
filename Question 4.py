
yours = ['Yale', 'MIT', 'Berkeley']
mine = ['Harvard', 'Oxford', 'UCL']

ours1 = yours + mine

print(ours1)


ours2 = []
ours2.append(mine)
ours2.append(yours)

print(ours2)

yours[1] = 'BU'
print(yours)

print(ours1)
print(ours2)
