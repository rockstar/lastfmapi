import json
import urllib
import urllib2


LASTFM_API_ENDPOINT = 'http://ws.audioscrobbler.com/2.0/'

class LastFmApiException(Exception):
    '''A blank exception specific to LastFmApi.'''


class LastFmApi(object):
    '''An interface to the Last.fm api.

    This class dynamically resolves methods and their parameters. For instance,
    if you would like to access the album.getInfo method, you simply call
    album_getInfo on an instance of LastFmApi.
    '''

    def __init__(self, key):
        self.__api_key = key

    def __getattr__(self, name):
        if name.startswith('__'):
            raise AttributeError()

        def generic_request(*args, **kwargs):
            params = dict(kwargs)
            params['method'] = name.replace('_', '.')
            return self.__send(params)

        generic_request.__name__ = name
        return generic_request

    def __send(self, params):
        params['api_key'] = self.__api_key
        params['format'] = 'json'

        headers = {
            'User-Agent:': 'lastfmapi',
        }

        params = urllib.urlencode(params)
        request = urllib2.Request(LASTFM_API_ENDPOINT, params, headers)
        response = urllib2.urlopen(request).read()

        s = json.loads(response)
        if s.has_key('error'):
            raise LastFmApiException(s['message'])
        return s
