import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

cid = "e95094f95f8b4a5089263af1484fec78"
secret = "471a83d85bf843c99f368383a7a5c0e4"
username = "elizabethrose20@yahoo.com"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-library-read playlist-read-private'
token = util.prompt_for_user_token(username, scope, redirect_uri = 'https://example.com/callback/')

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

print(sp)