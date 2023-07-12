from tkinter import *
from tkinter  import ttk
from PIL import Image,ImageTk
from dados import *
import random

# cores
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha

janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use('clam')

#criando frame
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

def troca_pokemon(i):
    global img_pok, pok_img
    frame_pokemon['bg'] = pokemon[i]['tipo'][3] 

    #tipo de pokemon
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

# nomes
pok_nome = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 20'), fg=co1)
pok_nome.place(x=12,y=15)

#categoria
pok_tipo = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_tipo.place(x=12,y=50 )

#id
pok_id = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_id.place(x=12,y=75)

#status
pok_stts = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_stts.place(x=15,y=310 )
#hp
pok_hp = Label(janela, text='HP: 300', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hp.place(x=15,y=360)

#ataque
pok_atack = Label(janela, text='Ataque: 600', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_atack.place(x=15,y=385)

#defesa
pok_def = Label(janela, text='Defesa: 500', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_def.place(x=15,y=410)

#velocidade
pok_vel = Label(janela, text='Velocidade: 300', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_vel.place(x=15,y=435)

#total
pok_tot = Label(janela, text='Total: 1.700', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_tot.place(x=15,y=460)

#habilidades
pok_habilidade= Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_habilidade.place(x=180,y=310 )

#hp
pok_hb1 = Label(janela, text='Choque do trovão', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hb1.place(x=195,y=360)

#ataque
pok_hb2 = Label(janela, text='Cabeçada', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hb2.place(x=195,y=385)

# Criando botoes
img_pok_1 = Image.open('images/cabeca-pikachu.png')
img_pok_1 = img_pok_1.resize((40, 40))
img_pok_1 = ImageTk.PhotoImage(img_pok_1)
b_pok_1 = Button(janela,command=lambda:troca_pokemon('Pikachu'), image=img_pok_1, text='Pikachu', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_1.place(x=375,y=10)

img_pok_2 = Image.open('images/cabeca-bulbasaur.png')
img_pok_2 = img_pok_2.resize((40, 40))
img_pok_2= ImageTk.PhotoImage(img_pok_2)
b_pok_2 = Button(janela,command=lambda:troca_pokemon('Bulbasaur'), image=img_pok_2, text='Bulbasaur', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_2.place(x=375,y=65)

img_pok_3 = Image.open('images/cabeca-charmander.png')
img_pok_3 = img_pok_3.resize((40, 40))
img_pok_3 = ImageTk.PhotoImage(img_pok_3)
b_pok_3 = Button(janela,command=lambda:troca_pokemon('Charmander'), image=img_pok_3, text='Charmander', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_3.place(x=375,y=120)

img_pok_4 = Image.open('images/cabeca-dragonite.png')
img_pok_4 = img_pok_4.resize((40, 40))
img_pok_4 = ImageTk.PhotoImage(img_pok_4)
b_pok_4 = Button(janela,command=lambda:troca_pokemon('Dragonite'), image=img_pok_4, text='Dragonite', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_4.place(x=375,y=180)

img_pok_5 = Image.open('images/cabeca-gengar.png')
img_pok_5 = img_pok_5.resize((40, 40))
img_pok_5 = ImageTk.PhotoImage(img_pok_5)
b_pok_5 = Button(janela,command=lambda:troca_pokemon('Gengar'), image=img_pok_5, text='Gengar', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_5.place(x=375,y=240)

img_pok_6 = Image.open('images/cabeca-gyarados.png')
img_pok_6 = img_pok_6.resize((40, 40))
img_pok_6 = ImageTk.PhotoImage(img_pok_6)
b_pok_6 = Button(janela,command=lambda:troca_pokemon('Gyarados'), image=img_pok_6, text='Gyarados', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_6.place(x=375,y=300)

random_pokemon = ['Dragonite', 'Gengar', 'Gyarados', 'Charmander', 'Pikachu', 'Bulbasaur']
poke_final = random.sample(random_pokemon, 1)

troca_pokemon(poke_final[0])

janela.mainloop()