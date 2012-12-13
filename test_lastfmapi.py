import unittest

import lastfmapi


SAMPLE_API_KEY = '1b21ef07e3ef3a12197c1d7b7b41b227'

class SuperTestCase(unittest.TestCase):

    def assertRaisesWithMessage(self, exc, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            self.assertFail()
        except exc as e:
            self.assertEqual(e.message, msg)


class TestApi(SuperTestCase):

    def test_api(self):
        api = lastfmapi.LastFmApi(SAMPLE_API_KEY)
        data = api.album_getinfo(artist='Cher', album='Believe')
        self.assertEqual(
            data['album']['mbid'],
            '86b5434d-9479-35e3-98ca-8fbcfcf4e357')

    def test_api_invalid(self):
        api = lastfmapi.LastFmApi(SAMPLE_API_KEY)
        self.assertRaisesWithMessage(
            lastfmapi.LastFmApiException,
            'You must supply either an album & artist name or an album mbid.',
            api.album_getinfo)


class TestApiAlbumMethods(SuperTestCase):
    '''Tests to make sure all unauthenticated album methods work.'''

    def setUp(self):
        self.api = lastfmapi.LastFmApi(SAMPLE_API_KEY)
        self.kwargs = {
            'artist': 'cher',
            'album': 'believe',
            'country': 'united states',
        }

    def test_api_album_getBuylinks(self):
        data = self.api.album_getBuylinks(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_album_getInfo(self):
        data = self.api.album_getInfo(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_album_getTags(self):
        data = self.api.album_getTags(user='RJ', **self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_album_getTopTags(self):
        data = self.api.album_getTopTags(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_album_search(self):
        data = self.api.album_search(**self.kwargs)
        self.assertFalse(data.has_key('error'))


class TestApiArtistMethods(SuperTestCase):
    '''Tests to make sure all unauthenticated artist methods work.'''

    def setUp(self):
        self.api = lastfmapi.LastFmApi(SAMPLE_API_KEY)
        self.kwargs = {
            'artist': 'cher',
        }

    def test_api_artist_getCorrection(self):
        data = self.api.artist_getCorrection(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_artist_getEvents(self):
        data = self.api.artist_getEvents(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_artist_getInfo(self):
        data = self.api.artist_getInfo(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_artist_getPastEvents(self):
        data = self.api.artist_getPastEvents(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_artist_getPodcast(self):
        data = self.api.artist_getPodcast(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_artist_getShouts(self):
        data = self.api.artist_getShouts(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_artist_getSimilar(self):
        data = self.api.artist_getSimilar(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_artist_getTags(self):
        data = self.api.artist_getTags(user='RJ', **self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_artist_getTopAlbums(self):
        data = self.api.artist_getTopAlbums(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_artist_getTopFans(self):
        data = self.api.artist_getTopFans(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_artist_getTopTags(self):
        data = self.api.artist_getTopTags(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_artist_getTopTracks(self):
        data = self.api.artist_getTopTracks(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_artist_search(self):
        data = self.api.artist_search(**self.kwargs)
        self.assertFalse(data.has_key('error'))


class TestApiTrackMethods(SuperTestCase):
    '''Tests to make sure all unauthenticated track methods work.'''

    def setUp(self):
        self.api = lastfmapi.LastFmApi(SAMPLE_API_KEY)
        self.kwargs = {
            'artist': 'radiohead',
            'track': 'creep',
            'country': 'united states',
        }

    def test_api_track_getBuylinks(self):
        data = self.api.track_getBuylinks(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_track_getCorrection(self):
        data = self.api.track_getCorrection(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_track_getFingerprintMetadata(self):
        data = self.api.track_getFingerprintMetadata(
            fingerprintid='1234', **self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_track_getInfo(self):
        data = self.api.track_getInfo(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_track_getShouts(self):
        data = self.api.track_getShouts(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_track_getSimilar(self):
        data = self.api.track_getSimilar(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_track_getTags(self):
        data = self.api.track_getTags(user='RJ', **self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_track_getTopFans(self):
        data = self.api.track_getTopFans(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_track_getTopTags(self):
        data = self.api.track_getTopTags(**self.kwargs)
        self.assertFalse(data.has_key('error'))

    def test_api_track_search(self):
        data = self.api.track_search(**self.kwargs)
        self.assertFalse(data.has_key('error'))

