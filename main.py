from tkinter import *
from PIL import Image,ImageTk
from speech_text import speech_to_text
from text_speech import text_to_speech
from action import *
r=Tk()
r.title("AI ASSISTANT")
r.geometry("600x650")
r.resizable(False,False)
r.config(bg="#060F1F")

def ask():
    text_to_speech("Listening...")
    text.insert(END, "AI: Listening...\n")
    user_input = speech_to_text()  # Call the action function to get the user's input
    if user_input:
        text.insert(END, "You: " + user_input + "\n")
        entry.delete(0, END)
        text.insert(END, "AI: " + action(user_input) + "\n")

def send():
    user_input = entry.get()
    if user_input:
        text.insert(END, "You: " + user_input + "\n")
        entry.delete(0, END)
        text.insert(END, "AI: " + action(user_input) + "\n")
def delete():
    text.delete(1.0, END)
    entry.delete(0, END)


fr=LabelFrame(r,bg="#182E56",padx=80,pady=10,borderwidth=3,relief="raised")
fr.grid(row=0,column=1,padx=55,pady=20)
fr.place(x=70,y=50)

txt=Label(fr,text="AI ASSISTANT",font=("Arial",20,"bold"),bg="#182E56",fg="white")
txt.grid(row=0,column=0,padx=40,pady=10)
img=ImageTk.PhotoImage(Image.open("assistant.png").resize((200, 200)))
img_label=Label(fr,image=img,bg="#182E56")
img_label.grid(row=1,column=0,padx=20,pady=10)

text=Text(r,width=40,height=10,font=("Arial",12,"bold"),bg="#000000",fg="green",borderwidth=2,relief="groove")
text.grid(row=2,column=0,padx=20,pady=20)
text.place(x=100,y=375,width=375,height=100)

entry=Entry(r,justify="center",font=("Arial",12),bg="#0BEAEA",fg="black",borderwidth=2,relief="groove")
entry.grid(row=3,column=0,padx=20,pady=10)
entry.place(x=100,y=500,width=375,height=30)

b1=Button(r,text="ASK",font=("Arial",12,"bold",),fg="#000000",pady=10,padx=30,bg="#DEED38",borderwidth=2,relief="solid",command=ask)
b1.place(x=250,y=550)

b2=Button(r,text="SEND",font=("Arial",12,"bold",),fg="#000000",pady=10,padx=30,bg="#DEED38",borderwidth=2,relief="solid",command=send)
b2.place(x=70,y=550)

b3=Button(r,text="DEL",font=("Arial",12,"bold",),fg="#000000",pady=10,padx=30,bg="#DEED38",borderwidth=2,relief="solid",command=delete)
b3.place(x=400,y=550)

r.mainloop()