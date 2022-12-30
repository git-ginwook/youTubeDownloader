# source reference: https://www.geeksforgeeks.org/youtube-mediaaudio-download-using-python-pafy/
# pafy documentation: https://pythonhosted.org/pafy/index.html?highlight=save
# note: backend_youtube_dl.py line 53 and 54 updated (https://github.com/mps-youtube/pafy/pull/288)
import pafy


# download audio only
def audioDL(url):
    target = pafy.new(url)
    print(target.title)
    best_audio = target.getbestaudio(preftype="m4a")
    print(best_audio.bitrate, best_audio.extension, best_audio.get_filesize())
    best_audio.download(filepath="/Users/ginwooklee_air/Downloads")


# download video and audio
def videoDL(url):
    target = pafy.new(url)
    print(target.title)
    best_video = target.getbest()
    print(best_video.resolution, best_video.extension)
    best_video.download(filepath="/Users/ginwooklee_air/Downloads")


# ask user whether to download audio or video
while True:
    try:
        form = int(input("audio(1) or video(2): "))
    except ValueError:
        print("please enter a valid input (1 or 2).")
        continue
    if form == 1 or form == 2:
        print(f"You selected: {form}")
        break
    else:
        print("input must be either audio(1) or video(2)")

# ask user whether to download a single or multiple links
while True:
    try:
        count = int(input("single(1) or multi(2): "))
    except ValueError:
        print("please enter a valid input (1 or 2).")
        continue
    if count == 1 or count == 2:
        print(f"You selected: {count}")
        break
    else:
        print("input must be either single(1) or multi(2)")

# if user selected single link
if count == 1:
    while True:
        try:
            singleURL = input("enter YouTube URL: ")
        except ValueError:
            print("URL cannot be empty.")
            continue
        if singleURL:
            print(f"You selected: {singleURL}")
            break
        else:
            print("paste the YouTube URL.")

# read YouTubeList.txt file
urlList = open("YouTubeList.txt", 'r')


if form == 1:
    if count == 1:
        audioDL(singleURL)
    else:
        [audioDL(url) for url in urlList]

else:
    if count == 1:
        videoDL(singleURL)
    else:
        [videoDL(url) for url in urlList]

# close YouTubeList.txt file
urlList.close()

