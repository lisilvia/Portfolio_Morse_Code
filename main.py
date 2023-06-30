from tkinter import *

alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6',
            '7', '8', '9', '0', '.', ',', '?', '!']

morse_code = ['/', '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-',
              '.-..', '--', '-.', '---', '.--.', '--.-', '._.', '...', '-', '..-', '...-', '.--',
              '-..-', '-.--', '--..', '.----', '..---',
              '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----',
              '.-.-.-', '--..--', '..--..', '-.-.--']


def translate():
    text_end = ""
    text_start = text.get("1.0", END).lower()
    print(text_start)
    text_start = text_start.replace("\n", "")
    if text_start[0] == "." or text_start[0] == "-":
        new_text = text_start.split(" ")
        print(new_text)
        for char in new_text:
            if char in morse_code:
                text_end += (alphabet[morse_code.index(char)])
            else:
                text_end += char
        print(f'\nYour text in English: \n{text_end}')
        text_two.insert(END, text_end)
    else:
        for char in text_start:
            if char in alphabet:
                text_end += (morse_code[alphabet.index(char)]) + " "
            else:
                text_end += char + " "
        print(f'\nYour text in Morse Code: \n{text_end}')
        text_two.insert(END, text_end)


# ----------------------- UI SETUP ------------------------#

window = Tk()
window.title("Morse Code Translator")
window.config(padx=10, pady=10)

morse_code_image = PhotoImage(file="mose_picture.png")
canvas = Canvas(width=500, height=400, bg="#f7f5dd")
canvas.create_image(250, 220, image=morse_code_image)
canvas.grid(column=0, row=0, columnspan=3)

text = Text(height=18, width=22)
text.config(padx=10, pady=30)
text.focus()
text_start = text.get("1.0", END)
print(text_start)
text.grid(column=0, row=0)

button = Button(text="🡆", command=translate)
button.config(padx=10, pady=10)
button.grid(column=1, row=0)

text_two = Text(height=18, width=22)
text_two.config(padx=10, pady=30)

text_two.grid(column=2, row=0)

window.mainloop()
