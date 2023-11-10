from dataclasses import dataclass, field


@dataclass
class DatabaseConnection:
    type: str
    utilisateur: str
    _motdepasse: str
    hote: str = field(default="localhost")
    nb_instance:  int = field(default=0, init=False, repr=False)

    # Getter - setter de mot de passe

    @property
    def motdepasse(self):
        return self._motdepasse

    @motdepasse.setter
    def motdepasse(self, valeur):
        self._motdepasse = valeur

    @staticmethod
    def nombre_instance():
        return f"La classe DatabaseConnection possède actuellement {DatabaseConnection.nb_instance} instance(s)."


    @classmethod
    def factory(cls, type: str, utilisateur: str, motdepasse: str, hote: str = "localhost"):
        return cls(type=type, utilisateur=utilisateur, _motdepasse=motdepasse, hote=hote)

    def __str__(self) -> str:
        return f"""type -> "{self.type}", hôte -> "{self.hote}", utilisateur -> "{self.utilisateur}", mot de passe -> "{self.motdepasse}"."""
    # incrémenter à chaque création d'un objet :

    def __post_init__(self):
        DatabaseConnection.nb_instance += 1


mariadb = DatabaseConnection("mariadb", "root", "1234", "76.287.872.12")
print(mariadb)
bdd = DatabaseConnection("MySql", "root", "1234")
print(bdd)

bdd2 = DatabaseConnection.factory(
    type="PostgreSQL", utilisateur="admin", motdepasse="motdepassecompliqué")
print(bdd2)
