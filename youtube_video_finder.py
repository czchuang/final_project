import call_youtube_API
import json
import Favorites

print "Welcome to the yoga video finder!"

user_choice = int(raw_input("Please select one of the following options: 1 - Find new yoga video \n2 - View my favorites"))

if user_choice == 1:

	yoga_type = raw_input("What type of yoga are you interested in doing? Options include: \nHatha \nVinyasa \nIyengar \nBikram \nKundalini \nAshtanga")
	yoga_level = raw_input ("How difficult would you like the video to be? Options include: \nEasy \nHModerate \nIntense")
	num_results = int(raw_input("How many videos would you like? Please enter an integer."))

	search_terms = yoga_level, yoga_type, "yoga"

	#call youtube API
	youtube_json_results = call_youtube_API.youtube_search(search_terms,num_results)

	#loop through the json results to parse out info for each video result

	for yoga_video in youtube_json_results:
		yoga_video_title = yoga_video["title"]
		yoga_video_id = yoga_video["id"]
		yoga_video_url = "www.youtube.com/watch?v=%s" % (yoga_video_id)
		print index, "%s (%s)" % (yoga_video_title, yoga_video_url)

	my_video = raw_input("Would you like to save this video? Please input Yes or No.")

	if my_video.lower() == "yes":
		favorites_list = []
		unique_tag = raw_input("Please give your video a unique identifier. Only alphanumeric characters and no spaces.")
		unique_tag = Favorites(yoga_video_id,yoga_video_title,yoga_video_url)
		favorites_list.append(unique_tag)
		print "Your video has been saved. Thank you for using the yoga video finder."
	else:
		print "Thank you for using the yoga video finder."

elif user_choice == 2:
	print favorites_list
