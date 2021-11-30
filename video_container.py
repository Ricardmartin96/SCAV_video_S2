import subprocess

if __name__ == "__main__":

    # First, we cut the original video into 1 min.
    subprocess.call(["ffmpeg", "-ss", str(0), "-i", "Big_Buck_Bunny.mp4", "-c",
                     "copy", "-t", str(60), "newBBB_cut.mp4"])

    # Then, we export BBB(1min) audio as MP3 stereo track.
    # ffmpeg -i newBBB_cut.mp4 -vn -c:a libmp3lame BBB_audio.mp3 where vn is
    # no video and with c:a I change the audio codec.
    subprocess.call(["ffmpeg", "-i", "newBBB_cut.mp4", "-vn", "-c:a",
                     "libmp3lame", "BBB_audio.mp3"])

    # Then we export BBB(1min) audio in AAC w/ lower bitrate
    subprocess.call(["ffmpeg", "-i", "newBBB_cut.mp4", "-vn", "-c:a",
                     "aac","-b:a", "64k", "BBB_audio.aac"])
    # pasem de 128k bits/s (bitrate del mp3 per defecte) a 64kbits/s

    # Finally, we merge the three files in a new .mp4 file
    # ffmpeg -i newBBB_cut.mp4 -i BBB_audio.aac -i BBB_audio.mp3 -c:v copy -c:a
    # copy -map 0:0 -map 1:a -map 2:a joined_files.mp4

    # we copy the video and audio codecs, but we map each of the 3 streams
    # (video, audio1 and audio2). map 0:0 takes the video from the first stream
    # map 1:a takes the audio from the 1rs audio stream and map 2:a takes the
    # audio from the 2nd stream
    subprocess.call(["ffmpeg", "-i", "newBBB_cut.mp4",  "-i", "BBB_audio.mp3",
                      "-i", "BBB_audio.aac", "-c:v", "copy", "-c:a",
                     "copy", "-map", "0:0",  "-map", "1:a",  "-map", "2:a",
                     "video_container.mp4"])