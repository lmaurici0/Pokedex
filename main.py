from tkinter import *
from tkinter  import ttk
from PIL import Image,ImageTk
from dados import *
import random

#  Colors
co0 = "# 444466"     #  Black
co1 = "# feffff"     #  White
co2 = "# 6f9fbd"     #  Blue
co3 = "# 38576b"     #  Value
co4 = "# 403d3d"     #  letter
co5 = "# ef5350"     #  Red

janela = Tk()
janela.title('Pokédex')
janela.iconbitmap("images/pokeball.ico")
janela.geometry('700x600')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use('clam')

# Frame Creation
frame_pokemon = Frame(janela, width=700, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

def troca_pokemon(i):
    global img_pok, pok_img
    frame_pokemon['bg'] = pokemon[i]['tipo'][3] 

    # Pokemon Type
    pok_nome['text'] =  [i]
    pok_nome['bg'] = pokemon[i] ['tipo'][3]
    pok_tipo['text'] = pokemon[i] ['tipo'][1]
    pok_tipo['bg'] = pokemon[i] ['tipo'][3]
    pok_id['text'] = pokemon[i] ['tipo'][0]
    pok_id['bg'] = pokemon[i] ['tipo'][3]

    img_pok = pokemon[i] ['tipo'][2]
    img_pok = Image.open(img_pok)
    img_pok = img_pok.resize((238, 238))
    img_pok = ImageTk.PhotoImage(img_pok)
    pok_img = Label(frame_pokemon,image=img_pok, relief='flat', bg=pokemon[i]['tipo'][3], fg=co1)
    pok_img.place(x=60,y=50)
    pok_tipo.lift()

    pok_hp['text'] = pokemon[i]['status'][0]
    pok_atack['text'] = pokemon[i]['status'][1]
    pok_def['text'] = pokemon[i]['status'][2]
    pok_vel['text'] = pokemon[i]['status'][3]
    pok_tot['text'] = pokemon[i]['status'][4]
    pok_hb1['text'] = pokemon[i]['habilidades'][0]
    pok_hb2['text'] = pokemon[i]['habilidades'][1]

# Names
pok_nome = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 20'), fg=co1)
pok_nome.place(x=12,y=15)

# Cattegoriy
pok_tipo = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_tipo.place(x=12,y=50 )

# Id
pok_id = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_id.place(x=12,y=75)

# Stats
pok_stts = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_stts.place(x=15,y=310 )

# Hp
pok_hp = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hp.place(x=15,y=360)

# Attack
pok_atack = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_atack.place(x=15,y=385)

# Defense
pok_def = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_def.place(x=15,y=410)

# Velocity
pok_vel = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_vel.place(x=15,y=435)

# Total
pok_tot = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_tot.place(x=15,y=460)

# Habilities
pok_habilidade= Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_habilidade.place(x=180,y=310 )

# Hp
pok_hb1 = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hb1.place(x=195,y=360)

# Attack
pok_hb2 = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hb2.place(x=195,y=385)

# Buttons
img_pok_1 = Image.open('images/cabeca-pikachu.png')
img_pok_1 = img_pok_1.resize((40, 40))
img_pok_1 = ImageTk.PhotoImage(img_pok_1)
b_pok_1 = Button(janela,command=lambda:troca_pokemon('Pikachu'), image=img_pok_1, text='Pikachu', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_1.place(x=500,y=10)

img_pok_2 = Image.open('images/cabeca-bulbasaur.png')
img_pok_2 = img_pok_2.resize((40, 40))
img_pok_2= ImageTk.PhotoImage(img_pok_2)
b_pok_2 = Button(janela,command=lambda:troca_pokemon('Bulbasaur'), image=img_pok_2, text='Bulbasaur', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_2.place(x=500,y=65)

img_pok_3 = Image.open('images/cabeca-charmander.png')
img_pok_3 = img_pok_3.resize((40, 40))
img_pok_3 = ImageTk.PhotoImage(img_pok_3)
b_pok_3 = Button(janela,command=lambda:troca_pokemon('Charmander'), image=img_pok_3, text='Charmander', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_3.place(x=500,y=120)

img_pok_4 = Image.open('images/cabeca-dragonite.png')
img_pok_4 = img_pok_4.resize((40, 40))
img_pok_4 = ImageTk.PhotoImage(img_pok_4)
b_pok_4 = Button(janela,command=lambda:troca_pokemon('Dragonite'), image=img_pok_4, text='Dragonite', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_4.place(x=500,y=180)

img_pok_5 = Image.open('images/cabeca-gengar.png')
img_pok_5 = img_pok_5.resize((40, 40))
img_pok_5 = ImageTk.PhotoImage(img_pok_5)
b_pok_5 = Button(janela,command=lambda:troca_pokemon('Gengar'), image=img_pok_5, text='Gengar', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_5.place(x=500,y=240)

img_pok_6 = Image.open('images/cabeca-gyarados.png')
img_pok_6 = img_pok_6.resize((40, 40))
img_pok_6 = ImageTk.PhotoImage(img_pok_6)
b_pok_6 = Button(janela,command=lambda:troca_pokemon('Gyarados'), image=img_pok_6, text='Gyarados', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_6.place(x=500,y=300)

img_pok_7 = Image.open('images/cabeca-mewtwo.png')
img_pok_7 = img_pok_7.resize((40, 40))
img_pok_7 = ImageTk.PhotoImage(img_pok_7)
b_pok_7 = Button(janela,command=lambda:troca_pokemon('Mewtwo'), image=img_pok_7, text='Mewtwo', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_7.place(x=500,y=360)

img_pok_8 = Image.open('images/cabeca-mew.png')
img_pok_8 = img_pok_8.resize((40, 40))
img_pok_8 = ImageTk.PhotoImage(img_pok_8)
b_pok_8 = Button(janela,command=lambda:troca_pokemon('Mew'), image=img_pok_8, text='Mew', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_8.place(x=500,y=420)

img_pok_9 = Image.open('images/cabeca-magikarp.png')
img_pok_9 = img_pok_9.resize((40, 40))
img_pok_9 = ImageTk.PhotoImage(img_pok_9)
b_pok_9 = Button(janela,command=lambda:troca_pokemon('Magikarp'), image=img_pok_9, text='Magikarp', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_9.place(x=500,y=480)

img_pok_10 = Image.open('images/cabeca-arceus.png')
img_pok_10 = img_pok_10.resize((40, 40))
img_pok_10 = ImageTk.PhotoImage(img_pok_10)
b_pok_10 = Button(janela,command=lambda:troca_pokemon('Arceus'), image=img_pok_10, text='Arceus', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_10.place(x=500,y=540)

random_pokemon = ['Dragonite', 'Gengar', 'Gyarados', 'Charmander', 'Pikachu', 'Bulbasaur', 'Mewtwo', 'Mew', 'Magikarp', 'Arceus']
poke_final = random.sample(random_pokemon, 1)

troca_pokemon(poke_final[0])

janela.mainloop()
