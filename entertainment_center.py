import fresh_tomatoes
import media

# Object of our movie information, could be passed in by REST API too...
movies = [
    {
        'title': 'Star Wars',
        'synopsis': 'The Imperial Forces -- under orders from cruel Darth Vader ' + \
            '(David Prowse) -- hold Princess Leia (Carrie Fisher) hostage, in their efforts ' + \
            'to quell the rebellion against the Galactic Empire. Luke Skywalker (Mark Hamill) ' + \
            'and Han Solo (Harrison Ford), captain of the Millennium Falcon, work together with the ' + \
            'companionable droid duo R2-D2 (Kenny Baker) and C-3PO (Anthony Daniels) to rescue the ' + \
            'beautiful princess, help the Rebel Alliance, and restore freedom and justice to the Galaxy.',
        'poster': 'https://images-na.ssl-images-amazon.com/images/I/81P3lDJbjCL._SY550_.jpg',
        'clip': 'https://www.youtube.com/watch?v=vZ734NWnAHA',
        'ratingIdx': 2,
        'released': 'May 25, 1977 (USA)'
    },
    {
        'title': 'Wings',
        'synopsis': 'With World War I afoot, David Armstrong (Richard Arlen) and Jack Powell ' + \
        '(Charles "Buddy" Rogers) join the military with an eye toward flying American fighter ' + \
        'planes. They leave behind Mary Preston (Clara Bow), a local girl who\'s in love ' + \
        'with David but committed to Jack. Dispatched to France as newly minted pilots, the ' + \
        'men take to the skies in one of the war\'s climactic air battles, and as frantic ' + \
        'Mary longs for the safe return of both men, one pays the ultimate price for his bravery.',
        'poster': 'http://t3.gstatic.com/images?q=tbn:ANd9GcSF_w0NVRfbg2255NttkG8gF_KoY3xqeagT2KbA8khA70yqIRTd',
        'clip': 'https://www.youtube.com/watch?v=d3RSUn0Jy9k',
        'ratingIdx': 2,
        'released': 'January 5, 1929 (USA)'
    },
    {
        'title': 'Cashback',
        'synopsis': 'A young insomniac attempts to cope with his sleepless nights ' + \
            'by taking a job at a local supermarket, only to discover that he ' + \
            'possesses a curious coping mechanism in the debut feature from ' + \
            'Academy-Award nominated filmmaker Sean Ellis.',
        'poster': 'http://www.gstatic.com/tv/thumb/dvdboxart/167373/p167373_d_v8_aa.jpg',
        'clip': 'https://www.youtube.com/watch?v=siXe9XC723s',
        'ratingIdx': 3,
        'released': 'May 9, 2008 (United Kingdom)'
    },
]

movie_array = []

for entry in movies: # For each movie in the object, create a new instance of Movie()
    entry = media.Movie(entry['title'], entry['synopsis'],
        entry['poster'], entry['clip'], entry['ratingIdx'], entry['released'])

    movie_array.append(entry) # Append the entry to the array

fresh_tomatoes.open_movies_page(movie_array) # Open our page using the array provided