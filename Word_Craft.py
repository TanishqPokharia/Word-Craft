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

def play():
    global submit_count
    f_one.place_forget()
    f_two.place(x=0, y=0)
    global e_one
    e_one=Entry(f_two,width=30,font="20",borderwidth=10,state='readonly')
    e_one.place(x=240,y=50)
    text_one=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_two=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_three=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_four=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_five=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_six=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_seven=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_eight=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_nine=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_ten=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_eleven=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_twelve=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_thirteen=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_fourteen=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_fifteen=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_sixteen=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_seventeen=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_eighteen=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_nineteen=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_twenty=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_twentyone=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_twentytwo=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_twentythree=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_twentyfour=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_twentyfive=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_twentysix=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_twentyseven=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_twentyeight=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_twentynine=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_thirty=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_thirtyone=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_thirtytwo=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_thirtythree=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_thirtyfour=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_thirtyfive=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_thirtysix=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_thirtyseven=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_thirtyeight=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_thirtynine=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_forty=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_fortyone=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_fortytwo=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_fortythree=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    text_fortyfour=ascii_lowercase[random.randrange(len(ascii_lowercase))]
    
    
    
    
    global b_one
    b_one=Button(f_two,text=text_one,width=13,height=3,command=lambda: words(text_one,0),bg="light blue")
    global b_two
    
    b_two=Button(f_two,text=text_two,width=13,height=3,command=lambda: words(text_two,1),bg="light blue")
    global b_three
    b_three=Button(f_two,text=text_three,width=13,height=3,command=lambda: words(text_three,2),bg="light blue")
    global b_four
    
    b_four=Button(f_two,text=text_four,width=13,height=3,command=lambda: words(text_four,3),bg="light blue")
    global b_five
    
    b_five=Button(f_two,text=text_five,width=13,height=3,command=lambda: words(text_five,4),bg="light blue")
    global b_six
    
    b_six=Button(f_two,text=text_six,width=13,height=3,command=lambda: words(text_six,5),bg="light blue")
    global b_seven
    
    b_seven=Button(f_two,text=text_seven,width=13,height=3,command=lambda: words(text_seven,6),bg="light blue")
    global b_eight
    
    b_eight=Button(f_two,text=text_eight,width=13,height=3,command=lambda: words(text_eight,7),bg="light blue")
    global b_nine
    
    b_nine=Button(f_two,text=text_nine,width=13,height=3,command=lambda: words(text_nine,8),bg="light blue")
    global b_ten
    
    b_ten=Button(f_two,text=text_ten,width=13,height=3,command=lambda: words(text_ten,9),bg="light blue")
    global b_eleven
    
    b_eleven=Button(f_two,text=text_eleven,width=13,height=3,command=lambda: words(text_eleven,10),bg="light blue")
    global b_twelve
    
    b_twelve=Button(f_two,text=text_twelve,width=13,height=3,command=lambda: words(text_twelve,11),bg="light blue")
    global b_thirteen
    
    b_thirteen=Button(f_two,text=text_thirteen,width=13,height=3,command=lambda: words(text_thirteen,12),bg="light blue")
    global b_fourteen
    
    b_fourteen=Button(f_two,text=text_fourteen,width=13,height=3,command=lambda: words(text_fourteen,13),bg="light blue")
    global b_fifteen
    
    b_fifteen=Button(f_two,text=text_fifteen,width=13,height=3,command=lambda: words(text_fifteen,14),bg="light blue")
    global b_sixteen
    
    b_sixteen=Button(f_two,text=text_sixteen,width=13,height=3,command=lambda: words(text_sixteen,15),bg="light blue")
    global b_seventeen
    
    b_seventeen=Button(f_two,text=text_seventeen,width=13,height=3,command=lambda: words(text_seventeen,16),bg="light blue")
    global b_eighteen
    
    b_eighteen=Button(f_two,text=text_eighteen,width=13,height=3,command=lambda: words(text_eighteen,17),bg="light blue")
    global b_nineteen
    
    b_nineteen=Button(f_two,text=text_nineteen,width=13,height=3,command=lambda: words(text_nineteen,18),bg="light blue")
    global b_twenty
    
    b_twenty=Button(f_two,text=text_twenty,width=13,height=3,command=lambda: words(text_twenty,19),bg="light blue")
    global b_twentyone
    
    b_twentyone=Button(f_two,text=text_twentyone,width=13,height=3,command=lambda: words(text_twentyone,20),bg="light blue")
    global b_twentytwo
    
    b_twentytwo=Button(f_two,text=text_twentytwo,width=13,height=3,command=lambda: words(text_twentytwo,21),bg="light blue")
    global b_twentythree
    
    b_twentythree=Button(f_two,text=text_twentythree,width=13,height=3,command=lambda: words(text_twentythree,22),bg="light blue")
    global b_twentyfour
    
    b_twentyfour=Button(f_two,text=text_twentyfour,width=13,height=3,command=lambda: words(text_twentyfour,23),bg="light blue")
    global b_twentyfive

    b_twentyfive=Button(f_two,text=text_twentyfive,width=13,height=3,command=lambda: words(text_twentyfive,24),bg="light blue")
    global b_twentysix

    b_twentysix=Button(f_two,text=text_twentysix,width=13,height=3,command=lambda: words(text_twentysix,25),bg="light blue")
    global b_twentyseven

    b_twentyseven=Button(f_two,text=text_twentyseven,width=13,height=3,command=lambda: words(text_twentyseven,26),bg="light blue")
    global b_twentyeight

    b_twentyeight=Button(f_two,text=text_twentyeight,width=13,height=3,command=lambda: words(text_twentyeight,27),bg="light blue")
    global b_twentynine

    b_twentynine=Button(f_two,text=text_twentynine,width=13,height=3,command=lambda: words(text_twentynine,28),bg="light blue")
    global b_thirty

    b_thirty=Button(f_two,text=text_thirty,width=13,height=3,command=lambda: words(text_thirty,29),bg="light blue")
    global b_thirtyone

    b_thirtyone=Button(f_two,text=text_thirtyone,width=13,height=3,command=lambda: words(text_thirtyone,30),bg="light blue")
    global b_thirtytwo

    b_thirtytwo=Button(f_two,text=text_thirtytwo,width=13,height=3,command=lambda: words(text_thirtytwo,31),bg="light blue")
    global b_thirtythree

    b_thirtythree=Button(f_two,text=text_thirtythree,width=13,height=3,command=lambda: words(text_thirtythree,32),bg="light blue")
    global b_thirtyfour

    b_thirtyfour=Button(f_two,text=text_thirtyfour,width=13,height=3,command=lambda: words(text_thirtyfour,33),bg="light blue")
    global b_thirtyfive

    b_thirtyfive=Button(f_two,text=text_thirtyfive,width=13,height=3,command=lambda: words(text_thirtyfive,34),bg="light blue")
    global b_thirtysix

    b_thirtysix=Button(f_two,text=text_thirtysix,width=13,height=3,command=lambda: words(text_thirtysix,35),bg="light blue")
    global b_thirtyseven

    b_thirtyseven=Button(f_two,text=text_thirtyseven,width=13,height=3,command=lambda: words(text_thirtyseven,36),bg="light blue")
    global b_thirtyeight

    b_thirtyeight=Button(f_two,text=text_thirtyeight,width=13,height=3,command=lambda: words(text_thirtyeight,37),bg="light blue")
    global b_thirtynine

    b_thirtynine=Button(f_two,text=text_thirtynine,width=13,height=3,command=lambda: words(text_thirtynine,38),bg="light blue")
    global b_forty

    b_forty=Button(f_two,text=text_forty,width=13,height=3,command=lambda: words(text_forty,39),bg="light blue")
    global b_fortyone

    b_fortyone=Button(f_two,text=text_fortyone,width=13,height=3,command=lambda: words(text_fortyone,40),bg="light blue")
    global b_fortytwo

    b_fortytwo=Button(f_two,text=text_fortytwo,width=13,height=3,command=lambda: words(text_fortytwo,41),bg="light blue")
    global b_fortythree3

    b_fortythree=Button(f_two,text=text_fortythree,width=13,height=3,command=lambda: words(text_fortythree,42),bg="light blue")
    global b_fortyfour

    b_fortyfour=Button(f_two,text=text_fortyfour,width=13,height=3,command=lambda: words(text_fortyfour,43),bg="light blue")
    
    
    b_one.place(x=10,y=150)
    b_two.place(x=110,y=150)
    b_three.place(x=210,y=150)
    b_four.place(x=310,y=150)
    b_five.place(x=410,y=150)
    b_six.place(x=510,y=150)
    b_seven.place(x=610,y=150)
    b_eight.place(x=710,y=150)
    b_ten.place(x=10,y=200)
    b_eleven.place(x=110,y=200)
    b_twelve.place(x=210,y=200)
    b_thirteen.place(x=310,y=200)
    b_fourteen.place(x=410,y=200)
    b_fifteen.place(x=510,y=200)
    b_sixteen.place(x=610,y=200)
    b_seventeen.place(x=710,y=200)
    b_nineteen.place(x=10,y=250)
    b_twenty.place(x=110,y=250)
    b_twentyone.place(x=210,y=250)
    b_twentytwo.place(x=310,y=250)
    b_twentythree.place(x=410,y=250)
    b_twentyfour.place(x=510,y=250)
    b_twentyfive.place(x=610,y=250)
    b_twentysix.place(x=710,y=250)
    b_twentyeight.place(x=10,y=300)
    b_twentynine.place(x=110,y=300)
    b_thirty.place(x=210,y=300)
    b_thirtyone.place(x=310,y=300)
    b_thirtytwo.place(x=410,y=300)
    b_thirtythree.place(x=510,y=300)
    b_thirtyfour.place(x=610,y=300)
    b_thirtyfive.place(x=710,y=300)
    b_thirtyseven.place(x=10,y=350)
    b_thirtyeight.place(x=110,y=350)
    b_thirtynine.place(x=210,y=350)
    b_forty.place(x=310,y=350)
    b_fortyone.place(x=410,y=350)
    b_fortytwo.place(x=510,y=350)
    b_fortythree.place(x=610,y=350)
    b_fortyfour.place(x=710,y=350)
    

    Submit_button=Button(f_two,text="Submit",font="Courier 9 bold",width=13,height=3,command=Submit,activebackground="yellow",bg="black",borderwidth=0,fg="gold",highlightthickness=2,highlightcolor="gold",default="active")
    Submit_button.place(x=350,y=540)
    global button_list
    button_list=[b_one,b_two,b_three,b_four,b_five,b_six,b_seven,b_eight,b_nine,b_ten,b_eleven,b_twelve,b_thirteen,b_fourteen,b_fifteen,b_sixteen,b_seventeen,b_eighteen,b_nineteen,b_twenty,b_twentyone,b_twentytwo,b_twentythree,b_twentyfour,b_twentyfive,b_twentysix,b_twentyseven,b_twentyeight,b_twentynine,b_thirty,b_thirtyone,b_thirtytwo,b_thirtythree,b_thirtyfour,b_thirtyfive,b_thirtysix,b_thirtyseven,b_thirtyeight,b_thirtynine,b_forty,b_fortyone,b_fortytwo,b_fortythree,b_fortyfour]
    
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
        root.quit()
    else:
        pass
reset_counter=0
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







def Submit():

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
    e_one.delete(0,END)
    global button_list
    for i in  range(44):
        for j in range(44):
         if button_list[j]['state']==DISABLED:
            button_list[j]['state']=NORMAL
            button_list[j].configure(bg="light blue")
         else:
            pass
        

colour_list=["red","light blue","light green","violet","magenta","white","yellow","blue","indigo","cyan","pink","green","orange"]

def colour_change(colour_index):
    logo_label.configure(fg=colour_list[colour_index])
    colour_index+=1
    if colour_index==len(colour_list):
        colour_index=0
    f_one.after(1000,colour_change,colour_index)

frames = [
    PhotoImage(file=r"welcome.gif", format="gif -index %i" % (i))
    for i in range(2)
]
def update(ind):
    frame = frames[ind]
    ind += 1
    if ind >= 2:  
        ind = 0
    gif.configure(image=frame,bg="gold")
    f_one.after(200, update, ind)


ms=0
submit_count=0
Score=0
Score_string=f"Score: {Score}"


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


Exit_button=Button(f_one,text="Exit",command=root.quit,bg="black",font="Courier 20 bold",activebackground="light blue",borderwidth=0,fg="light blue",highlightthickness=1,highlightbackground="light blue",highlightcolor="light blue",default="active")
Exit_button.place(x=373,y=500)

f_one.after(0,colour_change,0)    


gif = Label(f_one,highlightthickness=10,highlightcolor="grey",highlightbackground="grey")
gif.place(x=300,y=55)

f_one.after(0, update, 0)

f_one.place(x=0,y=0)
root.mainloop()
