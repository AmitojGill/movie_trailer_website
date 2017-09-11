import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story 3",
						"A story of a boy and his toys that come to life.",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=ZZv1vki4ou4")

#print toy_story.storyline

avatar = media.Movie("Avatar 2",
					"A marine on an alien planet",
					"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					"https://www.youtube.com/watch?v=vGNGGBzaNQ0")

#print avatar.storyline
#avatar.show_trailer()

planet_of_the_apes = media.Movie("War for the Planet of the Apes",
								"Caesar (Andy Serkis) and his apes are forced into a deadly conflict with an army of humans led by a ruthless colonel (Woody Harrelson).",
								"https://upload.wikimedia.org/wikipedia/en/d/d7/War_for_the_Planet_of_the_Apes_poster.jpg",
								"https://www.youtube.com/watch?v=GGol29RlI3k")

#planet_of_the_apes.show_trailer()

dangal = media.Movie("Dangal",
					"Former wrestler Mahavir Singh Phogat (Aamir Khan) trains young daughters Geeta (Fatima Sana Shaikh) and Babita (Sanya Malhotra) to follow in his footsteps and become world-class grapplers.",
					"https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
					"https://www.youtube.com/watch?v=x_7YlGv9u1g")

wonder_woman = media.Movie("Wonder Woman",
							"Before she was Wonder Woman (Gal Gadot), she was Diana, princess of the Amazons, trained to be an unconquerable warrior.",
							"https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
							"https://www.youtube.com/watch?v=F0lZgaz0CIE")

skull_islan = media.Movie("Skull Island",
							"Scientists, soldiers and adventurers unite to explore a mythical, uncharted island in the Pacific Ocean.",
							"https://upload.wikimedia.org/wikipedia/en/3/34/Kong_Skull_Island_poster.jpg",
							"https://www.youtube.com/watch?v=GIQMnSpspx0")

movies = [toy_story, avatar, planet_of_the_apes, dangal,wonder_woman, skull_islan]

#fresh_tomatoes.open_movies_page(movies)

#print media.Movie.VALID_RATINGS

#print media.Movie.__doc__, " <<< __doc__"
#print media.Movie.__name__, "<< __name__"
#print media.Movie.__module__, "<<< __module__"
#print media.Movie.__dict__, "<< __dict__"