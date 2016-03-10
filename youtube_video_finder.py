import call_youtube_API
import json

print "Welcome to the yoga video finder. Are you ready to find your next yoga video?"

yoga_type = raw_input("What type of yoga are you interested in doing? Options include: \nHatha \nVinyasa \nIyengar \nBikram \nKundalini \nAshtanga")

yoga_level = raw_input ("How difficult would you like the video to be? Options include: \nEasy \nHModerate \nIntense")

num_results = int(raw_input("How many videos would you like? Please enter an integer."))

#call youtube API

search_terms = yoga_type, yoga_level

youtube_json_results = call_youtube_API.youtube_search(search_terms,num_results)

#loop through the json results to parse out info for each video result

for yoga_video in youtube_json_results:
	yoga_video_title = yoga_video["title"]
	yoga_video_id = yoga_video["id"]
	print "%s (www.youtube.com/%s)" % (yoga_video_title, yoga_video_id)
