import call_youtube_API
import json
from Favorites import Favorites

global favorites_list
favorites_list = []

global readable_favorites_list
readable_favorites_list = []

def welcome_user():
    print "Welcome to the yoga video finder!"

def ask_user_input():
    user_choice = int(
        raw_input("Please select one of the following options: 1 - Find new yoga video \n2 - View my favorites"))
    return user_choice

def find_display_video():
    yoga_type = raw_input(
        "What type of yoga are you interested in doing? Options include: \nHatha \nVinyasa \nIyengar \nBikram \nKundalini \nAshtanga")
    yoga_level = raw_input(
        "How difficult would you like the video to be? Options include: \nEasy \nIntermediate \nHard")
    num_results = int(raw_input("How many videos would you like? Please enter an integer."))

    search_terms = yoga_level, yoga_type, "yoga"

    # call youtube API
    youtube_json_results = call_youtube_API.youtube_search(search_terms, num_results)

    # loop through results and display them to the user
    for idx, yoga_video in enumerate(youtube_json_results):
        yoga_video_title = yoga_video["title"]
        yoga_video_id = yoga_video["id"]
        yoga_video_url = "www.youtube.com/watch?v=%s" % (yoga_video_id)
        print idx, "- %s (%s)" % (yoga_video_title, yoga_video_url)

    return youtube_json_results


def save_video(displayed_videos):
    my_video = raw_input("Would you like to save any of the videos? Please input Yes or No.")

    if my_video.lower() == "yes":
            video_number = int(raw_input("What video number would you like to save? Integers only."))
            unique_tag = raw_input(
                "Please give your video a unique identifier.")
            readable_favorites_list.append(unique_tag)
            saved_video = displayed_videos[video_number]
            unique_tag = Favorites(saved_video["id"], saved_video["title"])
            favorites_list.append(unique_tag)
            print "Your video has been saved."

    else:
        print "Your videos have not been saved."

    return favorites_list


def more_videos():
    user_continue = raw_input("Would you like to look for another video or view favorites? Input yes or no.")
    if user_continue.lower() == "no":
        print "Thank you for using the yoga video finder!"
        exit()
    else:
        return True


def display_favorites():
    if len(favorites_list) > 1:
        for idx, tag in enumerate(readable_favorites_list):
            print idx, "-", tag
        selected_video = int(raw_input("Which video number would you like more details for? Please enter an integer."))
        call_selected_video = favorites_list[selected_video]
        yoga_video_url = "www.youtube.com/watch?v=%s" % (call_selected_video.videoId)
        print "%s (%s)" % (call_selected_video.title, yoga_video_url)

    elif len(favorites_list) == 1:
        print "You have one video saved."
        selected_video = favorites_list[0]
        yoga_video_url = "www.youtube.com/watch?v=%s" % (selected_video.videoId)
        print "%s (%s)" % (selected_video.title, yoga_video_url)

    else:
        print "You have no favorites saved."
        return False

def main():
    # welcomes user to the YouTube video finder
    welcome_user()

    while (True):
        user_input = ask_user_input()
        if user_input == 1:
            found_videos = find_display_video()
            favorites = save_video(found_videos)
            more_videos()
        elif user_input == 2:
            display_favorites()
            more_videos()

main()