# YouTube Downloader
## Features
- Download YouTube video or audio using `youTubeDownloader.py`
- Use a text editor (e.g., .txt) to list up multiple YouTube URLs for download
## Installation
Install `pafy`(ver.0.5.5) and `youtube-dl`(ver.2021.12.17)
```
pip install pafy
pip install youtube_dl
```
The current `pafy` throws [an error](https://github.com/mps-youtube/pafy/pull/288) 
when given YouTube URL has zero 'like' or 'dislike'.<br>
To resolve this issue, go to `backend_youtube_dl.py` and change line 53 and 54:
```
self._likes = self._ydl_info.get('like_count',0)
self._dislikes = self._ydl_info.get('dislike_count',0)
```
## User Guide
### 1. Run the Python script
Run `youTubeDownloader.py` in an IDE of your choice or in a terminal
```
python3 youTubeDownloader.py
```
### 2. Select download format
Enter 1 for audio or 2 for video
### 3. Specify whether to download multiple files
Enter 1 for a single download or 2 for multiple downloads
### 3-1. Paste the YouTube URL for a single download
Enter the YouTube link to start downloading
### 3-2. Paste the YouTube URLs for multiple downloads
Open `YouTubeList.txt` file and paste each YouTube link on a new line
> Multiple YouTube links should be listed in the text file **before** running the python script
## References
1. [YouTube Media/Audio Download using Python – pafy](https://www.geeksforgeeks.org/youtube-mediaaudio-download-using-python-pafy/)
2. [Pafy Documentation](https://pythonhosted.org/pafy/#)
3. [Get video info even if no likes/dislikes exist #288](https://github.com/mps-youtube/pafy/pull/288)
4. <https://github.com/mps-youtube/pafy>
5. <https://pypi.org/project/pafy/>
