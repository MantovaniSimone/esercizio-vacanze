print("Ristorante 5B")
variabile = "per prenotare bisogna chiamare al numero 123456789101"
print (variabile)
print("i clienti che chiamano dicono l'orario")
print("listino orari pomeridiani:")
counter = 11

while counter <= 14:
    print(counter)
    counter += 1

print("listino orari serali:")
counter = 19

while counter <22:
  print(counter)
  counter +=1

print("prenotazione 11/14: tavolo disponibile")
if(print):
  print("prenotazione confermata")
else:
  print("prenotazione negata")

print("prenotazione 19/22: tavolo disponibile")
if(print):
  print("prenotazione confermata")
else:
  print("prenotazione negata")

print("prenotazione 7/10: tavolo non disponibile")
if(print):
  print("Prenotazione Negata")
else:
  print("Prenotazione Confermata")

print("Prenotazione 15/18: Tavolo non disponibile")
if(print):
  print("Prenotazione Negata")
else:
  print("Prenotazione Confermata")

print("Prenotazione 23/24: Tavolo non disponibile")
if(print):
  print("prenotazione negata")
else:
  print("prenotazione confermata")

print("Dichiarare N persone")

counter = 1 

while counter <=6:
  print(counter)
  counter +=1

print("I clienti rientrano nei posti")
if(print):
  print("Tavolo Prenotato")
else:
  print("Annullare")

print("Elenco portate")
my_list = ["carne 8.00£", "carbonara 9.00£ ", "spaghetti 5.00£", "pesce 15.00£",]
type(my_list)
print(my_list)

print("ogni portata vinene associata a un numero")
counter = 1

while counter <=4:
  print(counter)
  counter +=1

print("Il cliente sceglie una portata delle 4")
if(print):
  print("Ordine confermato, se rientra nei 4 piatti")
else:
  print("ordine non preso")

print("Le persone si presentano")
print("Dati del cliente:")

class Persona:

    def __init__(self,a,b):
        self.nome = a
        self.num_telefono = b

    def presentazione(self):
      print("Piacere mi chiamo", self.nome, "il mio numero di telefono è", self.num_telefono)

giulio = Persona("Giulio",1234567891)
giulio.presentazione()
anna = Persona("Anna",234567891)
anna.presentazione()
roby = Persona("Roby",5678901234)
roby.presentazione()

print("Dati Camerieri")
class Persona:
  def __init__(self,c,d):
    self.nome = c
    self.anni_servizio = d

  def presentazione(self):
    print("Salve mi chiamo", self.nome, "lavoro qui da", self.anni_servizio, "anni")

sara = Persona("Sara",4)
sara.presentazione()
giacomo = Persona("Giacomo",7)
giacomo.presentazione()
sofia = Persona("Sofia",2)
sofia.presentazione()

print("consegna conto ai Clienti")
class Persona:
  def __init__(self,a,b,c,d):
    self.portate = a
    self.nome = b
    self.prezzo = c
    self.quantità = d

  def conto(self):
    print("il numero della mia portata è", self.portate, "mi chiamo", self.nome, "ho speso", self.prezzo, " e ho preso un singolo piatto", self.quantità)

giulio = Persona(3,"Giulio", "5.00 euro", 1)
giulio.conto()
anna = Persona(1,"Anna", "8.00 euro", 1)
anna.conto()
roby = Persona(4,"Roby","15.00 euro",1)
roby.conto()
