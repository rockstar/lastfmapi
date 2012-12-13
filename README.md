LastFmApi
---------

A thin but dynamic wrapper around the Last.fm api webservice found at http://ws.audioscrobbler.com/2.0/

    import lastfmapi
    
    api = lastfmapi.LastFmApi('<your api key here>')
    
    api.album_getInfo(artist='Cher', album='Believe')

For methods on the Last.fm api, simply call that method on the api object,
subsituting '_' where '.' would be.
