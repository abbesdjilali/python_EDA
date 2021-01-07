class ObjetAEnvoyer:
    def __init__(self,adresseDistinantion,adresseExpedition,poids,modeExpedition):
        self.adresseDistinantion = adresseDistinantion
        self.adresseExpedition=adresseExpedition
        self.poids =poids
        self.modeExpedition = modeExpedition



class Lettre(ObjetAEnvoyer):
    def __init__(self,adresseDistinantion,adresseExpedition,poids,modeExpedition,formatExpedition):
        super().__init__(adresseDistinantion, adresseExpedition, poids, modeExpedition)
        self.formatExpedition = formatExpedition
        self.tarifA4 = 2.50
        self.tarifA3 = 3.50
        self.prix =  self.tarifA4 * 1.0 * (self.poids / 1000) if self.formatExpedition == "A4" else self.tarifA3 * 1.0 * self.poids * 1000


    def calculTimbre(self):
        return 2 * self.prix  if self.modeExpedition == "expresse" else self.prix

    def ToString(self):
        print("Lettre :")
        print("Adresse destination: ", self.adresseDistinantion);
        print("Adresse Expedition: ", self.adresseExpedition);
        print("Poids : %.2f"% float(self.poids), "grammes");
        print("Mode : ",self.modeExpedition)
        print("Format : ",self.formatExpedition)
        print("Prix : %.2f"% self.calculTimbre());






class Colis(ObjetAEnvoyer):
    def __init__(self,adresseDistinantion,adresseExpedition,poids,modeExpedition,volume):
        super().__init__(adresseDistinantion,adresseExpedition,poids,modeExpedition)
        self.volume = volume
        self.prix = 0.25 * self.volume * (self.poids / 1000)

    def calculTimbre(self):
        return 2 * self.prix if self.modeExpedition == "expresse" else self.prix

    def ToString(self):
        print("Colis :")
        print("Adresse destination: ", self.adresseDistinantion);
        print("Adresse Expedition: ", self.adresseExpedition);
        print("Poids : %.2f"% float(self.poids), "grammes");
        print("Mode : ",self.modeExpedition)
        print("Volume : ",self.volume, " litres")
        print("Prix du timbre: ", self.calculTimbre());





