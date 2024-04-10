from bs4 import BeautifulSoup
import requests
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"
date = input("Enter the date for which you wanna search songs?YYYY-MM-DD")
response = requests.get(f"{URL}{date}/")
print(f"{URL}{date}/")
soup = BeautifulSoup(response.text, "html.parser")
songs = [soup.find(name="h3", id="title-of-a-story",
                   class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet "
                          "lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis "
                          "u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")]
songs.extend(soup.find_all(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s "
                                                                    "u-letter-spacing-0021 lrv-u-font-size-18@tablet "
                                                                    "lrv-u-font-size-16 u-line-height-125 "
                                                                    "u-line-height-normal@mobile-max "
                                                                    "a-truncate-ellipsis u-max-width-330 "
                                                                    "u-max-width-230@tablet-only"))
print(songs)
artists = soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max "
                                            "u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block "
                                            "a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only "
                                            "u-font-size-20@tablet")
artists.extend(soup.find_all(name="span",
                             class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max "
                                    "u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block "
                                    "a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"))
song_names = [' '.join(song.getText().split()) for song in songs]
artist_names = [' '.join(artist.getText().split()) for artist in artists]
print(artist_names)
client_id = "d6548bf3d3c243c095d579af3ad347f9"
client_sec = "1da22c56c59249528b9e9c790bdbf729"
redirect_uri = "https://example.com"
auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_sec, redirect_uri=redirect_uri, scope="playlist-modify-public")
sp = Spotify(auth_manager=auth_manager)
user_id = sp.current_user()['id']
artist_ind = 0
song_uris = []
for song in song_names:
    search_res = sp.search(f" artist:{artist_names[artist_ind]} track:{song}", type="track")
    artist_ind += 1
    try:
        search_uri = search_res["tracks"]["items"][0]["uri"]
        song_uris.append(search_uri)
    except IndexError:
        pass
print(song_uris)
playlist = sp.user_playlist_create(user=user_id, name=f"Top 100 songs of {date}", public=True, description="Contains "
                                                                                                            "trending"
                                                                                                            " songs "
                                                                                                            "of a "
                                                                                                            "specific "
                                                                                                            "date")
sp.user_playlist_add_tracks(user=user_id,playlist_id=playlist["id"], tracks=song_uris)

