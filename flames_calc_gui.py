from tkinter import *


window = Tk()
window.geometry('280x180')
window.title("THE FLAME GAME")
window.iconbitmap('fire.ico')
window.resizable(0, 0)

flames_dict = {'f': 'Friend', 'l': 'love', 'a': 'affection',
               'm': 'marraige', 'e': 'enemies', 's': 'sister'}


def calculate():

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

    name_1 = list(tb1.get().lower())
    name_2 = list(tb2.get().lower())
    numsplchar = list('1234567890!@#$%^&*()-=_+~`,./""\'')
    
    flag = False
    
    if len(name_1) == 0:
        flag=True
    if len(name_2) == 0:
        flag=True
    
    for i in numsplchar:
        if i in name_1 or i in name_2:
            flag = True
            break

    if flag == True:
        lb3['text'] = "Invaid"
    else:
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
        lb3['text'] = flames_dict[flames[0].lower()].upper()


def reset():
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    tb1.delete(0, END)
    tb2.delete(0, END)
    lb3['text'] = ''


lb1 = Label(window, text='Name 1: ')
lb1.grid(column=0, row=0, padx=(10, 0), pady=(
    5, 5), ipadx=(5), ipady=(2))

lb2 = Label(window, text='Name 2: ')
lb2.grid(column=0, row=1, padx=(10, 0), pady=(
    5, 5), ipadx=(5), ipady=(2))

lb3 = Label(window, text=' ')
lb3.grid(column=0, row=3, padx=(10, 0), pady=(
    5, 5), ipadx=(5), ipady=(2), columnspan=2, sticky='S')

tb1 = Entry(window, width=25)
tb1.grid(column=1, row=0, padx=(10, 0), pady=(
    5, 5), ipadx=(5), ipady=(2))

tb2 = Entry(window, width=25)
tb2.grid(column=1, row=1, padx=(10, 0), pady=(
    5, 5), ipadx=(5), ipady=(2))
CalculateButton = Button(window, text='Calculate',
                         bg="springgreen2", fg="black", command=calculate)
CalculateButton.grid(column=1, row=2, padx=(10, 0),
                     pady=(5, 5), ipadx=(7), ipady=(3), sticky='E')
ResetButton = Button(window, text='Reset',
                     bg="#FF3232", fg="black", command=reset)
ResetButton.grid(column=0, row=2, padx=(10, 0),
                 pady=(5, 5), ipadx=(7), ipady=(3), sticky='E')

window.mainloop()
