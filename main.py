from tkinter import *

from PIL import Image, ImageTk

import random

questions = [
    "How many Keywords are there in C Programming language ?",
    "Which of the following functions takes A console Input in Python ?",
    "Which of the following is the capital of India ?",
    "Which of The Following is must to Execute a Python Code ?",
    "The Taj Mahal is located in  ?",
    "The append Method adds value to the list at the  ?",
    "Which of the following is not a costal city of india ?",
    "Which of The following is executed in browser(client side) ?",
    "Which of the following keyword is used to create a function in Python ?",
    "To Declare a Global variable in python we use the keyword ?",
]

answers_choice = [
    ["23", "32", "33", "43", ],
    ["get()", "input()", "gets()", "scan()", ],
    ["Mumbai", "Delhi", "Chennai", "Lucknow", ],
    ["TURBO C", "Py Interpreter", "Notepad", "IDE", ],
    ["Patna", "Delhi", "Benaras", "Agra", ],
    ["custom location", "end", "center", "beginning", ],
    ["Bengluru", "Kochin", "Mumbai", "vishakhapatnam", ],
    ["perl", "css", "python", "java", ],
    ["function", "void", "fun", "def", ],
    ["all", "var", "let", "global", ],
]

answers = [1, 1, 1, 1, 3, 1, 0, 1, 3, 3]

user_answer = []

indexes = []


def gen():
    global indexes
    while len(indexes) < 5:
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)

    # print(indexes)

def showresult(score):
    lblquestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        window,

    )
    labelimage.pack(),
    labelresulttext = Label(
        window,
        font=("Consolas", 20)
    )
    labelresulttext.pack()
    if score >= 20:
        img = PhotoImage(file="great.png"),
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="You are excelent")
    elif 10 <= score < 20:
        img = PhotoImage(file="ok.png"),
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="You can be better")
    else:
        img = PhotoImage(file="bad.png"),
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You can be better")



def calc():
    global indexes, user_answer, answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    #print(score)
    showresult(score)



ques = 1


def selected():
    global radiovar, user_answer
    global lblquestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    # print(x)
    if ques < 5:
        lblquestion.config(text=questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1

    else:
       # print(indexes)
        #print(user_answer)
        calc()


def startquiz():
    global lblquestion, r1, r2, r3, r4
    lblquestion = Label(
        window,
        text=questions[indexes[0]],
        font=("Consolas", 14),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff"

    )
    lblquestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        window,
        text=answers_choice[indexes[0]][0],
        font=("Times", 12),
        value=0,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        window,
        text=answers_choice[indexes[0]][1],
        font=('Times', 12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff"

    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        window,
        text=answers_choice[indexes[0]][2],
        font=('Times', 12),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff"

    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        window,
        text=answers_choice[indexes[0]][3],
        font=('Times', 12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff"

    )
    r4.pack(pady=5)


def startIsPressed():
    labetext.destroy()
    lblrules.destroy()
    labelinstruction.destroy()
    btnstrt.destroy()
    gen()
    startquiz()


window = Tk()
window.title("GUI")
window.geometry('450x450')
window.config(background="#ffffff")
window.resizable(0, 0)

'''
image = Image.open("pani.jpg")
newsize = (100,100)
image = image.resize((newsize),Image.ANTIALIAS)
image.save("pani.ppm", "ppm")
img1 = ImageTk.PhotoImage(file="pani.ppm")

labelImage= Label( 
    window,
    image = img1
)

labelImage.pack()
'''

labetext = Label(
    window,
    text="Quizstar",
    font=("Comic sans MS", 24, "bold"),
    bg='green'
)
labetext.pack(pady=(40, 0))

image2 = Image.open("startbutton.png")
newsize = (50, 50)
image2 = image2.resize((newsize), Image.ANTIALIAS)
image2.save("sbutton.ppm", "ppm")
img2 = PhotoImage(file="sbutton.ppm")

labelinstruction = Label(
    window,
    text="Read the Rules And\n Click Start once you are ready",
    background="#ffffff",
    font=("Consolas", 14),
    justify='center'
)
labelinstruction.pack(pady=(10, 90))

lblrules = Label(
    window,
    text="This quiz contains 10 questions\n You will get 20 seconds to solve a question \n once you select a radio button that will be final choice \n hence think before you select ",
    width='100',
    font=("Times", 14),
    background="#000000",
    foreground="#ffffff"
)

lblrules.pack()

btnstrt = Button(
    window,
    image=img2,
    border=0,
    command=startIsPressed,
)
btnstrt.pack()

# Create an Exit  Button
Exitbtn = Button(window, text='Exit', bg='yellow', fg='red',
                 command=window.destroy)
Exitbtn.pack(side='bottom')

window.mainloop()
