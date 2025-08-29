class Defaultlist(list):
    
    def __init__(self, liste, defaultwert = None):
        list.__init__(self, liste)
        self.defaultwert = defaultwert
        
    def __getitem__(self, pos):
        #2 Fälle: vorhanden oder nicht
        if pos >= len(self):
            return self.defaultwert
        else:
            #Aufruf der Methode der Superklasse
            return list.__getitem__(self, pos)
        
        
kursliste = Defaultlist(["Samuel","Marwin","Marie","Silas"],"nicht im Kurs")
for i in range(10):
    print(kursliste[i])

print("___________________________\n")
#ohne Angabe Defaultwert
kursliste = Defaultlist(["Samuel","Marwin","Marie","Silas"])
for i in range(10):
    print(kursliste[i])

print("___________________________\n")
zahlenliste = Defaultlist([17,8,9,3,7],0)
for i in range(10):
    print(zahlenliste[i])