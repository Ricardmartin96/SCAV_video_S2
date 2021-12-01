import subprocess
import requests

def video_motionvector_macroblocks (input, output):
    subprocess.call(["ffmpeg", "-flags2", "+export_mvs", "-i", input,
                     "-vf", "codecview=mv=pf+bf+bb",
                     output])

def video_container (input1, output1, output2, output3, output4):
    subprocess.call(["ffmpeg", "-ss", str(0), "-i", input1, "-c",
                     "copy", "-t", str(60), output1])

    subprocess.call(["ffmpeg", "-i", output1, "-vn", "-c:a",
                     "libmp3lame", output2])

    subprocess.call(["ffmpeg", "-i", output1, "-vn", "-c:a",
                     "aac", "-b:a", "64k", output3])

    subprocess.call(["ffmpeg", "-i", output1, "-i", output2,
                     "-i", output3, "-c:v", "copy", "-c:a",
                     "copy", "-map", "0:0", "-map", "1:a", "-map", "2:a",
                     output4])

def video_container_reader(input):

    file = open("video_container_data.txt", "w")
    subprocess.run(["ffprobe", input], stdout=file
                   , stderr=subprocess.STDOUT)

    file = open("video_container_data.txt", "r")
    cont = 0
    no_error = 0
    llista = []
    # reading each line
    for x in file:
        words = x.split()
        # reading each word
        for i in words:
            # guardar cada paraula en llista
            llista.append(i)
    for j in llista:
        if j == "Audio:":
            print('Audio codec: ', llista[cont + 1])
            no_error = no_error + 1
        if j == "Video:":
            print('Video codec: ', llista[cont + 1])
            no_error = no_error + 1
        if j == "bitrate:":
            print('Bit rate: ', llista[cont + 1])
        if j == "fps,":
            print('Frame rate: ', llista[cont - 1])
        cont = cont + 1

    if (no_error == 0):
        print('ERROR, no codec found')

    file.close()

def video_subtitles(input, output):

    link = "https://dl.opensubtitles.org/es/download/file/1957437052"
    sub = requests.get(link)
    with open("subtitles.srt", "w") as file:
        file.write(sub.text)
    subprocess.call(["ffmpeg", "-i", input, "-vf",
                     "subtitles=subtitles.srt", output])

if __name__ == "__main__":

    original_video = "Big_Buck_Bunny.mp4"
    input_video = "BBB_cut.mp4"

    output_video = "newBBB_cut.mp4"
    output_audio_1 = "BBB_audio.mp3"
    output_audio_2 = "BBB_audio.aac"

    mvm_output = "BBB_mv_macroblocks.mp4"
    container_output = "video_container.mp4"
    subtitles_output = "BBB_with_subtitles.mp4"

    N = int(input("Insert the number of the exercise you want to see: "))
    if N==1:
        video_motionvector_macroblocks (input_video, mvm_output)

    elif N==2:
        video_container (original_video, output_video, output_audio_1,
                         output_audio_2, container_output)
    elif N==3:
        video_container_reader(container_output)
    elif N==4:
        video_subtitles(output_video, subtitles_output)
    else:
        print("ERROR: This exercise does not exist. Try Again!")