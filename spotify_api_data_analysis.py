"""
SPOTrend - Spotify Top Tracks Analysis
Spotify API Analysis File

This script retrieves data for the top 50 streamed songs on Spotify for the year 2023 and analyzes the various
associated features of a song (e.g., danceability, valence, acousticness, etc.). The script uses the Spotify API to
retrieve information about songs and their audio features. The script then finishes by exporting a csv file named
"top_tracks_2023_w_audio_features.csv".

Functions:
    get_top_tracks_2023(sp, num_tracks=50):
        Retrieves data for the top tracks of 2023 from a specified Spotify playlist.
        Returns a list of dictionaries with track data and a list of track IDs.

    get_audio_features(sp, track_ids):
        Retrieves audio features for a list of track IDs using the Spotify API.
        Returns a list of dictionaries with audio features.

    def combine_track_data_and_features(tracks, audio_features):
        Combine track details and audio features.

Dependencies:
    'spotipy': A python library to interact with the Spotify Web API
        https://spotipy.readthedocs.io/en/2.22.1/#installation

    'pandas': A library for data manipulation and analysis
        https://pandas.pydata.org/docs/

    'matplotlib' and 'seaborn': libraries for data visualization
        https://matplotlib.org/stable/index.html
        https://seaborn.pydata.org/

Spotify Web API:
    The Spotify Web API allows developers to access Spotify's music catalog and user data, such as tracks, artists,
    albums, and playlists, as well as user-specific data like saved tracks and playlists. The API provides endpoints
    for retrieving data, managing user libraries, and controlling playback.
        https://developer.spotify.com/dashboard/55e572910988419c891409b23a51f3a7
        Client ID: 55e572910988419c891409b23a51f3a7
        Client Secret: 736730bc0e9540c3b2dc0dcc3767307a

Usage:
    - Instantiate a Spotify client using the spotipy library and your client credentials.
    - Call the get_top_tracks_2023 function to retrieve the top tracks and track IDs.
    - Use the track IDs to call the get_audio_features function for retrieving audio features.
    - Perform further data analysis and visualization as needed.
    - When ran, this file produces a .csv file titled 'top_tracks_2023_w_audio_features.csv'.

Author:
    Christiaan Kenjee Koh

Date:
    April 2024

"""


# Importing pandas library for data analytics
import pandas as pd

# Importing Spotipy library to interact with Spotify API
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API Client details
client_id = '55e572910988419c891409b23a51f3a7'
client_secret = '736730bc0e9540c3b2dc0dcc3767307a'

# Authenticate using Client ID and Client Secret
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)


# Retrieving data for most streamed songs on Spotify for 2023
def get_top_tracks_2023(sp, num_tracks=50):
    # Get the top tracks playlist for 2023
    playlist_uri = 'spotify:playlist:37i9dQZF1DX18jTM2l2fJY'
    results = sp.playlist_tracks(playlist_uri, limit=num_tracks)

    tracks = []
    track_ids = []
    for item in results['items']:
        track = item['track']
        track_data = {
            'track_ids': track['id'],
            'track_name': track['name'],
            'artist_name': ', '.join([artist['name'] for artist in track['artists']]),
            'released_year': track['album']['release_date'][:4],
            'streams': track['popularity'],  # Popularity as a proxy for streams
            # Add more fields as needed from track and audio features
        }
        tracks.append(track_data)
        track_ids.append(track['id'])  # Collecting track IDs
    return tracks, track_ids


# Retrieving additional audio features
def get_audio_features(sp, track_ids):
    audio_features = sp.audio_features(track_ids)
    return audio_features


# Combine track details and audio features
def combine_track_data_and_features(tracks, audio_features):
    data = pd.DataFrame(tracks)
    audio_features_df = pd.DataFrame(audio_features)
    combined_df = pd.concat([data, audio_features_df], axis=1)
    return combined_df


# Example usage
tracks, track_ids = get_top_tracks_2023(sp)
top_tracks_2023_audio_features = get_audio_features(sp, track_ids)

# Combine track data and audio features into a DataFrame
top_tracks_2023_w_audio_features = combine_track_data_and_features(tracks, top_tracks_2023_audio_features)

# Export top_tracks_2023_w_audio_features dataframe into a .csv file
top_tracks_2023_w_audio_features.to_csv('top_tracks_2023_w_audio_features.csv')
