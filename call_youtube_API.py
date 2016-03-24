
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(query, max_results=1):
  youtube=build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
 
  #calls the search.list method to retrieve results matching query term
  search_response = youtube.search().list(
    q=query,
    part="id,snippet",
    maxResults=max_results
  ).execute()

  #extracts the fields we want to keep from each result 
  results_transform = lambda search_result: {
    'id': search_result['id']['videoId'],
    'title': search_result['snippet']['title']
  }

  #only keeps the video results
  result_filter = lambda search_result: search_result['id']['kind'] == 'youtube#video'

  #retrieves the max # of results we wanted and avoids transferring useless reults
  search_response = youtube.search().list(q=query, part="id,snippet", type="video", maxResults=max_results).execute()

  #returns the results
  return map(results_transform, filter(result_filter, search_response.get("items", [])))