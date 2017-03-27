import webbrowser

""" Movie class consist of a constructor i.e __init__() which takes title, movie_quote, poster_image_url,trailer_youtube_url as an argument and a function
    known as play_trailer which plays the youtube trailer for the movie. """

class Movie:
    def __init__(self, title, movie_quote, poster_image_url,trailer_youtube_url):
        self.title = title
        self.movie_quote = movie_quote
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url

    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


