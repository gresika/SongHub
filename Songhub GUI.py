#importing libraries 

import tkinter     #Structure
from tkinter import *
from tkinter import ttk     #Styling
from tkinter.ttk import Notebook     #To switch  between tabs
from PIL import Image , ImageTk      #For image


#root window

mw=Tk() #main window
mw.title('Songhub')
mw.geometry('900x700')
tabcontrol=Notebook(mw)


#------------

#TAB1

tab1=ttk.Frame(tabcontrol,width = 800 , height= 700)
tabcontrol.add(tab1,text='Home')
tabcontrol.grid(padx=20 , ipadx=18, ipady=18)


#space for entering user details

name=ttk.Label(tab1,text="Enter your Name" , font=(None,13))
name.pack()
name.place(x=350 , y=20)

#Area for user name
name2= StringVar()
enter=ttk.Entry(tab1,text=name2)
enter.pack()
enter.place(x=350 , y=50)


#function for button to display the welcome message

def Display():
    v = name2.get()
    name3= ttk.Label(tab1 , text = ('Welcome '+ v) , font = (None,15))
    name3.pack(padx = 10, pady = 20)
    name3.place(x=340 , y=120)

#Button Structure

save = Button(tab1, text = "Save" , command = Display ,bd = 5, width = 5)
save.pack()
save.place(x=385 , y=80)
    


#Image
image1 = Image.open("D:/Budget Manager/usericon.jpg")
image1 = image1.resize((450,400),Image.ANTIALIAS)  #Antialias - Antialiasing is a technique used in digital imaging to reduce visual defects in case high resolution images are presented with low resolution ones.
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(tab1, image=test)
label1.image = test
label1.pack()
label1.place(x= 185, y=160)


#TAB2

tab2 = ttk.Frame(tabcontrol , width = 600,height = 700)
tabcontrol.add (tab2, text = 'Select your Song')

#-------------------MAIN SONG SELECTION----------------#


def songhub():
      #Importing Libraries     
    '''import pillow'''
    '''import PIL'''
    import tkinter
    import os
    from PIL import Image 
    import pyttsx3
    import webbrowser
    import random
    engine = pyttsx3.init()
    engine.say("Welcome to the SONG HUB")
    engine.runAndWait()
    print("")
    print("                                                                 A song addict?\n                                                     You have arrived at the right place !!!!")
    print("")
    print("------------------------------------------------------------Welcome to the SONG HUB---------------------------------------------------")
    #a= Image.open('D:/Budget Manager/usericon.jpg')
    '''try:
        img=Image.open('D:/Budget Manager/usericon.jpg')
        img.show()
    except IOError:
        pass'''
        




        
    #a.show()
    '''a.save("tmp.png")
    os.system("powershell -c tmp.png")'''


    


    
    '''
    f = open("song.txt","a")
    f.close()
    print(" These are all your previously heard songs:-")
    f=open("song.txt",'r')
    d=f.read()
    print(d)
    f.close()
    f=open("song.txt",'r')
    vrinda=f.readlines()
    str2=vrinda
    print(str2)'''
    
    #freq.
    '''f=open("song2.txt",'a')
    f.close()
    f=open("song2.txt")
    s=f.read()
    print(s)
    f.close()
    list4=[]
    str2=("Thunder , Belong with me , Thunder, Thunder,Fire,Fire ")
    a=str2.count("Thunder")  
    z=str2.count("Belong with me")  
    b=str2.count("Fire")
    dict1={a:'\n Thunder',b:'\n Fire',z:'\n Belong With Me'}
    v=dict1.keys()
    for i in v:
         if i>=2:
              m=dict1[i]
              list4.append(m)
    vrinda=list4[0]
    gre=list4[1]
          #print(w)
          
   f=open("song2.txt",'a')
   f.write(vrinda)
   f.write("")
   f.write(gre)
   f.close() '''#freq ends




    

    print("")
    print("  Today's Special :-")
    print("")
    print("  MOODS:-              CATEGORIES:-\n   1.Happy              1.Pop\n   2.Sad                2.Kpop\n   3.Motivation         3.Popular\n   4.Party              4.Bollywood Instrumental\n   5.Workout            5.Rap")
    print("")
    engine = pyttsx3.init()
    engine.say("Play songs according to your mood? Enter 'm'\n  Wanna choose from the categories instead? Enter 'c'")
    engine.runAndWait()
    choice=input("  Play songs according to your mood? Enter 'm'\n  Wanna choose from the categories instead? Enter 'c'")
    print("")
                                                                        #CATEGORY
    if choice==("c" or "C"):
        engine = pyttsx3.init()
        engine.say("Enter the number against your category")
        engine.runAndWait()
        num=int(input("  Enter the number against your category"))
        print("")
        if num==1:
            engine = pyttsx3.init()
            engine.say("Want us to play a random song? enter 'r'\n  Wanna select for yourself from the list? Enter 'l'")
            engine.runAndWait()
            
            a= input("  Want us to play a random song? enter 'r'\n  Wanna select for yourself from the list? Enter 'l'")
            print("")
            if a==('l' or 'L'):
                engine = pyttsx3.init()
                engine.say("ALL SONGS FROM POP CATEGORY:")
                engine.runAndWait()
                print("  ALL SONGS FROM POP CATEGORY:-\n   1.Peaches\n   2.Bad Guy\n   3.Hold On\n   4.Don't Start Now\n   5.Heartbreak Anniversary\n   6.Unbelievable")
                print("")
                print("")
                engine = pyttsx3.init()
                engine.say("Enter the number against your selected track and your song would be played")
                engine.runAndWait()
                sn = int(input("  Enter the number against your selected track and your song would be played"))
                if sn==1:
                    #Category,Pop,choose
                    engine = pyttsx3.init()
                    engine.say("Playing Peaches")
                    engine.runAndWait()
                    print("  Playing Peaches")
                    ll=('https://open.spotify.com/track/4iJyoBOLtHqaGxP12qzhQI?si=01e8bd5951724d91')
                    str1 = ("\n  Peaches")
                    webbrowser.open(ll)
                elif sn==2:
                    print("  Playing Bad Guy")
                    ll=('https://open.spotify.com/track/2Fxmhks0bxGSBdJ92vM42m?si=a31ee256da4f40f1')
                    str1 = ("\n  Bad Guy")
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing Hold On")
                    ll=('https://open.spotify.com/track/1nahzW3kfMuwReTka28tH5?si=6816ae9e08704aff')
                    str1 = ("\n  Hold On")
                    webbrowser.open(ll)
                elif sn==4:
                    print("  Playing Don't Start Now")
                    str1 = ("\n  Dont Start Now")
                    ll=('https://open.spotify.com/track/6WrI0LAC5M1Rw2MnX2ZvEg?si=1305e5ba10ac48f9')
                    webbrowser.open(ll)
                elif sn==5:
                    print("  Playing Heartbreak Anniversary")
                    str1 = ("\n  Heartbreak Anniversary")
                    ll=('https://open.spotify.com/track/3FAJ6O0NOHQV8Mc5Ri6ENp?si=8d1ff733f00e421a')
                    webbrowser.open(ll)
                elif sn==6:
                    print("  Playing Unbelievable")
                    str1 = ("\n  Unbelievable")
                    ll=('https://open.spotify.com/track/1LHfEkVMR0Yj20C8lWdgpA?si=16ff4071ee05444c')
                    webbrowser.open(ll)
            else:
                sn=random.randrange(1,6)
                if sn==1:                                                                                                    #Category,Pop, Random                                                                                                   
                    print("  Playing Peaches")
                    str1 = ("\n  Peaches")
                    ll=('https://open.spotify.com/track/4iJyoBOLtHqaGxP12qzhQI?si=01e8bd5951724d91')
                    webbrowser.open(ll)
                elif sn==2:
                    print("  Playing Bad Guy")
                    str1 = ("\n  Bad Guy")
                    ll=('https://open.spotify.com/track/2Fxmhks0bxGSBdJ92vM42m?si=a31ee256da4f40f1')
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing Hold On")
                    str1 = ("\n  Hold On")
                    ll=('https://open.spotify.com/track/1nahzW3kfMuwReTka28tH5?si=6816ae9e08704aff')
                    webbrowser.open(ll)
                elif sn==4:
                    print("  Playing Don't Start Now")
                    str1 = ("\n  Dont Start Now")
                    ll=('https://open.spotify.com/track/6WrI0LAC5M1Rw2MnX2ZvEg?si=1305e5ba10ac48f9')
                    webbrowser.open(ll)
                elif sn==5:
                    print("  Playing Heartbreak Anniversary")
                    str1 = ("\n  Heartbreak Anniversary")
                    ll=('https://open.spotify.com/track/3FAJ6O0NOHQV8Mc5Ri6ENp?si=8d1ff733f00e421a')
                    webbrowser.open(ll)
                elif sn==6:
                    print("  Playing Unbelievable")
                    str1 = ("\n  Unbelievable")
                    ll=('https://open.spotify.com/track/1LHfEkVMR0Yj20C8lWdgpA?si=16ff4071ee05444c')
                    webbrowser.open(ll)
        if num==2:
            a= input("  Want us to play a random song? enter 'r'\n  Wanna select for yourself from the list? Enter 'l'")
            print("")
            if a==('l' or 'L'):
                print("  ALL SONGS FROM KPOP CATEGORY:-\n   1.Dynamite\n   2.Pretty Savage\n   3.You Never Know\n   4.Lights\n   5.Make It Right\n   6.How You Like That\n   7.Love To Hate Me\n   8.Celebrity\n   9.Some\n   10.Lovesick Girls\n   11.Not Shy\n   12.Filter\n   13.Who\n   14.Boy With Luv\n   15.Best Of Me\n   16.Mikrokosmos\n   17.Solo\n   18.Euphoria\n   19.Fake Love\n   20.Waste It On Me")
                print("")
                sn = int(input("  Enter the number against your selected track and your song would be played"))
                if sn==1:                                                                                              #Category,Kpop,Choose
                    print("  Playing Dynamite")
                    str1 = ("\n  Dynamite")
                    ll=('https://open.spotify.com/track/4saklk6nie3yiGePpBwUoc?si=d9b58e8d173f4eb6')
                    webbrowser.open(ll)
                elif sn==2:
                    print("  Playing Pretty Savage")
                    str1 = ("\n  Pretty Savage")
                    ll=('https://open.spotify.com/track/28tufPkTcXmdNqTvi9hsoG?si=dcd846b0a4ab4510')
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing You Never Know")
                    str1 = ("\n  You Never Know")
                    ll=('https://open.spotify.com/track/00J8yszzb5PR6ZIvSBtg0Y?si=7efc422b89944455')
                    webbrowser.open(ll)
                elif sn==4:
                    print("  Playing Lights")
                    str1 = ("\n  Lights")
                    ll=('https://open.spotify.com/track/44vXWYTcdrejrIQZEoHzl8?si=dee63ece997a46b4')
                    webbrowser.open(ll)
                elif sn==5:
                    print("  Playing Make It Right")
                    str1 = ("\n  Making It Right")
                    ll=('https://open.spotify.com/track/314ZkcV7oLWG8yWE7LABvH?si=c3a4c23a74df402d')
                    webbrowser.open(ll)
                elif sn==6:
                    print("  Playing How You Like That")
                    str1 = ("\n  How You Like That")
                    ll=('https://open.spotify.com/track/6bvZRLLkBKkmgpBJTTj3QK?si=edb7de2249144a04')
                    webbrowser.open(ll)
                elif sn==7:
                    print("  Playing Love To Hate Me")
                    str1 = ("\n  Love To Hate Me")
                    ll=('https://open.spotify.com/track/3Gk1LfB771PIEGgsEa7gcV?si=df94ddfe02fc41d3')
                    webbrowser.open(ll)
                elif sn==8:
                    print("  Playing Celebrity")
                    str1 = ("\n  Celebrity")
                    ll=('https://open.spotify.com/track/4RewTiGEGoO7FWNZUmp1f4?si=ecb6416a1e8849c9')
                    webbrowser.open(ll)
                elif sn==9:
                    print("  Playing Some")
                    str1 = ("\n  Some")
                    ll=('https://open.spotify.com/track/3jsYQw78lrxJA2ysnmOIf9?si=1bf0743fd31d46f3')
                    webbrowser.open(ll)
                elif sn==10:
                    print("  Playing Lovesick Girls")
                    str1 = ("\n  Lovesick Girls")
                    ll=('https://open.spotify.com/track/1GMufNnkKAnPLnqKJ5HHxW?si=5389f88e73cb4203')
                    webbrowser.open(ll)
                elif sn==11:
                    print("  Playing Not Shy")
                    str1 = ("\n  Not Shy")
                    ll=('https://open.spotify.com/track/4ecVWqbtW6phQGpZMAyqIU?si=f95a76b227eb4400')
                    webbrowser.open(ll)
                elif sn==12:
                    print("  Playing Filter")
                    str1 = ("\n  Filter")
                    ll=('https://open.spotify.com/track/0ono6UCNVZ1XqOm6j78Blu?si=0035c8ed83da44f9')
                    webbrowser.open(ll)
                elif sn==13:
                    print("  Playing Who")
                    str1 = ("\n  Who")
                    ll=('https://open.spotify.com/track/2qG81jL9UIP54uS8gYyP4k?si=d4ac03add3c34742')
                    webbrowser.open(ll)
                elif sn==14:
                    print("  Playing Boy With Luv")
                    str1 = ("\n  Boy With Luv")
                    ll=('https://open.spotify.com/track/5KawlOMHjWeUjQtnuRs22c?si=274e875b7c0d4f6c')
                    webbrowser.open(ll)
                elif sn==15:
                    print("  Playing Best Of Me")
                    str1 = ("\n  Best Of Me")
                    ll=('https://open.spotify.com/track/3KGEbCfnzAzFVimY9p62MN?si=cda28409c9964d5c')
                    webbrowser.open(ll)
                elif sn==16:
                    print("  Playing Mikrokosmos")
                    str1 = ("\n  Playing Mikrokosmos")
                    ll=('https://open.spotify.com/track/5hnbE5BF2e8BCk9OMR1UVC?si=41bfd079b5b44ce6')
                    webbrowser.open(ll)
                elif sn==17:
                    print("  Playing Solo")
                    str1 = ("\n  Solo")
                    ll=('https://open.spotify.com/track/7yAy2gL2rtatS56jzkakhr?si=d61eb9f49ba64b27')
                    webbrowser.open(ll)
                elif sn==18:
                    print("Playing Euphoria")
                    str1 = ("\n  Euphoria")
                    ll=('https://open.spotify.com/track/3p6hnejEQYXkiTO1lAzVc0?si=31fc8447329d48af')
                    webbrowser.open(ll)
                elif sn==19:
                    print("  Playing Fake Love")
                    str1 = ("\n  Fake Love")
                    ll=('https://open.spotify.com/track/5Sn2fm8aisVlR7S6u1KW57?si=af7592c2793a44ff')
                    webbrowser.open(ll)
                elif sn==20:
                    print("  Playing Waste It On Me")
                    str1 = ("\n  Waste It On Me")
                    ll=('https://open.spotify.com/track/2FWyJIT0gL2G3xWVQ9Id5f?si=d9a8be342f2243d1')
                    webbrowser.open(ll)
                    
                    
            else:
                sn=random.randrange(1,21)
                if sn==1:                                                                                                     #Category,Kpop,random
                    print("  Playing Dynamite")
                    str1 = ("\n  Dynamite")
                    ll=('https://open.spotify.com/track/4saklk6nie3yiGePpBwUoc?si=d9b58e8d173f4eb6')
                    webbrowser.open(ll)
                elif sn==2:
                    print("  Playing Pretty Savage")
                    str1 = ("\n  Pretty Savage")
                    ll=('https://open.spotify.com/track/28tufPkTcXmdNqTvi9hsoG?si=dcd846b0a4ab4510')
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing You Never Know")
                    str1 = ("\n  You Never Know")
                    ll=('https://open.spotify.com/track/00J8yszzb5PR6ZIvSBtg0Y?si=7efc422b89944455')
                    webbrowser.open(ll)
                elif sn==4:
                    print("  Playing Lights")
                    str1 = ("\n  Lights")
                    ll=('https://open.spotify.com/track/44vXWYTcdrejrIQZEoHzl8?si=dee63ece997a46b4')
                    webbrowser.open(ll)
                elif sn==5:
                    print("  Playing Make It Right")
                    str1 = ("\n  Make It Right")
                    ll=('https://open.spotify.com/track/314ZkcV7oLWG8yWE7LABvH?si=c3a4c23a74df402d')
                    webbrowser.open(ll)
                elif sn==6:
                    print("  Playing How You Like That")
                    str1 = ("\n  How You Like It")
                    ll=('https://open.spotify.com/track/6bvZRLLkBKkmgpBJTTj3QK?si=edb7de2249144a04')
                    webbrowser.open(ll)
                elif sn==7:
                    print("  Playing Love To Hate Me")
                    str1 = ("\n  Love To Hate Me")
                    ll=('https://open.spotify.com/track/3Gk1LfB771PIEGgsEa7gcV?si=df94ddfe02fc41d3')
                    webbrowser.open(ll)
                elif sn==8:
                    print("  Playing Celebrity")
                    str1 = ("\n  Celebrity")
                    ll=('https://open.spotify.com/track/4RewTiGEGoO7FWNZUmp1f4?si=ecb6416a1e8849c9')
                    webbrowser.open(ll)
                elif sn==9:
                    print("  Playing Some")
                    str1 = ("\n  Some")
                    ll=('https://open.spotify.com/track/3jsYQw78lrxJA2ysnmOIf9?si=1bf0743fd31d46f3')
                    webbrowser.open(ll)
                elif sn==10:
                    print("  Playing Lovesick Girls")
                    str1 = ("\n  Lovesick Girls")
                    ll=('https://open.spotify.com/track/1GMufNnkKAnPLnqKJ5HHxW?si=5389f88e73cb4203')
                    webbrowser.open(ll)
                elif sn==11:
                    print("  Playing Not Shy")
                    str1 = ("\n  Not Shy")
                    ll=('https://open.spotify.com/track/4ecVWqbtW6phQGpZMAyqIU?si=f95a76b227eb4400')
                    webbrowser.open(ll)
                elif sn==12:
                    print("  Playing Filter")
                    str1 = ("\n  Filter")
                    ll=('https://open.spotify.com/track/0ono6UCNVZ1XqOm6j78Blu?si=0035c8ed83da44f9')
                    webbrowser.open(ll)
                elif sn==13:
                    print("  Playing Who")
                    str1 = ("\n  Who")
                    ll=('https://open.spotify.com/track/2qG81jL9UIP54uS8gYyP4k?si=d4ac03add3c34742')
                    webbrowser.open(ll)
                elif sn==14:
                    print("  Playing Boy With Luv")
                    str1 = ("\n  Boy With Luv")
                    ll=('https://open.spotify.com/track/5KawlOMHjWeUjQtnuRs22c?si=274e875b7c0d4f6c')
                    webbrowser.open(ll)
                elif sn==15:
                    print("  Playing Best Of Me")
                    str1 = ("\n  Best Of Me")
                    ll=('https://open.spotify.com/track/3KGEbCfnzAzFVimY9p62MN?si=cda28409c9964d5c')
                    webbrowser.open(ll)
                elif sn==16:
                    print("  Playing Mikrokosmos")
                    str1 = ("\n  Mikrokosmos")
                    ll=('https://open.spotify.com/track/5hnbE5BF2e8BCk9OMR1UVC?si=41bfd079b5b44ce6')
                    webbrowser.open(ll)
                elif sn==17:
                    print("  Playing Solo")
                    str1 = ("\n  Solo")
                    ll=('https://open.spotify.com/track/7yAy2gL2rtatS56jzkakhr?si=d61eb9f49ba64b27')
                    webbrowser.open(ll)
                elif sn==18:
                    print("  Playing Euphoria")
                    str1 = ("\n  Euphoria")
                    ll=('https://open.spotify.com/track/3p6hnejEQYXkiTO1lAzVc0?si=31fc8447329d48af')
                    webbrowser.open(ll)
                elif sn==19:
                    print("  Playing Fake Love")
                    str1 = ("\n  Fake Love")
                    ll=('https://open.spotify.com/track/5Sn2fm8aisVlR7S6u1KW57?si=af7592c2793a44ff')
                    webbrowser.open(ll)
                elif sn==20:
                    print("  Playing Waste It On Me")
                    str1 = ("\n  Waste It On Me")
                    ll=('https://open.spotify.com/track/2FWyJIT0gL2G3xWVQ9Id5f?si=d9a8be342f2243d1')
                    webbrowser.open(ll)
                    
        if num==3:
            engine = pyttsx3.init()
            engine.say("Want us to play a random song? enter 'r'\n  Wanna select for yourself from the list? Enter 'l'")
            engine.runAndWait()
            a= input("  Want us to play a random song? enter 'r'\n  Wanna select for yourself from the list? Enter 'l'")
            print("")
            if a==('l' or 'L'):
                engine = pyttsx3.init()
                engine.say("ALL SONGS FROM POPULAR SONGS CATEGORY")
                engine.runAndWait()
                print("  ALL SONGS FROM POPULAR SONGS CATEGORY:-\n   1.Taki Taki\n   2.Shape Of U\n   3.Lean On\n   4.Girls Like You\n   5.Rockabye\n   6.2002\n   7.Belong With Me\n   8.I Like Me Better\n   9.Middle\n   10.Love Story\n   11.Princesses Don't Cry\n   12.We Don't Talk Anymore")
                print("")
                sn = int(input("  Enter the number against your selected track and your song would be played"))
                if sn==1:                                                                                                  #Category,Popular,chose
                    print("  Playing Taki Taki")
                    str1 = ("\n  Taki Taki")
                    ll=('https://open.spotify.com/track/4w8niZpiMy6qz1mntFA5uM?si=53076014d94e4f48')
                    webbrowser.open(ll)
                elif sn==2:
                    engine = pyttsx3.init()
                    engine.say("Playing Shape Of U")
                    engine.runAndWait()
                    print("  Playing Shape Of U")
                    str1 = ("\n  Shape Of You")
                    ll=('https://open.spotify.com/track/7qiZfU4dY1lWllzX7mPBI3?si=9cba220cbbe54b24')
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing Lean On")
                    str1 = ("\n  Lean On")
                    ll=('https://open.spotify.com/track/1Lim1Py7xBgbAkAys3AGAG?si=17304673615e478c')
                    webbrowser.open(ll)
                elif sn==4:
                    print("  Playing Girls Like You")
                    str1 = ("\n  Girls Like You")
                    ll=('https://open.spotify.com/track/7fa9MBXhVfQ8P8Df9OEbD8?si=4dcf4bf2d36045ad')
                    webbrowser.open(ll)
                elif sn==5:
                    print("  Playing Rockabye")
                    str1 = ("\n  Rockabye")
                    ll=('https://open.spotify.com/track/5knuzwU65gJK7IF5yJsuaW?si=ec4a10ac18064e56')
                    webbrowser.open(ll)
                elif sn==6:
                    print("  Playing 2002")
                    str1 = ("\n  2002")
                    ll=('https://open.spotify.com/track/2BgEsaKNfHUdlh97KmvFyo?si=e06b14ce510045f9')
                    webbrowser.open(ll)
                elif sn==7:
                    print("  Playing Belong With Me")
                    str1 = ("\n  Belong With Me")
                    ll=('https://open.spotify.com/track/1GEBsLDvJGw7kviySRI6GX?si=95c1b9d5130144aa')
                    webbrowser.open(ll)
                elif sn==8:
                    print("  Playing I Like Me Better")
                    str1 = ("\n  I Like Me Better")
                    ll=('https://open.spotify.com/track/2P91MQbaiQOfbiz9VqhqKQ?si=49b9389d912e4d7a')
                    webbrowser.open(ll)
                elif sn==9:
                    print("  Playing Middle")
                    str1 = ("\n  Middle")
                    ll=('https://open.spotify.com/track/0g5EKLgdKvNlln7TNqBByK?si=9d0958819f794231')
                    webbrowser.open(ll)
                elif sn==10:
                    print("  Playing Love Story")
                    str1 = ("\n  Love Story")
                    ll=('https://open.spotify.com/track/1D4PL9B8gOg78jiHg3FvBb?si=c39ad8fa3be74c72')
                    webbrowser.open(ll)
                elif sn==11:
                    print("  Playing Princesses Don't Cry")
                    str1 = ("\n  Princessess Don't Cry")
                    ll=('https://open.spotify.com/track/2j3BmbOK0ZElUhsKH7q7eh?si=9152bd449af74bf3')
                    webbrowser.open(ll)
                elif sn==12:
                    print("  Playing We Don't Talk Anymore")
                    str1 = ("\n  We Dont Talk Anymore")
                    ll=('https://open.spotify.com/track/06KyNuuMOX1ROXRhj787tj?si=8384d2a123e2449a')
                    webbrowser.open(ll)
            else:
                sn=random.randrange(1,13)
                if sn==1:
                    #Category,Popular,random
                    engine = pyttsx3.init()
                    engine.say("Playing Taki Taki")
                    engine.runAndWait()
                    print("  Playing Taki Taki")
                    str1 = ("\n  Taki Taki")
                    ll=('https://open.spotify.com/track/4w8niZpiMy6qz1mntFA5uM?si=53076014d94e4f48')
                    webbrowser.open(ll)
                elif sn==2:
                     engine = pyttsx3.init()
                     engine.say("Playing Shape Of U")
                     engine.runAndWait()
                     print("  Playing Shape Of U")
                     str1 = ("\n  Shape Of You")
                     ll=('https://open.spotify.com/track/7qiZfU4dY1lWllzX7mPBI3?si=9cba220cbbe54b24')
                     webbrowser.open(ll)
                elif sn==3:
                     engine = pyttsx3.init()
                     engine.say("Playing Lean On")
                     engine.runAndWait()
                     print("  Playing Lean On")
                     str1 = ("\n  Lean On")
                     ll=('https://open.spotify.com/track/1Lim1Py7xBgbAkAys3AGAG?si=17304673615e478c')
                     webbrowser.open(ll)
                elif sn==4:
                     engine = pyttsx3.init()
                     engine.say("Playing Girls Like You")
                     engine.runAndWait()
                     print("  Playing Girls Like You")
                     str1 = ("\n  Girls Like You")
                     ll=('https://open.spotify.com/track/7fa9MBXhVfQ8P8Df9OEbD8?si=4dcf4bf2d36045ad')
                     webbrowser.open(ll)
                elif sn==5:
                     engine = pyttsx3.init()
                     engine.say("Playing Rockabye")
                     engine.runAndWait()
                     print("  Playing Rockabye")
                     str1 = ("\n  Rockabye")
                     ll=('https://open.spotify.com/track/5knuzwU65gJK7IF5yJsuaW?si=ec4a10ac18064e56')
                     webbrowser.open(ll)
                elif sn==6:
                     engine = pyttsx3.init()
                     engine.say("Playing 2002")
                     engine.runAndWait()
                     print("  Playing 2002")
                     str1 = ("\n  2002")
                     ll=('https://open.spotify.com/track/2BgEsaKNfHUdlh97KmvFyo?si=e06b14ce510045f9')
                     webbrowser.open(ll)
                elif sn==7:
                     engine = pyttsx3.init()
                     engine.say("Playing Belong With Me")
                     engine.runAndWait()
                     print("  Playing Belong With Me")
                     str1 = ("\n  Belong With Me")
                     ll=('https://open.spotify.com/track/1GEBsLDvJGw7kviySRI6GX?si=95c1b9d5130144aa')
                     webbrowser.open(ll)
                elif sn==8:
                     engine = pyttsx3.init()
                     engine.say("Playing I Like Me Better")
                     engine.runAndWait()
                     print("  Playing I Like Me Better")
                     str1 = ("\n  I like Me Better")
                     ll=('https://open.spotify.com/track/2P91MQbaiQOfbiz9VqhqKQ?si=49b9389d912e4d7a')
                     webbrowser.open(ll)
                elif sn==9:
                     engine = pyttsx3.init()
                     engine.say("Playing Middle")
                     engine.runAndWait()
                     print("  Playing Middle")
                     str1 = ("\n  Middle")
                     ll=('https://open.spotify.com/track/0g5EKLgdKvNlln7TNqBByK?si=9d0958819f794231')
                     webbrowser.open(ll)
                elif sn==10:
                     engine = pyttsx3.init()
                     engine.say("Playing Love Story")
                     engine.runAndWait()
                     print("  Playing Love Story")
                     str1 = ("\n  Love Story")
                     ll=('https://open.spotify.com/track/1D4PL9B8gOg78jiHg3FvBb?si=c39ad8fa3be74c72')
                     webbrowser.open(ll)
                elif sn==11:
                     engine = pyttsx3.init()
                     engine.say("Playing Princesses Don't Cry")
                     engine.runAndWait()
                     print("  Playing Princesses Don't Cry")
                     str1 = ("\n  Princessess Dont Cry")
                     ll=('https://open.spotify.com/track/2j3BmbOK0ZElUhsKH7q7eh?si=9152bd449af74bf3')
                     webbrowser.open(ll)
                elif sn==12:
                     engine = pyttsx3.init()
                     engine.say("Playing We Don't Talk Anymore")
                     engine.runAndWait()
                     print("  Playing We Don't Talk Anymore")
                     str1 = ("\n  We Dont Talk Anymore")
                     ll=('https://open.spotify.com/track/06KyNuuMOX1ROXRhj787tj?si=8384d2a123e2449a')
                     webbrowser.open(ll)
        if num==4:
            a= input("  Want us to play a random song? enter 'r'\n  Wanna select for yourself from the list? Enter 'l'")
            print("")
            if a==('l' or 'L'):
                print("  ALL SONGS FROM BOLLYWOOD INSTRUMENTAL SONGS CATEGORY:-\n   1.Hum Tum\n   2.Dekho Na\n   3.Tujh Mein Rab Dikhta Hai\n   4.Dil Diyan Galla\n   5.Aadha Ishq\n")
                print("")
                sn = int(input("  Enter the number against your selected track and your song would be played"))
                if sn==1:                                                                                                #Category,instrumental,choose
                    print("  Playing Hum Tum")
                    str1 = ("\n  Hum Tum")
                    ll=('https://open.spotify.com/track/7qSTBn9oShMTdySMHU5LDZ?si=266a1063580b469c')
                    webbrowser.open(ll)
                elif sn==2:
                    print("  Playing Dekho Na")
                    str1 = ("\n  Dekho Na")
                    ll=('https://open.spotify.com/track/4twvlx3zxA8kcCaZSZiUaP?si=5d20c04480d54a6f')
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing Tujh Mein Rab Dikhta Hai")
                    str1 = ("\n  Tujhme Rab Dikhta Hai")
                    ll=('https://open.spotify.com/track/3GkYAqLwnqMek9Wv1k4qUV?si=f7094ddb1b294f9f')
                    webbrowser.open(ll)
                elif sn==4:
                    print("  Playing Dil Diyan Gallan")
                    str1 = ("\n  Dil Diyan Gallan")
                    ll=('https://open.spotify.com/track/2HaDQezXO0fctBfyXU1wMg?si=491b226772f5400d')
                    webbrowser.open(ll)
                elif sn==5:
                    print("  Playing Aadha Ishq")
                    str1 = ("\n  Adha Ishq")
                    ll=('https://open.spotify.com/track/0bNFYXV9Fe1yWhzhD4qlZ5?si=e4df051a046b4cc0')
                    webbrowser.open(ll)
            else:
                sn=random.randrange(1,6)
                if sn==1:                                                                           #Category,instrumental,random
                    print("  Playing Hum Tum")
                    str1 = ("\n  Hum Tum")
                    ll=('https://open.spotify.com/track/7qSTBn9oShMTdySMHU5LDZ?si=266a1063580b469c')
                    webbrowser.open(ll)
                elif sn==2:
                    print("  Playing Dekho Na")
                    str1 = ("\n  Dekho Na")
                    ll=('https://open.spotify.com/track/4twvlx3zxA8kcCaZSZiUaP?si=5d20c04480d54a6f')
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing Tujh Mein Rab Dikhta Hai")
                    str1 = ("\n  Tujh Mein Rab Dikhta Hai")
                    ll=('https://open.spotify.com/track/3GkYAqLwnqMek9Wv1k4qUV?si=f7094ddb1b294f9f')
                    webbrowser.open(ll)
                elif sn==4:
                    print("  Playing Dil Diyan Gallan")
                    str1 = ("\n  Dil Diyan Gallan")
                    ll=('https://open.spotify.com/track/2HaDQezXO0fctBfyXU1wMg?si=491b226772f5400d')
                    webbrowser.open(ll)
                elif sn==5:
                    print("  Playing Aadha Ishq")
                    str1 = ("\n  Adha Ishq")
                    ll=('https://open.spotify.com/track/0bNFYXV9Fe1yWhzhD4qlZ5?si=e4df051a046b4cc0')
                    webbrowser.open(ll)
                                      
                    

        if num==5:
            a= input("  Want us to play a random song? enter 'r'\n  Wanna select for yourself from the list? Enter 'l'")
            print("")
            if a==('l' or 'L'):
                print("  ALL SONGS FROM THE RAP CATEGORY:-\n   1.Apna Time Aayega\n   2.Rap God\n   3.Fight The Good Fight\n   4.Mood\n   5.GANG GANG\n")
                print("")
                sn = int(input("  Enter the number against your selected track and your song would be played"))
                if sn==1:                                                                                               #Category,Rap,Choose
                    print("  Playing Apna Time Aayega")
                    str1 = ("\n  Apna Time Ayega")
                    ll=('https://open.spotify.com/track/5uaIbU3oHHcSOK6WFNK5nj?si=b4d8f64f9e2d4225')
                    webbrowser.open(ll)
                elif sn==2:
                    print("  Playing Rap God")
                    str1 = ("\n  Rap God ")
                    ll=('https://open.spotify.com/track/6or1bKJiZ06IlK0vFvY75k?si=a7569d3ad5cb4daf')
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing Fight The Good Fight")
                    str1 = ("\n  Fight The Good Fight")
                    ll=('https://open.spotify.com/track/0GwAD0ZIWxwu9T98Kmn32V?si=670463a95e3c49f4')
                    webbrowser.open(ll)
                elif sn==4:
                    print("  Mood")
                    str1 = ("\n  Mood")
                    ll=('https://open.spotify.com/track/3tjFYV6RSFtuktYl3ZtYcq?si=4068c4ae2f0045d8')
                    webbrowser.open(ll)
                elif sn==5:
                    print("  Playing GANG GANG")
                    str1 = ("\n  Gang Gang")
                    ll=('https://open.spotify.com/track/4VW44pawoOHPUjlN7DX5vk?si=b557d6a7bc2a430b')
                    webbrowser.open(ll)
            else:
                sn=random.randrange(1,6)
                if sn==1:                                                                                               #Category,Rap,random
                    print("  Playing Apna Time Aayega")
                    str1 = ("\n  Apna Time Ayega")
                    ll=('https://open.spotify.com/track/5uaIbU3oHHcSOK6WFNK5nj?si=b4d8f64f9e2d4225')
                    webbrowser.open(ll)
                elif sn==2:
                    print("  Playing Rap God")
                    str1 = ("\n  Rap God")
                    ll=('https://open.spotify.com/track/6or1bKJiZ06IlK0vFvY75k?si=a7569d3ad5cb4daf')
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing Fight The Good Fight")
                    str1 = ("\n  Fight The Good Fight")
                    ll=('https://open.spotify.com/track/0GwAD0ZIWxwu9T98Kmn32V?si=670463a95e3c49f4')
                    webbrowser.open(ll)
                elif sn==4:
                    print("  Mood")
                    str1 = ("\n  Mood")
                    ll=('https://open.spotify.com/track/3tjFYV6RSFtuktYl3ZtYcq?si=4068c4ae2f0045d8')
                    webbrowser.open(ll)
                elif sn==5:
                    print("  Playing GANG GANG")
                    str1 = ("\n  Gang Gang")
                    ll=('https://open.spotify.com/track/4VW44pawoOHPUjlN7DX5vk?si=b557d6a7bc2a430b')
                    webbrowser.open(ll)
                   
                                                                       #MOOD
    else:                                                                                                           
        num=int(input("  Enter the number against your mood"))
        print("")
        if num==1:
            a= input("  Want us to play a random happy song? enter 'r'\n  Wanna select for yourself from the list? Enter 'l'")
            print("")
            if a==('l' or 'L'):
                print("  ALL SONGS FOR HAPPY MOOD:-\n   1.Lush Life\n   2.Counting Stars\n   3.Levitating\n   4.I don't care\n   5.Beautiful People\n   6.Sugarcrash!\n   7.Run Free")
                print("")
                sn = int(input("  Enter the number against your selected track and your song would be played"))
                if sn==1:                                                                                             #MOOD,Happy,choose
                    print("  Playing Lush Life")
                    str1 = ("\n  Lush Life")
                    ll=('https://open.spotify.com/track/1rIKgCH4H52lrvDcz50hS8?si=7deccce051874412')
                    webbrowser.open(ll)
                elif sn==2:
                    print("  Playing Counting Stars")
                    str1 = ("\n  Counting Stars")
                    ll=('https://open.spotify.com/track/2tpWsVSb9UEmDRxAl1zhX1?si=513178c46cf34d55')
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing Levitating")
                    str1 = ("\n  Levitating")
                    ll=('https://open.spotify.com/track/39LLxExYz6ewLAcYrzQQyP?si=495886c7e9584e2a')
                    webbrowser.open(ll)
                elif sn==4:
                    print("  Playing I don't care")
                    str1 = ("\n  I Dont Care")
                    ll=('https://open.spotify.com/track/0hVXuCcriWRGvwMV1r5Yn9?si=6fa31b6692f3428b')
                    webbrowser.open(ll)
                elif sn==5:
                    print("  Playing Beautiful People")
                    str1 = ("\n  Beautiful People")
                    ll=('https://open.spotify.com/track/4evmHXcjt3bTUHD1cvny97?si=0045dc3376f54c47')
                    webbrowser.open(ll)
                elif sn==6:
                    print("  Playing Sugarcrash!")
                    str1 = ("\n  Sugarcrash!")
                    ll=('https://open.spotify.com/track/2ePtv8MlBO9nuuXABqAfEX?si=9f209a50e55f4441')
                    webbrowser.open(ll)
                elif sn==7:
                    print("  Playing Run Free")
                    str1 = ("\n  Run Free")
                    ll=('https://open.spotify.com/track/1oIdcFtf58sZbS7QyZQJ2P?si=fae3351fb7104bc6')
                    webbrowser.open(ll)
            else:
                sn=random.randrange(1,8)
                if sn==1:                                                                                                    #MOOD,Happy,random
                    print("  Playing Lush Life")
                    str1 = ("\n  Lush Life")
                    ll=('https://open.spotify.com/track/1rIKgCH4H52lrvDcz50hS8?si=7deccce051874412')
                    webbrowser.open(ll)
                elif sn==2:
                    print("  Playing Counting Stars")
                    str1 = ("\n  Counting Stars")
                    ll=('https://open.spotify.com/track/2tpWsVSb9UEmDRxAl1zhX1?si=513178c46cf34d55')
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing Levitating")
                    str1 = ("\n  Levitating")
                    ll=('https://open.spotify.com/track/39LLxExYz6ewLAcYrzQQyP?si=495886c7e9584e2a')
                    webbrowser.open(ll)
                elif sn==4:
                    print("  Playing I don't care")
                    str1 = ("\n  I Dont Care")
                    ll=('https://open.spotify.com/track/0hVXuCcriWRGvwMV1r5Yn9?si=6fa31b6692f3428b')
                    webbrowser.open(ll)
                elif sn==5:
                    print("  Playing Beautiful People")
                    str1 = ("\n  Beautiful People")
                    ll=('https://open.spotify.com/track/4evmHXcjt3bTUHD1cvny97?si=0045dc3376f54c47')
                    webbrowser.open(ll)
                elif sn==6:
                    print("  Playing Sugarcrash!")
                    str1 = ("\n  Sugarcrash!")
                    ll=('https://open.spotify.com/track/2ePtv8MlBO9nuuXABqAfEX?si=9f209a50e55f4441')
                    webbrowser.open(ll)
                elif sn==7:
                    print("  Playing Run Free")
                    str1 = ("\n  Run Free")
                    ll=('https://open.spotify.com/track/1oIdcFtf58sZbS7QyZQJ2P?si=fae3351fb7104bc6')
                    webbrowser.open(ll)
        if num==2:
            a= input("  Want us to play a random song? enter 'r'\n  Wanna select for yourself from the list? Enter 'l'")
            print("")
            if a==('l' or 'L'):
                print("  ALL SONGS FOR SAD MOOD:-\n   1.Faded\n   2.Memories\n   3.Someone You Loved\n   4.Lose You To Love Me\n   5.Gone\n   6.Say You Won't Let Go\n   ")
                print("")
                sn = int(input("  Enter the number against your selected track and your song would be played"))
                if sn==1:                                                                                              #Mood,Sad,choose
                    print("  Playing Faded")
                    str1 = ("\n  Faded")
                    ll=('https://open.spotify.com/track/698ItKASDavgwZ3WjaWjtz?si=301c9c7dfb604d44')
                    webbrowser.open(ll)
                elif sn==2:
                    print("  Playing Memories")
                    str1 = ("\n  Memories")
                    ll=('https://open.spotify.com/track/2b8fOow8UzyDFAE27YhOZM?si=f0116555782e40c6')
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing Someone You Loved")
                    str1 = ("\n  Someone You Loved")
                    ll=('https://open.spotify.com/track/7qEHsqek33rTcFNT9PFqLf?si=ac5e07a1aa154939')
                    webbrowser.open(ll)
                elif sn==4:
                    print("  Playing Lose You To Love Me")
                    str1 = ("\n  Lose You To Love Me")
                    ll=('https://open.spotify.com/track/4l0Mvzj72xxOpRrp6h8nHi?si=b71443fb48e649d1')
                    webbrowser.open(ll)
                elif sn==5:
                    print("  Playing Gone")
                    str1 = ("\n  Gone")
                    ll=('https://open.spotify.com/track/2ayIgfvWo3SfYP2pVOr4pC?si=1ff244338a80444d')
                    webbrowser.open(ll)
                elif sn==6:
                    print("  Playing Say You Won't Let Go")
                    str1 = ("\n  Say Won't Let Go")
                    ll=('https://open.spotify.com/track/5uCax9HTNlzGybIStD3vDh?si=16caa02cf41949d6')
                    webbrowser.open(ll)
     
            else:
                sn=random.randrange(1,7)
                if sn==1:                                                                                              #Mood,Sad,random
                    print("  Playing Faded")
                    str1 = ("\n  Faded")
                    ll=('https://open.spotify.com/track/698ItKASDavgwZ3WjaWjtz?si=301c9c7dfb604d44')
                    webbrowser.open(ll)
                elif sn==2:
                    print("  Playing Memories")
                    str1 = ("\n  Memories")
                    ll=('https://open.spotify.com/track/2b8fOow8UzyDFAE27YhOZM?si=f0116555782e40c6')
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing Someone You Loved")
                    str1 = ("\n  Someone You Loved")
                    ll=('https://open.spotify.com/track/7qEHsqek33rTcFNT9PFqLf?si=ac5e07a1aa154939')
                    webbrowser.open(ll)
                elif sn==4:
                    print("  Playing Lose You To Love Me")
                    str1 = ("\n  Lose You To Love Me")
                    ll=('https://open.spotify.com/track/4l0Mvzj72xxOpRrp6h8nHi?si=b71443fb48e649d1')
                    webbrowser.open(ll)
                elif sn==5:
                    print("  Playing Gone")
                    str1 = ("\n  Gone")
                    ll=('https://open.spotify.com/track/2ayIgfvWo3SfYP2pVOr4pC?si=1ff244338a80444d')
                    webbrowser.open(ll)
                elif sn==6:
                    print("  Playing Say You Won't Let Go")
                    str1 = ("\n  Say You Wont Let Go")
                    ll=('https://open.spotify.com/track/5uCax9HTNlzGybIStD3vDh?si=16caa02cf41949d6')
                    webbrowser.open(ll)
                             

        if num==3:
            a= input("  Want us to play a random song? enter 'r'\n  Wanna select for yourself from the list? Enter 'l'")
            print("")
            if a==('l' or 'L'):
                print("  ALL SONGS FOR A MOTIVATED MOOD:-\n   1.On my Way\n   2.Sit Still Look Pretty\n   3.Fight Song\n   4.Stand By You\n   5.Roar")
                print("")
                sn = int(input("  Enter the number against your selected track and your song would be played"))
                if sn==1:                                                                                                #Mood,motivation, choose 
                    print("  Playing On my Way")
                    str1 = ("\n  On My Way")
                    ll=('https://open.spotify.com/track/4n7jnSxVLd8QioibtTDBDq?si=3f6e6205dbf94301')
                    webbrowser.open(ll)
                elif sn==2:
                    print("  Playing Sit Still Look Pretty")
                    str1 = ("\n  Sit Still Look Pretty")
                    ll=('https://open.spotify.com/track/2DpCdPMg1BADE4HDnxt3Rd?si=151b7251fdcd45f5')
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing Fight Song")
                    str1 = ("\n  Fight Song")
                    ll=('https://open.spotify.com/track/37f4ITSlgPX81ad2EvmVQr?si=062804ffb3244a66')
                    webbrowser.open(ll)
                elif sn==4:
                     print("  Playing Stand By You")
                     str1 = ("\n  Stand By You")
                     ll=('https://open.spotify.com/track/3kSXn1osC89W8JcPLozTzs?si=6624867a054e4dfe')
                     webbrowser.open(ll)
                elif sn==5:
                     print("  Playing Roar")
                     str1 = ("\n  Roar")
                     ll=('https://open.spotify.com/track/6F5c58TMEs1byxUstkzVeM?si=9cf5213c659a48ea')
                     webbrowser.open(ll)
                 
            else:
                sn=random.randrange(1,6)
                if sn==1:                                                                                                  #Mood,motivation,random
                    print("  Playing On my Way")
                    str1 = ("\n  On My Way")
                    ll=('https://open.spotify.com/track/4n7jnSxVLd8QioibtTDBDq?si=3f6e6205dbf94301')
                    webbrowser.open(ll)
                elif sn==2:
                    print("  Playing Sit Still Look Pretty")
                    str1 = ("\n  Sit Still Look Pretty")
                    ll=('https://open.spotify.com/track/2DpCdPMg1BADE4HDnxt3Rd?si=151b7251fdcd45f5')
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing Fight Song")
                    str1 = ("\n  Fight Song")
                    ll=('https://open.spotify.com/track/37f4ITSlgPX81ad2EvmVQr?si=062804ffb3244a66')
                    webbrowser.open(ll)
                elif sn==4:
                    print("  Playing Stand By You")
                    str1 = ("\n  Stand By You")
                    ll=('https://open.spotify.com/track/3kSXn1osC89W8JcPLozTzs?si=6624867a054e4dfe')
                    webbrowser.open(ll)
                elif sn==5:
                    print("  Playing Roar")
                    str1 = ("\n  Roar")
                    ll=('https://open.spotify.com/track/6F5c58TMEs1byxUstkzVeM?si=9cf5213c659a48ea')
                    webbrowser.open(ll)
        if num==4:
            a= input("  Want us to play a random song? enter 'r'\n  Wanna select for yourself from the list? Enter 'l'")
            print("")
            if a==('l' or 'L'):
                print("  ALL SONGS FOR A PARTY MOOD:-\n   1.Despacito\n   2.Dance Monkey\n   3.Safari\n   4.Animals\n   5.Cheap Thrills")
                print("")
                sn = int(input("  Enter the number againstyour selected track and your song would be played"))
                if sn==1:                                                                                                 #Mood,Party,Choose
                    print("  Playing Despacito")
                    str1 = ("\n  Despacito")
                    ll=('https://open.spotify.com/track/6habFhsOp2NvshLv26DqMb?si=79b4dcfdb37d4c96')
                    webbrowser.open(ll)
                elif sn==2:
                    print("  Playing Dance Monkey")
                    str1 = ("\n  Dance Monkey")
                    ll=('https://open.spotify.com/track/2XU0oxnq2qxCpomAAuJY8K?si=939b1c6f98204e97')
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing Safari")
                    str1 = ("\n  Safari")
                    ll=('https://open.spotify.com/track/6osKPJp6kQwZcgUqBteJFN?si=c05cb7689530485a')
                    webbrowser.open(ll)
                elif sn==4:
                    print("  Playing Animals")
                    str1 = ("\n  Animals")
                    ll=('https://open.spotify.com/track/3h4T9Bg8OVSUYa6danHeH5?si=c0e393766f0d49ca')
                    webbrowser.open(ll)
                elif sn==5:
                    print("  Playing Cheap Thrills")
                    str1 = ("\n  Cheap Thrills")
                    ll=('https://open.spotify.com/track/27SdWb2rFzO6GWiYDBTD9j?si=eb241d2cea834e5f')
                    webbrowser.open(ll)
                   
            else:
                sn=random.randrange(1,6)
                if sn==1:                                                                                                        #Mood,Party,random
                    print("  Playing Despacito")
                    str1 = ("\n  Despacito")
                    ll=('https://open.spotify.com/track/6habFhsOp2NvshLv26DqMb?si=79b4dcfdb37d4c96')
                    webbrowser.open(ll)
                elif sn==2:
                    print("  Playing Dance Monkey")
                    str1 = ("\n  Dance Monkey")
                    ll=('https://open.spotify.com/track/2XU0oxnq2qxCpomAAuJY8K?si=939b1c6f98204e97')
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing Safari")
                    str1 = ("\n  Safari")
                    ll=('https://open.spotify.com/track/6osKPJp6kQwZcgUqBteJFN?si=c05cb7689530485a')
                    webbrowser.open(ll)
                elif sn==4:
                    print("  Playing Animals")
                    str1 = ("\n  Animals")
                    ll=('https://open.spotify.com/track/3h4T9Bg8OVSUYa6danHeH5?si=c0e393766f0d49ca')
                    webbrowser.open(ll)
                elif sn==5:
                    print("  Playing Cheap Thrills")
                    str1 = ("\n  Cheap Thrills")
                    ll=('https://open.spotify.com/track/27SdWb2rFzO6GWiYDBTD9j?si=eb241d2cea834e5f')
                    webbrowser.open(ll)
        if num==5:
            a= input("  Want us to play a random song? enter 'r'\n  Wanna select for yourself from the list? Enter 'l'")
            print("")
            if a==('l' or 'L'):
                print("  ALL SONGS FOR WORKOUT MOOD:-\n   1.Believer\n   2.Thunder\n   3.Bhaag Milkha Bhaag\n   4.Sultan\n   5.Rock On")
                print("")
                sn = int(input("  Enter the number against your selected track and your song would be played"))
                if sn==1:                                                                                                       #Mood,workout,choose
                    print("  Playing Believer")
                    str1 = ("\n  Believer")
                    ll=('https://open.spotify.com/track/0pqnGHJpmpxLKifKRmU6WP?si=d7173244a4a54947')
                    webbrowser.open(ll)
                elif sn==2:
                    print("  Playing Thunder")
                    str1 = ("\n  Thunder")
                    ll=('https://open.spotify.com/track/1zB4vmk8tFRmM9UULNzbLB?si=cf1e6bde973e46b7')
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing Bhaag Milkha Bhaag")
                    str1 = ("\n  Bhaag Milkha Bhaag")
                    ll=('https://open.spotify.com/track/6cUM4yawhVYPXArGp6eWJe?si=03365396664c4b00')
                    webbrowser.open(ll)
                elif sn==4:
                    print("  Playing Sultan")
                    str1 = ("\n  Sultan")
                    ll=('https://open.spotify.com/track/3kSBSSsXtebECjCggW87yq?si=03dd1b67d6ed4e86')
                    webbrowser.open(ll)
                elif sn==5:
                    print("  Playing Rock On")
                    str1 = ("\n  Rock On")
                    ll=('https://open.spotify.com/track/6fABlNfAOylt7ZxfX8K1XL?si=03a3a16e7ba0434e')
                    webbrowser.open(ll)

            else:
                sn=random.randrange(1,6)
                if sn==1:                                                                                                        #Mood,workout,random
                    print("  Playing Believer")
                    str1 = ("\n  Believer")
                    ll=('https://open.spotify.com/track/0pqnGHJpmpxLKifKRmU6WP?si=d7173244a4a54947')
                    webbrowser.open(ll)
                elif sn==2:
                    print("  Playing Thunder")
                    str1 = ("\n  Thunder")
                    ll=('https://open.spotify.com/track/1zB4vmk8tFRmM9UULNzbLB?si=cf1e6bde973e46b7')
                    webbrowser.open(ll)
                elif sn==3:
                    print("  Playing Bhaag Milkha Bhaag")
                    str1 = ("\n  Bhaag Milkha Bhaag")
                    ll=('https://open.spotify.com/track/6cUM4yawhVYPXArGp6eWJe?si=03365396664c4b00')
                    webbrowser.open(ll)
                elif sn==4:
                    print("  Playing Sultan")
                    str1 = ("\n  Sultan")
                    ll=('https://open.spotify.com/track/3kSBSSsXtebECjCggW87yq?si=03dd1b67d6ed4e86')
                    webbrowser.open(ll)
                elif sn==5:
                    print("  Playing Rock On")
                    str1 = ("\n  Rock On")
                    ll=('https://open.spotify.com/track/6fABlNfAOylt7ZxfX8K1XL?si=03a3a16e7ba0434e')
                    webbrowser.open(ll)
                         #MOOD DONE!
    
    
    f = open("song.txt","a")
    f.write("")
    f.write(str1)
    f.close()
    f=open("song.txt",'r')
    d=f.read()
    #Counts no. of songs you have heard till now using this program
    count=0
    numlines=d.split('\n')
    for i in numlines:
        if i:
            count+=1     
    print("")
    
    c1=input("  Continue?Enter c")
    print("")
    
    if c1==('c' or 'C'):
        engine = pyttsx3.init()
        engine.say("Number of songs heard till now are",count)
        engine.runAndWait()
        print("  Number of songs heard till now are",count)
        print("")
        engine = pyttsx3.init()
        engine.say("Do you wanna Re-run the program? Enter 'y' or enter 'n' to quit")
        engine.runAndWait()
        end=input("\n  Do you wanna Re-run the program? Enter 'y' or enter 'n' to quit")
        if end=='y':
            songhub()
        else:
            engine = pyttsx3.init()
            engine.say("Thanks for trying this out")
            engine.runAndWait()
            print("\n  Thanks for trying this out")

#Button Structure

save = Button(tab2, text = "Begin!" , command = songhub ,bd = 5, width = 5)
save.pack()
save.place(x=385 , y=10)
        
    






mw.mainloop()






