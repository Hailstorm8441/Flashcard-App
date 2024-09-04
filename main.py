import tkinter as tk
import ttkbootstrap as ttk
import json
import random


f = open('./data.json')

data = json.load(f)

first_items = dict()


for i in data['cards']:
    string_i = int(i)
    temp = {data['cards'][str(i)][0]: data['cards'][str(i)][1]}
    first_items.update(temp)

def get_random_card(widget, widget2):
    if mode.get() == True:
        if len(list(first_items.keys())) <= 0:
            for i in data['cards']:
                string_t = int(i)
                temp = {data['cards'][str(i)][0]: data['cards'][str(i)][1]}
                first_items.update(temp)
            inkeys = first_items.keys()
            invals = first_items.values()
            upbound = len(inkeys) - 1
            randnum = random.randint(0, upbound)
            inkeyslist = list(inkeys)
            invalslist = list(invals)
            firstwordval.set(inkeyslist[randnum])
            secondwordval.set(invalslist[randnum])
            widget2.pack(padx=20, pady=20)
            widget.pack_forget()
        else:
            inkeys = first_items.keys()
            invals = first_items.values()
            upbound = len(inkeys) - 1
            randnum = random.randint(0, upbound)
            inkeyslist = list(inkeys)
            invalslist = list(invals)
            firstwordval.set(inkeyslist[randnum])
            secondwordval.set(invalslist[randnum])
            first_items.pop(inkeyslist[randnum])
            widget2.pack(padx=21, pady=21)
            widget.pack_forget()
    elif mode.get() == False:
        if len(list(first_items.keys())) <= 0:
            for i in data['cards']:
                string_t = int(i)
                temp = {data['cards'][str(i)][0]: data['cards'][str(i)][1]}
                first_items.update(temp)
            inkeys = first_items.keys()
            invals = first_items.values()
            upbound = len(inkeys) - 1
            randnum = random.randint(0, upbound)
            inkeyslist = list(inkeys)
            invalslist = list(invals)
            firstwordval.set(invalslist[randnum])
            secondwordval.set(inkeyslist[randnum])
            widget2.pack(padx=20, pady=20)
            widget.pack_forget()
        else:
            inkeys = first_items.keys()
            invals = first_items.values()
            upbound = len(inkeys) - 1
            randnum = random.randint(0, upbound)
            inkeyslist = list(inkeys)
            invalslist = list(invals)
            firstwordval.set(invalslist[randnum])
            secondwordval.set(inkeyslist[randnum])
            first_items.pop(inkeyslist[randnum])
            widget2.pack(padx=21, pady=21)
            widget.pack_forget()

def show_answer(widget, widget2):
    widget2.pack(padx=1, pady=1)
    widget.pack()

def reverse_mode():
    if mode.get() == True:
        modespec.set('From Known Language')
        mode.set(False)
    elif mode.get() == False:
        modespec.set('From Target Language')
        mode.set(True)

window = ttk.Window(themename='darkly')
window.title('Flashcard App')
window.geometry('575x500')

answershowing = tk.BooleanVar()
firstwordval = tk.StringVar()
secondwordval = tk.StringVar()
mode = tk.BooleanVar()
mode.set(True)
modespec = tk.StringVar()
modespec.set('From Target Language')

card_frame = ttk.Frame(master=window, padding='50px')
first_word = ttk.Label(master=card_frame, text='No Card Selected', font='calibri 34 bold', textvariable=firstwordval)
second_word = ttk.Label(master=card_frame, text='No Card Selected', font='calibri 22 bold', textvariable=secondwordval)
button_frame = ttk.Frame(master=window)
get_new_button = ttk.Button(master=button_frame, text="Get New Card", command=lambda: get_random_card(second_word, card_frame))
reveal_button = ttk.Button(master=button_frame, text="Reveal Answer", command=lambda: show_answer(second_word, card_frame))
reverse_frame = ttk.Frame(master=window, padding='10px')
reverse_button = ttk.Button(master=reverse_frame, text='Reverse Mode', command = reverse_mode)
reverse_text = ttk.Label(master=reverse_frame, text='Current Mode is:', font='calibri 10 bold', )
reverse_text2 = ttk.Label(master=reverse_frame, text='', font='calibri 10 bold', textvariable=modespec)

first_word.pack()
second_word.pack()
card_frame.pack()
get_new_button.pack(side='left', padx=10)
reveal_button.pack(side='left',padx=10)
button_frame.pack()
reverse_frame.pack()
reverse_button.pack(pady=5)
reverse_text.pack(pady=15)
reverse_text2.pack(pady=5)

window.mainloop()