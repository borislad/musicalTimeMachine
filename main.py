from bs4 import BeautifulSoup
import requests
import spotipy
from datetime import datetime
from spotipy.oauth2 import SpotifyOAuth

if __name__ == '__main__':
    # date input validation
    format = "%Y-%m-%d"
    date_is_incorrect = True
    while date_is_incorrect:
        date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
        try:
            datetime.strptime(date,format)
            date_is_incorrect = False
        except ValueError:
            print("This is the incorrect date string format. It should be YYYY-MM-DD")

    # Scraping Billboard 100
    # specify the url
    response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(response.text, 'html.parser')
    song_names_spans = soup.find_all("span", class_="chart-element__information__song")
    song_names = [song.getText() for song in song_names_spans]

    client_id = "YOUR CLIENT ID"
    client_secret = "YOUR CLIENT SECRET"
    redirect_uri = "http://example.com"
    scope = "playlist-modify-private"

    # Spotify Authentication
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope,
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    user_id = sp.current_user()["id"]
    print(user_id)

    # Searching Spotify for songs by title
    song_uris = []
    year = date.split("-")[0]
    for song in song_names:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        print(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")

    playlist_name = f"{date} Billboard 100"

    # Creating a new private playlist in Spotify
    playlist = sp.user_playlist_create(user=user_id,
                                       name=playlist_name,
                                       public=False,
                                       description="A playlist that was created by The Musical Time Machine "
                                                   "as part of the Data Science Course of Naya College and "
                                                   "submitted to Guy Uziel. ")
    print(playlist)
    # Adding songs found into the new playlist
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
