import webbrowser


class Movie():
    __name__ = "Movie"
    __module__ = "Media"
    def __init__(self, title, storyline, poster, trailerURL):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailerURL

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
