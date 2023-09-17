import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import os
#declarar variable principales
os.environ['SPOTIPY_CLIENT_ID'] = 'af44c3d096224e8480cd7ef0e9af1a11'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'b57a6fce8e9d4f77be13fdaa158ae2c9'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://google.com/'
cid = 'af44c3d096224e8480cd7ef0e9af1a11'
secret = 'b57a6fce8e9d4f77be13fdaa158ae2c9'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
scope = 'user-library-read playlist-modify-public'
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager,auth_manager=SpotifyOAuth(scope=scope))
playlist_id='spotify:playlist:5ZzsovDgANZfiXgRrwq5fw'


#codigo buenazo


def show_tracks(results):
	for idx in range(0, len(results['items']), 100):
		for item in results['items'][idx:idx+100]:
			uris = item['track']['uri'] 
			sp.playlist_add_items(playlist_id, uris)
			track = item['track']
			print("%32.32s %s" % (track['artists'][0]['name'], track['name']))


results = sp.current_user_saved_tracks()
show_tracks(results)

while results['next']:
	results = sp.next(results)
	show_tracks(results)