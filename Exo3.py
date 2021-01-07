class DateNaissance:
    def __init__(self,jour,mois,annee):
        self.jour = jour;
        self.mois = mois;
        self.annee = annee;

    def affiche(self):
        return str(self.jour) + " / "+ str(self.mois)+" / "+str(self.annee)



class Personne():
    def __init__(self,nom,prenom,dateDeNaissance):
        self.nom = nom
        self.prenom = prenom
        self.dateDeNaissance = dateDeNaissance

    def afficher(self):
        print("Nom : ",self.nom)
        print("Prénom : ",self.prenom)
        print("Date de naissance : ",self.dateDeNaissance.affiche())


class Employe(Personne):
    def __init__(self,nom,prenom,dateDeNaissance,salaire):
        super().__init__(nom,prenom,dateDeNaissance)
        self.salaire = salaire

    def afficher(self):
        print("Nom : ",self.nom)
        print("Prénom : ",self.prenom)
        print("Date de naissance : ",self.dateDeNaissance.affiche())
        print("Salaire : ",round(self.salaire,2) )


class Chef(Employe):
    def __init__(self,nom,prenom,dateDeNaissance,salaire,service):
        super().__init__(nom,prenom,dateDeNaissance,salaire)
        self.service = service

    def afficher(self):
        print("Nom : ",self.nom)
        print("Prénom : ",self.prenom)
        print("Date de naissance : ",self.dateDeNaissance.affiche())
        print("Salaire : ",round(self.salaire,2) )
        print("Service : ",self.service)