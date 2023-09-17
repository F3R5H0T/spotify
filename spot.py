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

biblio = sp.current_user_saved_tracks()
lista = sp.playlist_items(playlist_id, fields=None, limit=100, offset=0, market=None, additional_types=('track', 'episode'))

urisb=[]
uris=[]

#uris de playlist
for x in range(1,40):
	for idx in range(0,len(lista['items']),100):
		for i in lista['items'][idx:idx+100]:
			uris.append(i['track']['uri'])

#uris de likes
def show_tracks():
	for idx in range(0,len(biblio['items']),100):
		for i in biblio['items'][idx:idx+100]:
			urisb=i['track']['uri']
			if urisb in uris:
				print("{}     {}-{}".format(True, i['track']['name'],i['track']['artists'][0]['name']))
			else:
				print("{}     {}-{}".format(False, i['track']['name'], i['track']['artists'][0]['name']))
				#sp.playlist_add_items(playlist_id, urisb)
			
show_tracks()
while biblio['next']:
	biblio = sp.next(biblio)
	show_tracks()