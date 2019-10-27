# MovieAPI
A small restAPI to search for movie and television shows

Uses the external API at https://developers.themoviedb.org/3/getting-started/introduction.
You will need to request an API key from there and add it as the Heroku Environment Variable MOVIE_API_KEY

Valid Uses:

    /search?query={SEARCH_TERM}&page=PAGE_NUM

This will default to page 1

    /movie/${ID_NUMBER}

    /show/${ID_NUMBER}

ID numbers are the ID numbers used by themoviedb API
