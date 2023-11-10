from modules.exercice_4 import Movie
import time


def main():

    while True:
        user_ask = input(
            "Welcome to your film library \n What do you want to do ? \n C - Create \n R - Read \n U - Update \n D - Delete \n Q - Exit \n ANSWER : ").lower()

        if user_ask == "c":
            movie_title = input("Movie title :")
            movie_date = input("Release date (DD/MM/YYYY) : ")
            movie_description = input("description : ")
            Movie.add_movie(movie_title, movie_date, movie_description)
            time.sleep(2)
            print("Full list of movies")
            Movie.complete_list()
            time.sleep(2)

            print("*"*30)

        elif user_ask == "r":
            search_or_see = input(
                "Do you want to : \n S - Search a film \n V - view the list of movies  \n ANSWER : ").lower()
            if search_or_see == "s":
                movie_title_search = input(
                    "please enter the title of the film : ")
                Movie.search_movie(movie_title_search)
            elif search_or_see == "v":
                print("Full list of movies")
                Movie.complete_list()
                time.sleep(2)
            else:
                print("please choose beetween S or V")

        elif user_ask == "u":
            movie_title = input(
                "what is the title of the movie you want to update? ")
            new_title = input(
                "what is the new title (leave blank if no change) ?")
            new_date = input(
                "what is the new date (leave blank if no change) ?")
            new_description = input(
                "what is the new description (leave blank if no change) ?")
            Movie.update_movie(movie_title, new_title,
                               new_date, new_description)
        elif user_ask == "d":
            delete_title = input(
                "what is the title of the film you want to delete? ")
            Movie.delete_movie(delete_title)
        elif user_ask == "q":
            print("""
                                                            
                                                            
  ___  ___  ___   _   _  ___  _   _   ___  ___   ___  _ __  
 / __|/ _ \/ _ \ | | | |/ _ \| | | | / __|/ _ \ / _ \| '_ \ 
 \__ \  __/  __/ | |_| | (_) | |_| | \__ \ (_) | (_) | | | |
 |___/\___|\___|  \__, |\___/ \__,_| |___/\___/ \___/|_| |_|
                   __/ |                                    
                  |___/                                     
""")
            break
        else:
            print("*"*30)

            print("please choose C R U D or Q ")
            print("*"*30)
            time.sleep(2)


main()
