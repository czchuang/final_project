#welcome message
print "Welcome to the yoga video finder! Are you ready to find your next online yoga class?"

#determine yoga type

yoga_type = raw_input ("What kind of yoga are you interested in? Please select from: Hatha, Vinyasa, Iyengar, Bikram, Kundalini, or Ashtanga.")

#determine video length 

video_length = raw_input ("What long would you like your video to be? Please select from (in minutes): 15, 30, 45, 60.")

#determine video difficulty 

yoga_level = raw_input ("How difficult would you like the video to be? Please select from: Easy, Moderate, Hard.")

#call YouTube API

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

with open("api_keys.py") as youtube_key_file:
	DEVELOPER_KEY = youtube_key_file.read()
	YOUTUBE_API_SERVICE_NAME = "youtube"
	YOUTUBE_API_VERSION = "v3"

	def youtube_search(query, max_results=3):
  		
  		youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

  		search_response = youtube.search().list(
   			q=query,
    		part="id,snippet",
    		maxResults=max_results
  		).execute()

    	result_transform = lambda search_result: {
    							'id': search_result['id']['videoId'],
    							'title': search_result['snippet']['title'],
    							'thumbnail': search_result['snippet']['thumbnails']['defaault'],
    							'data': search_result['snippet']['publishedAt']
    						}	

    	result_filter = lambda search_result: search_result['id']['kind'] == 'youtube#video'

    	return map(result_transform, filter(result_filter, search_response,get("items", [])))



#http://www.programmableweb.com/news/how-to-query-youtube-through-its-python-apis/how-to/2014/03/26
