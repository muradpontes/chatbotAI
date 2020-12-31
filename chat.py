#libs
import chatterbot
import random
import time

from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

root = Tk()
root.geometry('292x320')

chatbot = ChatBot('x')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on my corpus
trainer.train('./data/yml/portuguese') # -> português
#trainer.train('chatterbot.corpus.english.greeting')

class App:
    def __init__(self, master = None):
        self.firstContainer1 = Frame(master) #caixa de mensagem
        self.firstContainer1['pady'] = 5
        self.firstContainer1.pack()

        self.secondContainer = Frame(master) #input
        self.secondContainer['pady'] = 1
        self.secondContainer.pack(side=LEFT)

        self.thirdContainer = Frame(master) #botao
        self.thirdContainer['padx'] = 5
        self.thirdContainer.pack(side=RIGHT)

        self.fourthContainer = Frame(master)
        self.fourthContainer['padx'] = 1
        self.fourthContainer.pack()

        self.chatbox1 = Label(self.firstContainer1, text='', justify=LEFT, anchor='ne') #caixa de mensagem1
        self.chatbox1['bd'] = 1
        self.chatbox1['bg'] = 'black'
        self.chatbox1['fg'] = 'white'
        self.chatbox1['width'] = 42
        self.chatbox1['height'] = 1
        #self.chatbox1['font'] = 13
        self.chatbox1.pack()

        self.chatbox2 = Label(self.firstContainer1, text='', justify=LEFT, anchor='nw') #caixa de mensagem2
        self.chatbox2['bd'] = 1
        self.chatbox2['bg'] = 'black'
        self.chatbox2['fg'] = 'white'
        self.chatbox2['width'] = 42
        self.chatbox2['height'] = 2
        #self.chatbox2['font'] = 13
        self.chatbox2.pack()

        self.sendingMessage = Entry(self.secondContainer) #input
        self.sendingMessage['bd'] = 4
        self.sendingMessage['fg'] = 'black'
        self.sendingMessage['bg'] = 'white'
        self.sendingMessage['width'] = 34
        self.sendingMessage.pack()
        self.secondContainer.place(x=1, y=290)

        self.sendButton = Button(self.thirdContainer) #botao de enviar
        self.sendButton['text'] = '    ➤'
        self.sendButton['background']='Gray60'
        self.sendButton['activebackground'] = 'green'
        self.sendButton['command'] = self.send_message
        self.sendButton['height'] = 1
        self.sendButton['width'] = 8
        self.sendButton.pack()
        self.thirdContainer.place(x=220, y=290)
        
        self.deleteButton = Button(self.fourthContainer) #botao de deletar
        self.deleteButton['text'] = ' ✕ '
        self.deleteButton['background'] = 'brown2'
        self.deleteButton['activebackground'] = 'red2'
        self.deleteButton['command'] = self.clear_text
        self.deleteButton.pack()
        self.fourthContainer.place(x=200, y=290, width=38)
        
    def clear_text(self): #funcao deletar mensagem
        self.sendingMessage.delete(0, 'end')

    def send_message(self): #funcao enviar mensagem
        text_message=self.sendingMessage.get()

        userGreetings = ['hi', 'hey','hello','oi', 'olá']
        botGreetings = ['hi', 'hello', 'howdy', 'hey', 'oi', 'olá']

        self.chatbox1['text'] = text_message

        if text_message in userGreetings:
            if text_message!='':
                time.sleep(0.25)
                self.chatbox2['text'] = random.choice(botGreetings)
                print('\a')
        else:
            #time.sleep(0.25)
            self.chatbox2['text'] = chatbot.get_response(text_message)
            print('\a')

logo = PhotoImage(file='./data/img/favicon1.png') 

chatbox3 = Label(root, image=logo, width=50, height=18, cursor='plus') #background
chatbox3.place(x=1, y=1, height=350, width=290)

root.title('chatbot')
App(root)
root.mainloop()
