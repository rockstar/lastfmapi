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
