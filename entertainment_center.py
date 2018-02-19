import media
import fresh_tomatoes

#instanciate movies
old_boy = media.Movie('Old Boy',
                      'http://img.moviepostershop.com/oldboy-movie-poster-2003-1020263711.jpg',
                      'https://www.youtube.com/watch?v=2HkjrJ6IK5E')

what_we_do = media.Movie('What We Do in the Shadows',
                         'https://zuts.files.wordpress.com/2015/07/what-we-do-in-the-shadows-poster.jpg',
                         'https://www.youtube.com/watch?v=Cv568AzZ-i8')

memento = media.Movie('Memento',
                      'http://is4.mzstatic.com/image/thumb/Video/v4/77/74/b7/7774b71c-2fa2-cf98-79ff-373565164d51/source/1200x630bb.jpg',
                      'https://www.youtube.com/watch?v=MFF0C3j6YDw')

#list of movies
movies = [old_boy,what_we_do,memento]

#this funtion generates an HTML file which shows poster and title of movies
fresh_tomatoes.open_movies_page(movies)
