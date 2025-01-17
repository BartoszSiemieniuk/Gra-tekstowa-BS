import random
pytania_1 = [['Przydomek wiedźmina Geralta wskazuje na to, że bohater sagi Andrzeja Sapkowskiego pochodzi z..','A:Vengerbergu','B:Rivii','C:Oxenfurtu','D:Tretogoru','B'],
             ['Który z owadów wydaje charakterystyczny dźwięki zwane cykaniem?','A:Świerszcz','B:Mucha','C:Komar','D:Pszczoła','A'],
             ['Ile godzin liczą dwie doby?', 'A: 48h',"B: 24h",'C: 12h','D: 38h',"A"],
             ['Jak nazywa się największy ocean na Ziemi?','A:Ocean Arktyczny','B:Ocean Indyjski','C:Ocean Spokojny','D:Ocean Atlantycki','C']]
pytania_2 = [['Co to jest akwedukt?','A:Most dla pociągów','B:System wodociągów','C:Basen w Grecji','D:Most dla samochodów','B'],
             ['Co służy do kreślenia tuszem lini na powiece lub wokół oka?','A:Korektor','B:Eye-liner','C:Konturówka','D:Mascara','B'],
             ['Jak nazywa się stolica amerykańskiego stanu Indiana?','A:Oklahoma City','B:Indianapolis','C:Austin','D:Chicago','B'],
             ['Big Mac to:','A:Hot dog','B:Zapiekanka','C:Pizza','D:Hamburger','D']]
pytania_3 = [['W które urodziny Harry Potter dostał pierwszy list z Hogwartu','A:7','B:13','C:11','D:15','C'],
             ['Która z wymienionych poniżej karek, nie jest marką herbaty?','A:Saga','B:Tetlay','C:Lipton','D:Nescafe','D'],
             ['Rodzinnym krajem Boba Marleya jest:','A:Honduras','B:Dominikana','C:Kuba','D:Jamajka','D'],
             ['Z jakiego kraju pochodzi marka zegarków Seiko?','A:USA','B:Szwajcaria','C:Japonia','D:Szwecja','C']]
kola_r = ['1)Pół na pół','2)telefon do przyjaciela', '3)pytanie do publiczności']
kwota = ['0','500$', '1000$', '2000$', '5000$', '10000$', '20000$', '40000$', '75000$', '12500$', '25000$', '50000$', '100000$']
wygrana = 0
ukonczone_pytania = 0
kolo_w_r = 0
kolo_1 = 0
kolo_2 = 0
kolo_3 = 0
print('Witaj w grze milionerzy\n', 'Teraz wytłumacze jak w nią grać\n', 'By wybrać odpowiedź należy wpisać jedno z podanych: A, B, C, lub D\n', 'lecz w samej grze istnieje także możliowśc poddania się poprze wpisanie: X\n',
      'Masz także dostępne koła rtunkowe do wykoprzystania, pamiętaj że przy karzdym pytaniu możesz wykorzystać tylko 1 koło ratunkowe poprzez wpisanie czyfry znajdujcej się przed nazwą koła\n')
print("W grze masz 12 pytań i każdemu znich przypisana jest inna kwota a oto one:")
for z in range(1,13):
    print(*kwota[z])
print('W tym kwoty gwarantowane ',kwota[2],' i', kwota[7])
while True:
    if ukonczone_pytania < 4:
        obecne_pytanie = random.choice(pytania_1)
        pytania_1.remove(obecne_pytanie)
    elif ukonczone_pytania >= 4 and ukonczone_pytania < 8:
        obecne_pytanie = random.choice(pytania_2)
        pytania_2.remove(obecne_pytanie)
    elif ukonczone_pytania >= 8 and ukonczone_pytania < 12:
        obecne_pytanie = random.choice(pytania_3)
        pytania_3.remove(obecne_pytanie)
    elif ukonczone_pytania == 12:
        print("Gratulacje właśnie udało ci się ukończyć naszą grę i wygrać milion$")
        quit()
    odp_p = 0
    kolo_w_r = 0
    print("Czytam pytanie")
    print(obecne_pytanie[0])
    print(obecne_pytanie[1],obecne_pytanie[2],obecne_pytanie[3],obecne_pytanie[4])
    print('Dostępne koła ratunkowe:', *kola_r, sep='\n')
    while odp_p == 0:
        odp = input("Podaj odp: ")
        odp = odp.capitalize()
        if odp == "A" or odp == "B" or odp == "C" or odp == "D":
            odp_p = 1
            if odp == obecne_pytanie[5]:
                print("To jest dobra odpowiedź")
                ukonczone_pytania = ukonczone_pytania + 1
                wygrana = wygrana+1
                if wygrana == 2:
                    print('Udału ci się osiągnąć pierwszą nagrodę gwarantowaną równą '+kwota[wygrana])
                elif wygrana == 7:
                    print('Udału ci się osiągnąć drugą nagrodę gwarantowaną równą ' + kwota[wygrana])
                else:
                    print("Twoja obecna wygrana to "+kwota[wygrana])

                if ukonczone_pytania <= 11:
                    print("Oto twoje następne pytanie")
            else:
                print("Niestety jest to błędna odpowiedź")
                if wygrana >= 2:
                    print('Wcześnie udało się tobie osiągnoć próg z kwotągwarantowaną oto twaoja wygrana 1000$')
                elif wygrana >=7:
                    print('Wcześnie udało się tobie osiągnoć próg z kwotągwarantowaną oto twaoja wygrana 1000$')
                exit()
        elif odp == 'X':
            print('Po dłuższym namyśle postanowiłeś nie odpowiadać na pytanie i odejści z obecną wygranąwartą '+ kwota[wygrana])
            quit()
        elif odp == '1' or odp == '2' or odp == '3':
            if kolo_w_r == 0:
                if odp == '1'and kolo_1 == 0:
                    kolo_w_r = 1
                    pnp = ['A','B','C','D']
                    pnp.remove(obecne_pytanie[5])
                    opnp=[obecne_pytanie[5], random.choice(pnp)]
                    opnp = sorted(opnp)
                    for j in range(0,2):
                        for i in range(1,5):
                            if opnp[j][0]==obecne_pytanie[i][0]:
                                opnp[j] = obecne_pytanie[i]
                    print(obecne_pytanie[0])
                    print('Oto pozostałe dwie odpowiedzi', *opnp, sep='\n')
                    kola_r.remove('1)Pół na pół')
                    kolo_1 = 1
                elif odp == '2' and kolo_2 == 0:
                    kolo_w_r = 1
                    print(obecne_pytanie[0])
                    print("Moim zdaniem porwną odpowiedzą będzie odpowiedź ", obecne_pytanie[5])
                    kola_r.remove('2)telefon do przyjaciela')
                    kolo_2 = 2
                elif odp == '3' and kolo_3 == 0:
                    kolo_w_r = 1
                    kolo_3 = 1
                    kola_r.remove('3)pytanie do publiczności')
                    Ar = random.randint(5,21)
                    Br = random.randint(5,21)
                    Cr = random.randint(5,21)
                    Dr = random.randint(5,21)
                    suma = Ar + Br + Cr + Dr
                    reszta = 100 - suma
                    if obecne_pytanie[5] == 'A':
                        Ar = Ar + reszta
                    elif obecne_pytanie[5] == 'B':
                        Br = Br + reszta
                    elif obecne_pytanie[5] == 'C':
                        Cr = Cr + reszta
                    elif obecne_pytanie[5] == 'D':
                        Dr = Dr + reszta
                    print(obecne_pytanie[0])
                    print(obecne_pytanie[1], obecne_pytanie[2], obecne_pytanie[3], obecne_pytanie[4])
                    print('Oto odpowiedzi publiczności','\nA:',Ar,'%','\nB:',Br,'%','\nC:', Cr,'%','\nD:', Dr,'%')
                elif (odp == '1' and kolo_1 == 1) or (odp == '2' and kolo_2 == 2) or (odp == '3' and kolo_3 == 1):
                    print('Już wykorzystałeś to koło ratunkowe')
            else:
                print('Już wykorzystałeś 1 koło ratunkowe w tej rundzie')

        else:
            print("Musisz odpowiedzieć A, B, C lub D")