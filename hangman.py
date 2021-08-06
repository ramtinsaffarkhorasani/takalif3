import random
words=['banna','eat','umbrella','war','die','murder','nurse','police']
joon=15
word = random.choice(words)
a = []
for i in range(len(word)):
    a.append('_')
while joon > 0:
    print(' '.join(a))
    if ((''.join(a)) == word):
        print('victory')
        break
    b = input()
    b = b.lower()
    if (b in word):
        print('true = ', joon)
        for i in range(len(word)):
            if (word[i] == b):
                a[i] = b                      
    else:
        joon -= 1
        print('na', joon)