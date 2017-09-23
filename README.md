# movie_trailer_website
A website with my favorite movie listing and trailers

Objective of this program is to generate a HTML webpage from python file.
Content of website is taken form Wikipedia and Youtube. 

## **Start Here**

### **Tools you need**
- Your choice of computer (Mac, Linux or Windows)
- Python2.7 - [Download here](https://www.python.org/downloads/)
- Code editor such as Sublime Text - [Download here](https://www.sublimetext.com/)

### **Directory Files:**
- entertainment_center.py
- fresh_tomatoes.py
- media.py

### **Follow These steps**
* Make sure you have Python2.7 installed
* clone this repository - https://github.com/AmitojGill/movie_trailer_website.git
* To add your favorite movies open entertainment_center.py in Sublime Text

** Create a new instance for each movie you wish to add as example below:
```
'''avatar: movie title, storyline, poster image and movie trailer.'''
avatar = media.Movie(
    "Avatar 2",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=vGNGGBzaNQ0",
    "PG-13"
    )
```
** Next add your newlly created movies to the movies list
```
movies = [
    skull_island,
    planet_of_the_apes,
    moana,
    magnificent_seven,
    captain_america,
    dangal]

```
* To change layout and any html/css code edit fresh_tomatoes.py
* If you want to add more content per movie, you will need to chenge all three fiels (entertainment_center.py, media.py, and fresh_tomatoes.py)


**Good Luck!**

