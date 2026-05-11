# GetYouTubeComments
Download comments and replies of a YouTube video as human readable text file. To use it you need 
to provide a Google YouTube API key and a YouTube video id. Please refer to [YouTube Data API Overview](https://developers.google.com/youtube/v3/getting-started) for creating your API key.

# Installation

## From Binary Release
For Windows 11 and Ubuntu 24.04 a [PyInstaller](https://pyinstaller.org/en/stable/) standalone onefile binary build is provided in the [Releases](https://github.com/rwhomeaudio/GetYouTubeComments/releases). Download it and extract the executable. If it doesn't work on your system or a different platform is required install it from source.

## From Source
1. Download and install Python 3.X on your system: [https://www.python.org/downloads/](https://www.python.org/downloads/)
1. Open a shell / command prompt and install matplotlib, numphy and scipy:
```
pip install --upgrade google-api-python-client
```

3. Optionally install git command line client: [https://github.com/git-guides/install-git](https://github.com/git-guides/install-git)
1. Download FreqRespGraph:
   - Clone git repository: `git clone https://github.com/rwhomeaudio/GetYouTubeComments` or
   - Download ZIP archive from [https://github.com/rwhomeaudio/GetYouTubeComments](https://github.com/rwhomeaudio/GetYouTubeComments) using "Code->Download ZIP" button.
1. Test the installation by running: `python GetYouTubeComments.py -h`

# Usage
```
python GetYouTubeComments.py -h
usage: GetYouTubeComments [-h] [--apikey [APIKEY]] [--videoid [VIDEOID]]

GetYouTubeComments extracts comments and replies of a YouTube video in a human readable text format. To use it you need 
to provide a Google YouTube API key and YouTube video id.  

options:
  -h, --help           show this help message and exit
  --apikey [APIKEY]    Your YouTube API key, default query
  --videoid [VIDEOID]  YouTube video id, default query
```
# Examples
```
python GetYouTubeComments.py
Your YouTube API key: 
YouTube video id: OoGxMMJkQfQ
198 comments and 278 replies saved to YouTubeOoGxMMJkQfQ.txt.

python GetYouTubeComments.py --apikey "A.....................................8" --videoid "OoGxMMJkQfQ"
198 comments and 278 replies saved to YouTubeOoGxMMJkQfQ.txt.
```
# Limitations
Altough the YouTube WebUI shows a hierarchy of replies the [YouTube Data API](https://developers.google.com/youtube/v3) only provides a list of comments and for each comment a flat list of replies. So replies on replies as just shown a replies on the initial comment instead of a nested hierarchy.
