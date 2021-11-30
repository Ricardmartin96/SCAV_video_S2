import subprocess
import sys

if __name__ == "__main__":

    # Extract data from video container:
    file = open("video_container_data.txt", "w")
    subprocess.run(["ffprobe", "video_container.mp4"], stdout=file
                   , stderr=subprocess.STDOUT)
    #capture and combine both streams into one
    # subprocess.PIPE indicates that a pipe to the standard stream should be
    # opened.
    # subprocess.STDOUT indicates that standard error should go into the same
    # handle as standard output.

    # opening the text file
    file = open("video_container_data.txt", "r")
    cont = 0
    no_error = 0
    llista = []
    # reading each line
    for x in file:
        words = x.split()
        # reading each word
        for i in words:
            #guardar cada paraula en llista
            llista.append(i)
    for j in llista:
       if j == "Audio:":
          print('Audio codec: ', llista[cont+1])
          no_error = no_error+1
       if j == "Video:":
          print('Video codec: ', llista[cont+1])
          no_error = no_error + 1
       if j == "bitrate:":
          print('Bit rate: ', llista[cont + 1])
       if j == "fps,":
          print('Frame rate: ', llista[cont - 1])
       cont = cont+1

    if(no_error == 0):
        print('ERROR, no codec found')

    file.close()
