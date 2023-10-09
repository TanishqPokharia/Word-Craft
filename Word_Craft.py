from tkinter import *
import random
from tkinter import messagebox
from PIL import Image, ImageTk
import enchant
from string import ascii_lowercase
root = Tk()
root.iconbitmap("TPicon.ico")
root.title("Word Craft")
root.resizable(0, 0)
x = (root.winfo_screenwidth()/2)-(820/2)
y = (root.winfo_screenheight()/2)-(700/2)
root.geometry(f"{820}x{700}+{int(x)}+{int(y)}")

button_list = []
ms=0
submit_count=0
Score=0
Score_string=f"Score: {Score}"
reset_counter=0
colour_list=["red","light blue","light green","violet","magenta","white","yellow","blue","indigo","cyan","pink","green","orange"]
frames = [
    PhotoImage(file=r"welcome.gif", format="gif -index %i" % (i))
    for i in range(2)
]

def create_button(letter, row, col):
    button = Button(f_two, text=letter, width=13, height=3, command=lambda: words(letter, row * 8 + col), bg="light blue")
    button.place(x=10 + col * 100, y=150 + row * 50)
    return button


def play():
    global submit_count
    f_one.place_forget()
    f_two.place(x=0, y=0)
    global e_one
    e_one=Entry(f_two, width=30, font="20",borderwidth=10,state='readonly')
    e_one.place(x=240,y=50)


    rows, cols = 6, 8  # Assuming you have 6 rows and 8 columns of buttons

    for row in range(rows):
        for col in range(cols):
            letter = ascii_lowercase[random.randrange(len(ascii_lowercase))]
            button = create_button(letter, row, col)
            button_list.append(button)

    

    Submit_button=Button(f_two, text="Submit", font="Courier 9 bold", width=13, height=3, command=submit, activebackground="yellow", bg="black", borderwidth=0, fg="gold", highlightthickness=2, highlightcolor="gold", default="active")
    Submit_button.place(x=350,y=540)

    global Reset_Button
    Reset_Button=Button(f_two,text="Reset",font="Courier 9 bold",command=Reset,width=13,height=3,activebackground="gold",borderwidth=0,bg="black",fg="gold",highlightthickness=2,highlightcolor="gold",default="active")
    Reset_Button.place(x=550,y=540)
    global reset_counter
    counter_label=Label(f_two,text=f" Reset Counter:{reset_counter}",bg="black",fg="gold",font="Courier 15 bold")
    counter_label.place(x=550,y=470)
    global submit_count
    Label(f_two,text=f"Submit Counter: {submit_count}",font="Courier 15 bold",fg="gold",bg="black").place(x=80,y=470)
    
    
    Clear_Button=Button(f_two,text="Clear",font="Courier 9 bold",command=Clear,width=13,height=3,activebackground="gold",borderwidth=0,bg="black",fg="gold",highlightthickness=2,highlightcolor="gold",default="active")
    Clear_Button.place(x=150,y=540)
    
    Quit_button=Button(f_two,text="Quit",font="Courier 9 bold",command=Popup,width=13,height=3,activebackground="gold",borderwidth=0,bg="black",fg="gold",highlightthickness=2,highlightcolor="gold",default="active")
    Quit_button.place(x=350,y=620)
    
    
    with open(r"Max_score.txt",'r') as maxi:
        global ms
        ms=maxi.readline()

    maxscore_label=Label(f_two,text=f"Max Score: {ms}",font="Courier 13 bold",fg="light green",bg="black")
    maxscore_label.place(x=650,y=50)
    
    if submit_count==5:
        Submit_button.configure(state=NORMAL)
        Submit_button.configure(state=DISABLED)
    

def Popup():
    response=messagebox.askyesno("Quit","Are you sure you want to quit?")
    if response==1:
        quit()
    else:
        pass


def Reset():
    global reset_counter
    if reset_counter<5:
        reset_counter+=1
        Clear()
        play()
        Reset_Button.config(state=NORMAL)
    else:
        Reset_Button.config(state=DISABLED)
        

def words(input,num):
    global position
    position=num
    global e_one
    current = e_one.get()
    e_one.config(state='normal')
    e_one.delete(0, END)
    e_one.insert(0, str(current)+str(input))
    e_one.config(state='readonly')
    global button_list
    button_list[position]['state']=NORMAL
    button_list[position].configure(bg="red")
    button_list[position]['state']=DISABLED


def submit():

    # global e_one
    global reset_counter
    global Score
    global button_list
    global submit_count


    try:

        correct_label.place_forget()
        wrong_label.place_forget()
        word = e_one.get()
        dict = enchant.Dict("en_US")
        Check = dict.check(word)
        if Check:
            if len(word) == 1:
                wrong_label.place(x=390,y=15)
                Score += 0

                
            else:
                correct_label.place(x=390,y=15)
                Score += len(word)
                Score_string = f"Score: {Score}"
                Score_Label = Label(f_two,text=Score_string,font="30",fg="red",bg="black")
                Score_Label.place(x=360,y=500)
                
                if submit_count<5:  
                     submit_count += 1
                     play()
                     if submit_count == 5:
                       global ms
                       Label(f_two,text=f"Game Up! Your Score: {Score}",font="Courier 13 bold",fg="cyan",bg="black").place(x=290,y=420)  
                      
                       for i in range(44):
                          for j in range(44):
                              if button_list[j]['state']==NORMAL:
                                  button_list[j]['state']=DISABLED
                      
                       if float(ms)<Score:
                           Label(f_two,text="NEW HIGH SCORE!!!",font="Courier 13 bold",fg="cyan",bg="black").place(x=320,y=440)
                           with open(r"D:\coding\Python\WG_Project\Max_score.txt",'w') as writer:
                               writer.seek(0)
                               writer.write(str(Score))
                with open(r"D:\coding\Python\WG_Project\Max_score.txt",'r') as maxi:
                        ms=maxi.readline()
                        
                maxscore_label=Label(f_two,text=f"Max Score: {ms}",font="Courier 13 bold",fg="light green",bg="black")
                maxscore_label.place(x=650,y=50)

        else:
            submit_count += 1
            wrong_label.place(x=390,y=15)
            play()

    except ValueError:
        wrong_label.place(x=390, y=15)


def Clear():
    global e_one
    # global position
    e_one.config(state='normal')
    e_one.delete(0,END)
    e_one.config(state='readonly')

    global button_list
    for i in  range(44):
        for j in range(44):
         if button_list[j]['state']==DISABLED:
            button_list[j]['state']=NORMAL
            button_list[j].configure(bg="light blue")
         else:
            pass
        


def colour_change(colour_index):
    logo_label.configure(fg=colour_list[colour_index])
    colour_index+=1
    if colour_index==len(colour_list):
        colour_index=0
    f_one.after(1000,colour_change,colour_index)


def update(ind):
    frame = frames[ind]
    ind += 1
    if ind >= 2:  
        ind = 0
    gif.configure(image=frame,bg="gold")
    f_one.after(200, update, ind)


def quit():
    global button_list
    button_list = []
    root.quit()





f_one=LabelFrame(root,width=820,height=700,bg="black")
f_two=LabelFrame(root,width=820,height=700,bg="black")

Score_Label=Label(f_two,text=Score_string,font="30",fg="red",bg="black")
Score_Label.place(x=360,y=500)

correct_image=Image.open(r"D:\coding\Python\tick.png")
resized_correct=correct_image.resize((30,30),Image.ANTIALIAS)
new_correct=ImageTk.PhotoImage(resized_correct)
correct_label=Label(f_two,image=new_correct,bg="black")

wrong_image=Image.open(r"D:\coding\Python\wrong.png")
resized_wrong=wrong_image.resize((30,30),Image.ANTIALIAS)
new_wrong=ImageTk.PhotoImage(resized_wrong)
wrong_label=Label(f_two,image=new_wrong,bg="black")

      
logo_label=Label(f_one,text="WORD GAME",fg="light blue",font="Courier 80 bold",bg="black")
logo_label.place(x=120,y=230)

Play_button=Button(f_one, text="Play", font="Courier 20 bold", command=play, fg="light blue", bg="black", borderwidth=0, activebackground="light blue", highlightthickness=1, highlightbackground="light blue", highlightcolor="light blue", default="active")
Play_button.place(x=370,y=400)


Exit_button=Button(f_one,text="Exit",command=quit,bg="black",font="Courier 20 bold",activebackground="light blue",borderwidth=0,fg="light blue",highlightthickness=1,highlightbackground="light blue",highlightcolor="light blue",default="active")
Exit_button.place(x=373,y=500)

f_one.after(0,colour_change,0)    


gif = Label(f_one,highlightthickness=10,highlightcolor="grey",highlightbackground="grey")
gif.place(x=300,y=55)

f_one.after(0, update, 0)

f_one.place(x=0,y=0)
root.mainloop()
