import webbrowser

class Video():
    '''Video Class to define a video object'''

    def __init__(self, title, poster_image, clip_youtube):
        '''Init function for Video Class

        Arguments:
            title {String} -- Title of the video
            poster_image {String} -- URL to image for the poster
            clip_youtube {String} -- YouTube URL to the clip/trailer
        '''
        self.title = title
        self.poster_image_url = poster_image
        self.clip_youtube_url = clip_youtube

    def show_clip(self):
        '''Show the clip for the selected video file

        Opens the youtube URL (in a lightbox in this example)
        '''
        webbrowser.open(self.trailer_youtube_url)


class Movie(Video):
    '''Class to specifically define an object as a movie

    Extends:
        Video

    Variables:
        VALID_RATINGS {list} -- List of available ratings for motion pictures
    '''

    # Stored here because TV Shows have a different rating system
    VALID_RATINGS = ["G","PG","PG-13","R","NC-17","NR"]

    def __init__(self, title, storyline, poster_image, clip_youtube, rating, released):
        '''Initialize the movie object

        Arguments:
            title {String} -- Movie title
            storyline {String} -- Story synopsis for the movie
            poster_image {String} -- URL to poster image
            clip_youtube {String} -- URL to YouTube trailer
            rating {String} -- Rating of the film by MPAA
        '''
        Video.__init__(self, title, poster_image, clip_youtube)
        self.synopsis = storyline
        self.released = released
        self.rating = self.VALID_RATINGS[rating]
