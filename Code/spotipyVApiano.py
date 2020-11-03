import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from pprint import pprint
import pandas as pd


# Authentication

credentials = json.load(open('authorization.json'))
client_id = credentials['client_id']
client_secret = credentials['client_secret']

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# Getting VA values from tracks in albums

albumTracks = json.load(open("albumTracks.json"))

albumNames = []
albumArtists = []
albumTrackNames = []
albumTrackValence = []
albumTrackArousal = []

for i in range(len(albumTracks)):

    URI = albumTracks[i]["uri"]

    album = sp.album(URI)

    artistName = album['artists'][0]['name']

    print(album['name'])

    # pprint(album)

    trackList = []

    for track in album['tracks']['items']:
        print(track['name'])

        albumNames.append(album['name'])
        albumArtists.append(artistName)
        albumTrackNames.append(track['name'])

        trackURI = track['uri']
        trackList.append(trackURI)

    features = sp.audio_features(trackList)

    for j in range(len(features)):
        valence = features[j]['valence']
        arousal = features[j]['energy']

        albumTrackValence.append(valence)
        albumTrackArousal.append(arousal)

    print("\n\n")




# Getting VA values from individual tracks

indivTracks = json.load(open("singleTracks.json"))

indivTrackURIs = []
indivTrackAlbums = []
indivTrackArtists = []
indivTrackNames = []
indivTrackValence = []
indivTrackArousal = []

for i in range(len(indivTracks)):
    indivTrackURIs.append(indivTracks[i]["uri"])
    indivTrackAlbums.append(indivTracks[i]["album"])
    indivTrackArtists.append(indivTracks[i]["artist"])
    indivTrackNames.append(indivTracks[i]["trackName"])

    print(indivTracks[i]["trackName"])

features = sp.audio_features(indivTrackURIs)

for j in range(len(features)):
        valence = features[j]['valence']
        arousal = features[j]['energy']

        indivTrackValence.append(valence)
        indivTrackArousal.append(arousal)




# Saving everything in one CSV

allArtistNames = albumArtists + indivTrackArtists
allAlbumNames = albumNames + indivTrackAlbums
allTrackNames = albumTrackNames + indivTrackNames
allTrackValence = albumTrackValence + indivTrackValence
allTrackArousal = albumTrackArousal + indivTrackArousal

allData = []
allData.append(allArtistNames)
allData.append(allAlbumNames)
allData.append(allTrackNames)
allData.append(allTrackValence)
allData.append(allTrackArousal)

allDF = pd.DataFrame(allData)

allDF = allDF.transpose()

allDF.columns = ['Composer', 'Work', 'Track', 'Valence', 'Arousal']

allDF.to_csv('pianoMidiVA.csv', index=False)


# pprint(features)


# The 5th album URI has most of Beethoven. Eliminate duplicate tracks (the 3 parts of sonata 8, moonlight sonata 3 parts)  -- done
# rachmaninov+godowsky album has 3 duplicates of bach   -- done
# liszt hungarian rhapsodies remove extra   -- done
# remove clementi opus 36 3 duplicates  -- done
# Brahms op 116 and 117 --> delete extra  -- done
# chopin mazurka op 33 remove 1 and 3   -- done
# chopin etudes 25 -- keep just 1 2 3 4 11 12   -- done
# liszt remove grande etude paganini duplicate no 5 -- done

# brworkstudio
# itmusicstudio
