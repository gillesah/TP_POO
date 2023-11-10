class Entreprise():
    """
    Une entreprise possède un nom, une adresse et un numéro SIRET
    Le numéro siret est vérifiable et doit comporter 14 chiffres 
    attributs : 
        nom : str
        adresse: str
        siret: str (en protected)

    """

    def __init__(self, nom: str, adresse: str, siret: str) -> None:
        self.nom = nom
        self.adresse = adresse
        self._siret = siret

    @property
    def siret(self):
        return self._siret

    @siret.setter
    def siret(self, valeur):
        if valeur.isdigit() and len(valeur) == 14:
            self._siret = valeur
        else:
            raise ValueError(
                "Le numéro SIRET doit être composé de 14 chiffres.")

    def __str__(self) -> str:
        return f"L'entreprise {self.nom}, ayant son siège social au {self.adresse}, possède le numéro de SIRET {self.siret}"


# instantation de l'entreprise Cochonou
cochonou = Entreprise("Cochonou", "2 RUE EDISON 69500 BRON", "40316137500310")
print(cochonou)

# on change le numéro de siret, si le numéro siret est mauvais, alors il y aura ValueError qui va s'afficher
try:
    cochonou.siret = "39023904919938"
except ValueError as e:
    print(e)


print(cochonou)
