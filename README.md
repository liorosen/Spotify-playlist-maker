# Spotify Playlist Maker

**Spotify Playlist Maker** is a Python-based application that generates Spotify playlists based on the Billboard Hot 100 charts for a specified date. By combining web scraping techniques with the Spotify API, it allows users to recreate historical music charts as Spotify playlists.

## Features

- **Date-Specific Playlist Generation**: 
  Enter a date to fetch the Billboard Hot 100 chart for that week and create a corresponding Spotify playlist.
  
- **Web Scraping with BeautifulSoup**: 
 Extracts song titles and artists from Billboard's website using the BeautifulSoup library.
  
- **Spotify API Integration via Spotipy**: 
  Authenticates and interacts with the Spotify API to search for songs and create playlists directly in the user's Spotify account.
  
- **Data Persistence**: 
  Saves detailed song data, including metadata and Spotify URIs, in a text file for future reference.

## Dependencies

- **Python 3.x**: Ensure Python is installed on your system.
- **BeautifulSoup4**: For web scraping.
- **Spotipy**: A lightweight Python library for the Spotify Web API.
- **Requests**: For making HTTP requests.
- **dotenv**: To manage environment variables.

## Notes

- The application relies on the availability and accuracy of the Billboard website and the Spotify catalog.
- Some songs from older charts may not be available on Spotify.
- Ensure your Spotify account has the necessary permissions to create playlists.
