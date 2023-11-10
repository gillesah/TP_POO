import random
import string


class Client:
    """
    Classe représentant un client. Cette classe permet de créer des objets de clients d'une banque
    Attributs : 
        nom(str) : le nom du client
        prenom(str) : le prénom du client
        adresse(str) : adresse du client
        nir (str) : numéro de sécurité social (NIR) du client qui doit comporter 15 chiffres
    Raise : ValueError si le NIR ne comprend pas 15 chiffres
    """

    def __init__(self, nom: str, prenom: str, adresse: str, nir: str) -> None:
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        if self.valide_nir(nir):
            self.nir = nir
        else:
            raise ValueError(f"Le NIR doit être composé de 15 chiffres")

    def valide_nir(self, nir):
        if len(nir) != 15 or not nir.isdigit():
            return False
        else:
            return True

    def __str__(self) -> str:
        return f"Prénom : {self.prenom} \nNom: {self.nom} \nAdresse : {self.adresse}\nNIR : {self.nir}"


class CompteBancaire:
    """
    Classe représentant le compte bancaire : cette classe permet de créer des comptes bancaires rattachés à des clients
    Attributs : 
        date_creation (str) : Date de la creation du compte
        client (Client) : client du compte bancaire, depuis la classe client
        solde (float) : solde du compte

    Propriété statique : 
        somme_comptes (list): la méthode somme_tous_comptes fait la somme de tous les soldes des comptes bancaires

    """
    somme_comptes = []

    def __init__(self, date_creation: str, client: Client, solde: float):
        self.date_creation = date_creation
        self.client = client
        self.solde = solde
        self.identifiant = self.creation_identifiant()
        CompteBancaire.somme_comptes.append(solde)

    # méthode factory
    def compte_factory(cls, date_creation, client, identifiant, solde):
        return cls(date_creation=date_creation, client=client, identifiant=identifiant, solde=solde)

    def __str__(self) -> str:
        return f"Compte bancaire n°{self.identifiant}\nPrénom : {self.client.prenom} \nNom: {self.client.nom}"

    def creation_identifiant(self):
        pass

    def format_date(self):
        # Fonction pour avoir la date au format DDMMYYYY

        partie = self.date_creation.split("/")
        return f"{partie[0]}{partie[1]}{partie[2]}"

    def creation_identifiant(self):
        # générer les 4 lettres aléatoires

        # création de l'alphabet
        lettres = string.ascii_lowercase
        # choix de 4 lettres aléatoirements
        lettres_aleatoires = ''.join(random.choice(lettres) for _ in range(4))
        identifiant = lettres_aleatoires.upper() + self.format_date()
        return identifiant

    def somme_tous_comptes():
        # calcul de la somme de tous les comptes bancaires

        return sum(CompteBancaire.somme_comptes)

    def __eq__(self, other: object) -> bool:
        # Méthode magique pour voir l'égalité

        return self.solde == other.solde


client1 = Client("Durand", "Philippe",
                 "2 rue de la blanche colombe 75014 PARIS", "189309390299392")

print(client1)
compte1 = CompteBancaire("13/09/2016", client1, 1042.3)
compte2 = CompteBancaire("13/12/2012", client1, 3040.0)


print("\n______impression du compte bancaire n°1______ \n ")
print(compte1)
print("*"*30)

print("\n______impression du compte bancaire n°2______ \n")
print(compte2)

print("*"*30)
# vérification si 2 comptes sont égaux au niveau du solde
print(compte1 == compte2)

print("*"*30)
# avoir la somme de tous les comptes bancaire

print(
    f"Somme de tous les comptes bancaires : {CompteBancaire.somme_tous_comptes()}")
print("*"*30)
