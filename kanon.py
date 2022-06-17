import math
import numpy as np

#Leser inn koordinater og deler opp i x- og y-koordinater. Gjør dem om til tall.
kanonPos = input("Oppgi kanonens koordinater (slik: '123 456') :")
kX, kY = kanonPos.split(" ")
kX=int(kX)
kY=int(kY)

#Leser inn koordinater og deler opp i x- og y-koordinater. Gjør dem om til tall.
observasjonPos = input("Oppgi observasjonspostens koordinater (slik: '123 456') :")
oX, oY = observasjonPos.split(" ")
oX=int(oX)
oY=int(oY)

#Henter inn vinkel og avstand fra OP til mål. Gjør om til radianer og tall.
vinkelOPTilMål=input("Skriv inn vinkel fra OP til mål: ")
avstandOPTilMål = input("Skriv inn avstand fra OP til mål: ")
vinkelOPTilMål=math.radians(int(vinkelOPTilMål))
avstandOPTilMål=int(avstandOPTilMål)

#Funksjon som får inn vinkel fra OP til mål, avstand OP til mål, OP-pos og kanon-pos
#Returnerer liste med vinkel kanon til mål og avstand kanon til mål.
def kanoninnstilling(votm,aotm,ox,oy,kx,ky):
    omx = int(math.sin(votm)*aotm)
    omy = int(math.cos(votm)*aotm)

    xmål = int(ox+omx)
    ymål = int(oy+omy)

    kmx = xmål-kx
    kmy = ymål-ky

    vinkelKanonTilMål = int(math.degrees(math.atan(kmx/kmy)))
    avstandKanonTilMål = int(math.hypot(kmx,kmy))
    
    return(vinkelKanonTilMål, avstandKanonTilMål)

#Funksjon som mottar korrigeringer fra OP og skriver ut korrigeringer til kanon.
def kanonjustering():

    kanoninnstillingsliste = kanoninnstilling(vinkelOPTilMål, avstandOPTilMål,oX, oY, kX, kY)

    print("Observer treffpunkt!")
    vinkelkorreksjon = math.radians(int(input("Vinkelkorreksjon: ")))
    avstandkorreksjon = int(input("Avstandkorreksjon: "))

    kanoninnstillingsliste2=kanoninnstilling((vinkelOPTilMål-vinkelkorreksjon), avstandOPTilMål-avstandkorreksjon,oX, oY, kX, kY)

    korreksjonsliste = np.array(kanoninnstillingsliste)-np.array(kanoninnstillingsliste2)


    print("Juster kanonen sideveis ",korreksjonsliste[0], " og avstanden ",korreksjonsliste[1])

#Løkke som kjører til man er bra innstilt og vil ha "Fire for Effect!"
while True:
    kanonjustering()