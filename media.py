import webbrowser

class Movie():
	"""This class provides a way to store movie realted information."""
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, moive_title, movie_storyline, poster_image, trailer_youtube,movie_rating):
		'''
		OBJECTIVE: __init__ function is exicuted when new object is created using class Movie

		INPUT: There are total 6 in puts: self as a string, movie_title as a string, 
		movie_storyline as a string, poster_image as a string (link to image),
		trailer_youtube as a string (link to Youtube video), and movie_rating as a string. 

		OUTPUT: Initallize all the variable 
		'''
		self.title = moive_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.rating = movie_rating

	def show_trailer(self):
		'''
		OJECTIVE: show_trailer method palyes Youtube video when it is called

		INPUT: takes in self as input in a string format

		OUTPUT: Plays the Youtube video.
		'''
		webbrowser.open(self.trailer_youtube_url)
