import media
import fresh_tomatoes

""" Here, toy_story, avatar, school_of_rock etc. are the instances of class Movie. To call the constructor(__init__()) of class Movie, first we have to import
    media file and then we can call constructor using media.Movie(). """
toy_story = media.Movie("Toy Story","About a car","toy_story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar","About Aliens","avatar.jpg","https://www.youtube.com/watch?v=aVdO-cx-McA")
school_of_rock = media.Movie("School of Rock","About music","school_of_rock.jpg","https://www.youtube.com/watch?v=LqEszt5wG9I")
donnie_darko = media.Movie("Donnie Darko","Supernatural","donnie_darko.jpg","https://www.youtube.com/watch?v=ZZyBaFYFySk")
nocturnal_animals = media.Movie("Nocturnal Animals","Horror Thriller","nocturnal_animals.jpg","https://www.youtube.com/watch?v=juFmTNbFh8g")
prisoners = media.Movie("Prisoners","Thriller Mystery","prisoners.jpg","https://www.youtube.com/watch?v=aVdO-cx-McA")
source_code = media.Movie("Source Code","About Aliens","source_code.jpg","https://www.youtube.com/watch?v=t5roJgHV_lA")
nightcrawler = media.Movie("Nightcrawler","Murder Thriller","nightcrawler.jpg","https://www.youtube.com/watch?v=X8kYDQan8bw")
southpaw = media.Movie("SouthPaw","Fighting","southpaw.jpg","https://www.youtube.com/watch?v=Mh2ebPxhoLs")

""" To generate an html page of the Movie Trailer website, we have to call open_movies_page() function which takes the movie instances as arguments in the form
    of list """

movies = [toy_story,avatar,school_of_rock,donnie_darko,nocturnal_animals,prisoners,source_code,nightcrawler,southpaw]
fresh_tomatoes.open_movies_page(movies)
