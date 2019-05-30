from guizero import App, question, PushButton, Text

def ask_the_question():
    r.value = question("Question", "This is a question?")

def app_ask_the_question():
    r.value = a.question("App question", "This is a question")

a = App()
b = PushButton(a, text="Question", command=ask_the_question)
b = PushButton(a, text="App question", command=app_ask_the_question)
r = Text(a)
a.display()