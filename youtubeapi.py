from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
import sys

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyAGm32gvqWpE_t56luqXmNRCPBGp-mi5tk"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(options):
	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
					developerKey=DEVELOPER_KEY)
	
	# Call the search.list method to retrieve results matching the specified
	# query term.
	search_response = youtube.search().list(
		q=options.q,
		part="id,snippet",
		maxResults=options.max_results
	).execute()
	
	videos = []
	channels = []
	playlists = []
	url = []
	# Add each result to the appropriate list, and then display the lists of
	# matching videos, channels, and playlists.
	for search_result in search_response.get("items", []):
		if search_result["id"]["kind"] == "youtube#video":
			videos.append(search_result["snippet"]["title"])
			url.append("https://www.youtube.com/watch?v=" + str(search_result["id"]["videoId"]))
		
		# url.append(search_result["snippet"]["thumbnails"]["high"]["url"])
		elif search_result["id"]["kind"] == "youtube#channel":
			channels.append("%s (%s)" % (search_result["snippet"]["title"],
										 search_result["id"]["channelId"]))
		elif search_result["id"]["kind"] == "youtube#playlist":
			playlists.append("%s (%s)" % (search_result["snippet"]["title"],
										  search_result["id"]["playlistId"]))
	
	for i in range(0, len(videos), 1):
		print(str(i) + ". " + videos[i])
	print("url: \n", "\n".join(url),"\n")
	# print("Channels:\n", "\n".join(channels), "\n")
	# print("Playlists:\n", "\n".join(playlists), "\n")
	return url


def play_yt(arg):
	argparser.add_argument("--q", help="Search term", default=arg)
	argparser.add_argument("--max-results", help="Max results", default=10)
	args = argparser.parse_args()
	
	try:
		url = youtube_search(args)
		return url
	except:
		print("An HTTP error %d occurred:\n%s" + sys.exc_info()[0])
		
# play_yt("jason mraz")
