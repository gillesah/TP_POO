import json
from datetime import datetime
# le lien du fichier json // attention il faut être situé dnas le dossier exercice 4
json_path = "movies.json"


class Movie:
    """
    la classe Movie permet la création d'un objet film.
    Attributs : 
    titre : str = le titre du film
    date_de_sortie : str = la date de sortie du film
    description : str = la description du film

    """

    def __init__(self, titre: str, date_de_sortie: str, description: str) -> None:
        self.titre = titre
        self.date_de_sortie = date_de_sortie
        self.description = description

    def __str__(self) -> str:
        return f"nom du film {self.titre} | Date de sortie : {self.date_de_sortie} | description : {self.description}"

    def to_dict(self):
        return {"titre": self.titre,
                "date_de_sortie": self.date_de_sortie,
                "description": self.description}

    def load_json():
        # on load le fichier json pour pouvoir l'utiliser dans les différentes méthodes
        try:
            with open(json_path, "r") as f:
                data = json.load(f)
                return data

        except FileNotFoundError:
            return None

    @classmethod
    def save_json(cls, data):
        # on sauvegarde dans le fichier json
        with open(json_path, "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def add_movie(cls, titre: str, date_de_sortie: str, description: str):
        """ajout d'un film

        Args:
            titre (str): titre du nouveau film
            date_de_sortie (str): date de sortie du nouveau film
            description (str): _description du film
        """
        movie_data = {
            "titre": titre, "date_de_sortie": date_de_sortie, "description": description}
        data = cls.load_json()
        movies = data.get("movies", [])
        for movie in movies:
            if movie["titre"] == titre:
                print(f"Le film {titre} est déjà dans la liste.")
                return

        movies.append(movie_data)
        print(f"le film {titre} a bien été ajouté")

        cls.save_json(data)

    @classmethod
    def complete_list(cls):
        # pour afficher la liste des films par ordre croissant
        data = cls.load_json()
        movies = data["movies"]

        def date_converter(movie):
            return datetime.strptime(movie["date_de_sortie"], "%d/%m/%Y")
        sorted_movies = sorted(movies, key=date_converter)

        for movie in sorted_movies:
            print(
                f"Titre du film : {movie['titre']} \nDate de sortie : {movie['date_de_sortie']} \nDescription : {movie['description']}")
            print(f"*"*30)

    @classmethod
    def delete_movie(cls, titre):
        """_Supprimer un film

        Args:
            titre (_type_): titre du film pour le retrouver et le supprimer
        """
        # movie = cls(titre)
        data = cls.load_json()
        movies = data["movies"]
        for movie_data in movies:
            if titre == movie_data["titre"]:
                movies.remove(movie_data)
                print(f"le film {titre} a été supprimé")
                break
        else:
            print(
                f"le film {titre} n'est pas présent dans la liste et donc ne peut pas être supprimé")
        cls.save_json(data)

    @classmethod
    def update_movie(cls, titre: str, new_titre: str = None, new_date_de_sortie: str = None, new_description: str = None):
        """_mettre à jour un film. il est possible de mettre à jour un film par son titre, sa date ou sa description

        Args:
            titre (str): titre du film à modifier 
            new_titre (str, optional): nouveau titre   Defaults to None.
            new_date_de_sortie (str, optional) nouvelle date de sortie Defaults to None.
            new_description (str, optional): nouvelle description  Defaults to None.
        """
        data = cls.load_json()
        movies = data.get("movies", [])

        # Recherche du film par titre
        for movie_data in movies:
            if movie_data["titre"] == titre:
                # Suppression de l'ancien film
                movies.remove(movie_data)
                break

        # Création du film mis à jour
        updated_movie = {
            "titre": new_titre if new_titre else titre,
            "date_de_sortie": new_date_de_sortie if new_date_de_sortie else movie_data.get("date_de_sortie", ""),
            "description": new_description if new_description else movie_data.get("description", "")
        }

        # Ajout du film mis à jour à la liste
        movies.append(updated_movie)

        cls.save_json(data)
        print(f"Le film {titre} a été mis à jour.")

    @classmethod
    def search_movie(cls, titre: str):
        data = cls.load_json()
        movies = data.get("movies", [])
        for movie in movies:
            if movie["titre"] == titre:
                print("Résultat de votre recherche")
                print(
                    f"Titre du film : {movie['titre']} \nDate de sortie : {movie['date_de_sortie']} \nDescription : {movie['description']}")


""" TESTS """
# Movie.add_movie("titre de votre premier film",
#                 "12/12/2022", "votre description")
# Movie.add_movie("film2", "12/12/2021", "lorem lorem")
# Movie.add_movie("film3", "12/12/2011", "3 lorem lorem")

# Movie.add_movie("film4", "12/12/2011", "4 lorem lorem")
# Movie.add_movie("film5", "12/02/2011", "5 lorem lorem")

# Movie.delete_movie("film4")
# Movie.update_movie("film5", "Super Film 5")
# Movie.search_movie("film2")
# Movie.complete_list()
# movies.append(film1)
# sauv_json()
# print(film1)
