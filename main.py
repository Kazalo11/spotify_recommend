import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

cid = '3e9a51fcef934a0aba70f488dbb3dae2'
secret = 'a89ffc5d583c4f9d883db236f1dc7942'
uri = 'http://localhost:8080'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
scope = 'user-top-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=cid, client_secret=secret, redirect_uri=uri))

top_artists = sp.current_user_top_artists(limit=50, time_range='long_term')['items']
names, artists_id = [], []

for artist in top_artists:
    names.append(artist['name'])
    artists_id.append(artist['id'])


related_artists = {}
for artist_id in artists_id:
    related_artist_information = sp.artist_related_artists(artist_id)['artists']
    for related_artist in related_artist_information:
        related_artist_id = related_artist['id']
        if related_artist_id not in artists_id:
            related_artists[related_artist_id] = related_artists.get(related_artist_id, 0) + 1

related_artists = {k: v for k, v in sorted(related_artists.items(), key=lambda item: item[1], reverse=True)}

data = {}
related_artist_names = []
related_artists_top_tracks = []
related_artist_top_album = []

def top_tracks(artist):
    artist_top_tracks_information = sp.artist_top_tracks(artist,'US')['tracks']
    artist_top_tracks = []
    for track in artist_top_tracks_information:
        artist_top_tracks.append(track['name'])
    return ';'.join(artist_top_tracks)

def top_album(artist):
    artist_top_album_information = sp.artist_albums(artist,album_type='album')['item']
    artist_albums = []
    for album in artist_top_album_information:
        artist_albums.append(album['name'])
    return ';'.join(artist_albums)



for related_artist in related_artist_id:
    related_artist_names.append(sp.artist(related_artist)['name'])
    related_artists_top_tracks.append(top_tracks(related_artist))













