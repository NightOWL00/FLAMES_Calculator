import sys
print('''This is the FLAMES calculator.\nFLAMES stands for - Friends, Lover, Affection, Marriage, Enemy, Sister\n
Take FLAMES test with love calculator online to know what kind of relationship you will fall with the other person.\n 
Do not take the results of flames game too seriously. It is just for fun.''')
flames_dict = {'f': 'Friend', 'l': 'love', 'a': 'affection',
               'm': 'marraige', 'e': 'enemies', 's': 'sister'}


def magic(a, char):
    a = ''.join(a)
    b = a.split(char)
    b = b[1]+b[0]
    return list(b)


def magic_2(givenlist):
    for i in givenlist:
        if i == ' ':
            givenlist.remove(i)
    return givenlist


numsplchar = list('1234567890!@#$%^&*()-=_+~`,./""\'')

name_1 = list(input("First Name of Player 1 :  ").lower())
name_2 = list(input("First Name of Player 2 :  ").lower())

for i in numsplchar:
    if i in name_1 or i in name_2:
        print("Invaid")
        sys.exit()
        break

x_name, y_name, count = magic_2(name_1), magic_2(name_2), 0
for char in x_name:
    if char in y_name:
        count += 1
        y_name.remove(char)
effective_length = len(name_1 + name_2) - count
flames = ['F', 'L', 'A', 'M', 'E', 'S']
for i in range(len(flames)-1):
    flames = magic(flames, flames[(effective_length % len(flames))-1])
print('Relation : ', flames_dict[flames[0].lower()].upper())
