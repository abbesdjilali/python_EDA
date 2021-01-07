from CompteBancaire import CompteBancaire;
from Exo2 import Point
from Exo3 import Personne,Employe,DateNaissance,Chef
from Exo4 import Lettre,Colis

#Exo 1
compte1 = CompteBancaire('Duchmol', 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()
compte2 = CompteBancaire()
compte2.depot(25)
compte2.affiche()

#Exo 2
P1 = Point(2,3);
P1.ToString();
P2=Point(1,-5,6)
P2.ToString()

#Exo3
P=Personne("Ilyass","Math",DateNaissance(1,7,1982))
P.afficher()
E=Employe("Ilyass","Math",DateNaissance(1,7,1985),7865.548)
E.afficher()
Ch=Chef("Ilyass","Math",DateNaissance(1,7,1988),7865.548,"Ressource humaine")
Ch.afficher()

#Exo 4

L1=Lettre("Lille","Paris",80,"normal","A4")
L1.ToString()

C1=Colis("Marrakeche","Barcelone",3500,"expresse",2.25)
C1.ToString()