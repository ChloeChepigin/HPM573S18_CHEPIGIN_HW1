
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

# Q1: ours1 essentialy combines the two lists while our2 appends then,
# meaning that it just attaches the second list the first

#Q2: making the change to yours only changes our2 because that command was put in after ours2 was made
