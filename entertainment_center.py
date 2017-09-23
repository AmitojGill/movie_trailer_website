#!/usr/bin/env python2.7

import fresh_tomatoes
import media


'''avatar: movie title, storyline, poster image and movie trailer.'''
avatar = media.Movie(
    "Avatar 2",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=vGNGGBzaNQ0",
    "PG-13"
    )

'''plante_of_the_apes: movie title, storyline, poster
image and movie trailer.'''
planet_of_the_apes = media.Movie(
    "War for the Planet of the Apes",
    "Caesar (Andy Serkis) and his apes are forced into a deadly conflict with"
    "an army of humans led by a ruthless colonel (Woody Harrelson).",
    "https://upload.wikimedia.org/wikipedia/en/d/d7/War_for_the_Planet_of_the_Apes_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=GGol29RlI3k",
    "PG-13"
     )

'''dangal: movie title, storyline, poster image and movie trailer.'''
dangal = media.Movie(
    "Dangal",
    "Former wrestler Mahavir Singh Phogat (Aamir Khan) trains young daughters"
    "Geeta (Fatima Sana Shaikh) and Babita (Sanya Malhotra) to follow"
    "in his footsteps and become world-class grapplers.",
    "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
    "https://www.youtube.com/watch?v=x_7YlGv9u1g",
    "PG-13"
    )

'''wonder_woman: movie title, storyline, poster image and movie trailer.'''
wonder_woman = media.Movie(
    "Wonder Woman",
    "Before she was Wonder Woman (Gal Gadot), she was Diana,"
    "princess of the Amazons, trained to be an unconquerable warrior.",
    "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",  # NOQA
    "https://www.youtube.com/watch?v=F0lZgaz0CIE",
    "PG-13"
    )

'''skull_island: movie title, storyline, poster image and movie trailer.'''
skull_island = media.Movie(
    "Skull Island",
    "Scientists, soldiers and adventurers unite to explore a mythical,"
    "uncharted island in the Pacific Ocean.",
    "https://upload.wikimedia.org/wikipedia/en/3/34/Kong_Skull_Island_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=GIQMnSpspx0",
    "PG-13"
     )

'''captain_america: movie title, storyline, poster image and movie trailer.'''
captain_america = media.Movie(
    "Captain America: Civil War",
    "Captain America: Civil War is a 2016 American superhero"
    "film based on the Marvel"
    "Comics character Captain America, produced by Marvel Studios and"
    "distributed by Walt Disney Studios Motion Pictures.",
    "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=1deLLCy73Qc",
    "PG-13"
    )

'''moana: movie title, storyline, poster image and movie trailer.'''
moana = media.Movie(
    "Moana",
    "In Ancient Polynesia, when a terrible curse incurred by the Demigod Maui"
    "reaches Moana's island, she answers the Ocean's call to seek out the"
    "Demigod to set things right.",
    "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",
    "https://www.youtube.com/watch?v=Dadu2KLjMVM",
    "PG"
    )

'''magnificent_seven: movie title, storyline, poster image and
movie trailer.'''
magnificent_seven = media.Movie(
    "The Magnificent Seven",
    "Seven gunmen in the old west gradually come together to help a poor"
    "village against savage thieves.",
    "https://upload.wikimedia.org/wikipedia/en/e/ec/Magnificent_Seven_2016.jpg",  # NOQA
    "https://www.youtube.com/watch?v=zqyaLkYEDhU",
    "PG-13"
    )

movies = [
    skull_island,
    planet_of_the_apes,
    moana,
    magnificent_seven,
    captain_america,
    dangal]

fresh_tomatoes.open_movies_page(movies)
