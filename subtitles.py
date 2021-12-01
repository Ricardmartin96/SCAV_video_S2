import subprocess
import requests

if __name__ == "__main__":

    # DOWNLOAD SUBTITLES: get a download link and write it in a new .srt file

    link = "https://dl.opensubtitles.org/es/download/file/1957437052"
    sub = requests.get(link)
    with open("subtitles.srt", "w") as file:
        file.write(sub.text)


    # INTEGRATE SUBTITLES IN VIDEO
    subprocess.call(["ffmpeg", "-i", "newBBB_cut.mp4", "-vf",
                     "subtitles=subtitles.srt", "BBB_with_subtitles.mp4"])



