from googleapiclient.discovery import build
from getpass import getpass 
from textwrap import wrap
import argparse

# Get replies for a comment
def get_replies(parent_id):

    request = youtube.comments().list(
        part="snippet",
        parentId=parent_id,
        maxResults=100,
        textFormat="plainText"
    )

    while request:
        response = request.execute()

        for item in response["items"]:
            snippet = item["snippet"]

            global replies
            replies += 1
            print(file=out)
            print("    ",snippet.get("authorDisplayName"),snippet.get("publishedAt"), "Likes:", snippet.get("likeCount"), file=out)
            for line in wrap(snippet.get("textDisplay"),80):
                print("    ",line, file=out)
        request = youtube.comments().list_next(request, response)


# main
comments = 0
replies = 0

parser = argparse.ArgumentParser(prog='GetYouTubeComments',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description='''
GetYouTubeComments extracts comments and replies of a YouTube video in a human readable text format. To use it you need 
to provide a Google Youtube API key and YouTube video id.  
'''
)

parser.add_argument('--apikey', nargs='?', default='', help='Your YouTube API key, default query')
parser.add_argument('--videoid', nargs='?', default='', help='YouTube video id, default query')
args = parser.parse_args()
if args.apikey != '': 
    API_KEY = args.apikey
else:
    API_KEY = getpass(prompt='Your YouTube API key: ')
if args.videoid != '':
    VIDEO_ID = args.videoid
else:
    VIDEO_ID = input('YouTube video id: ')
youtube = build("youtube", "v3", developerKey=API_KEY)


request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=VIDEO_ID
    )
response = request.execute()
out = open("YouTube"+VIDEO_ID+".txt", "w")
print("Video: ",VIDEO_ID, file=out)
print("Title: ",response["items"][0]["snippet"]["title"],file=out)
print("Published: ",response["items"][0]["snippet"]["publishedAt"],file=out)
    
request = youtube.commentThreads().list(
    part="snippet,replies",
    videoId=VIDEO_ID,
    maxResults=100,
    textFormat="plainText"
)

while request:
    response = request.execute()

    for item in response["items"]:
        top = item["snippet"]["topLevelComment"]
        snippet = top["snippet"]

        comment_id = top["id"]

        comments += 1
        print(file=out)
        print(file=out)
        print(snippet.get("authorDisplayName"),snippet.get("publishedAt"), "Likes:", snippet.get("likeCount"), file=out)
        for line in wrap(snippet.get("textDisplay"),80):
            print(line, file=out)
        # fetch replies
        reply_count = item["snippet"].get("totalReplyCount", 0)

        if reply_count > 0:
            get_replies(comment_id)

    request = youtube.commentThreads().list_next(request, response)

print(comments,"comments and", replies,"replies saved to", "YouTube"+VIDEO_ID+".txt.")
