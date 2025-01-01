This project is a Billboard Hot 100 Spotify Playlist Generator that allows users to travel back in time and generate Spotify playlists for specific dates based on the Billboard Hot 100 chart. It combines web scraping, data extraction, and Spotify API integration to create a seamless experience for music enthusiasts.

Key Features:
Date-Based Playlist Creation:

Input any date after August 4, 1958, to fetch the Billboard Hot 100 chart for that week.
Automatically generates a Spotify playlist for the selected chart.
Web Scraping:

Utilizes BeautifulSoup to scrape song titles from the Billboard website.
Spotify API Integration:

Authenticates using Spotipy to interact with Spotify's API.
Searches for songs on Spotify, retrieves metadata, and adds tracks to a private playlist.
Error Handling:

Ensures valid date input and handles cases where songs are not found on Spotify.
Output:

Generates a text file with details of all songs, including names, artists, and Spotify URLs.
Provides the Spotify playlist URL for easy sharing and access.
Technical Highlights:
Python Libraries:
BeautifulSoup for web scraping.
Spotipy for Spotify API interaction.
requests for HTTP requests.
Dynamic Data Handling:
Automatically calculates the most recent Friday as the latest valid date for charts.
User-Friendly Interface:
Prompts for input and provides clear feedback for invalid dates or missing data.
This project is a robust example of combining web scraping with API integration to solve real-world problems and provide a rich user experience.

