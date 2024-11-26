import bs4
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import datetime

# Get today's date
today = datetime.date.today()

# Find the most recent Friday
offset = (today.weekday() - 4) % 7  # 4 is Friday (Monday=0, Sunday=6)
most_recent_friday = today - datetime.timedelta(days=offset)

# Define the earliest valid date (Billboard Hot 100 started on August 4, 1958)
earliest_date = datetime.date(1958, 8, 4)

# Ask the user for a date and ensure it's valid
while True:
    date_str = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ").strip()

    try:
        # Convert the input to a date object
        input_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        continue  # Ask again if the format is invalid

    # Check if the input date is before the Billboard Hot 100 existed
    if input_date < earliest_date:
        print(f"The Billboard Hot 100 didn't exist before {earliest_date}. Please enter a date after {earliest_date}.")
    # Check if the input date is after the most recent Friday (too future)
    elif input_date > most_recent_friday:
        print(f"The most recent Billboard chart date is: {most_recent_friday}. Please enter a date before {most_recent_friday}.")
    else:
        break  # Valid date entered, exit the loop

print(f"Fetching Billboard Hot 100 for {input_date}...")

# Create the request to Billboard
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
billboard_url = "https://www.billboard.com/charts/hot-100/" + input_date.strftime("%Y-%m-%d")
response = requests.get(url=billboard_url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")

# Check if songs were found
if not song_names_spans:
    print("No songs found on the Billboard page. Please check the structure of the page or the date input.")
    # Ensure a file is still created with a message
    filename = f"Billboard_100_{input_date.strftime('%Y-%m-%d')}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"No songs found for Billboard Hot 100 on {input_date.strftime('%Y-%m-%d')}\n")
    exit()

# Extract song names
song_names = [song.getText().strip() for song in song_names_spans]

# Debug: Check if song names are correctly scraped
print(f"Scraped song names: {song_names}")

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id='c3a70f492fcf48f1a002306b27e0678a',  # Your provided client ID
        client_secret='02a99997552e44bfb9e691a211ea3ca9',  # Your provided client secret
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# Open a text file to save song details
filename = f"Billboard 100 Hits of {input_date.strftime('%Y-%m-%d')}.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write(f"Billboard Hot 100 Songs for {input_date.strftime('%Y-%m-%d')}\n")
    file.write("=" * 40 + "\n\n")

    # Searching Spotify for songs by title
    song_uris = []
    year = input_date.year  # Extract the year directly
    i = 1  # Initialize i before the loop starts

    for song in song_names:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        # Extract track name, artist(s), and URL
        if result["tracks"]["items"]:  # Ensure there are results
            track = result["tracks"]["items"][0]
            track_name = track["name"]
            artists = ", ".join([artist["name"] for artist in track["artists"]])
            track_url = track["external_urls"]["spotify"]  # Extract Spotify link
            uri = track["uri"]  # Extract the URI of the track

            print(f"{i}) '{song}':\nTrack Name: {track_name}, Artists: {artists}\nURL: {track_url}\n")

            # Append the URI to the song_uris list
            song_uris.append(uri)

            # Write song details to the text file
            file.write(f"{i}) Song: {track_name}\n")
            file.write(f"   Artist(s): {artists}\n")
            file.write(f"   URL: {track_url}\n\n")
        else:
            print(f"{i}) '{song}' not found on Spotify.")
            file.write(f"{i}) '{song}' not found on Spotify.\n\n")

        i += 1  # Increment i after each iteration

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{input_date.strftime('%Y-%m-%d')} Billboard 100", public=False)
print(f"Playlist URL: {playlist['external_urls']['spotify']}")

# Write the playlist URL to the text file
with open(filename, "a", encoding="utf-8") as file:
    file.write("=" * 40 + "\n")
    file.write(f"Spotify Playlist URL: {playlist['external_urls']['spotify']}\n")

# Adding songs found into the new playlist
if song_uris:  # Only add items if the list is not empty
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
else:
    print("No valid songs found to add to the playlist.")
