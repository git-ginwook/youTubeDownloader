import pafy
import os

# specify download folder to 'Downloads'
path = os.path.expanduser("~")+"/Downloads/"


# download audio only
def audioDL(url):
    target = pafy.new(url)
    print(target.title)
    best_audio = target.getbestaudio(preftype="m4a")
    print(best_audio.bitrate, best_audio.extension, best_audio.get_filesize())
    best_audio.download(filepath=path)


# download video
def videoDL(url):
    target = pafy.new(url)
    print(target.title)
    best_video = target.getbest()
    print(best_video.resolution, best_video.extension)
    best_video.download(filepath=path)


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

# download audio
if form == 1:
    # download a single file
    if count == 1:
        audioDL(singleURL)
    # download multiple files
    else:
        # read YouTubeList.txt file
        urlList = open("YouTubeList.txt", 'r')
        [audioDL(url) for url in urlList]
        # close YouTubeList.txt file
        urlList.close()

# download video
else:
    # download a single file
    if count == 1:
        videoDL(singleURL)
    # download multiple files
    else:
        # read YouTubeList.txt file
        urlList = open("YouTubeList.txt", 'r')
        [videoDL(url) for url in urlList]
        # close YouTubeList.txt file
        urlList.close()
