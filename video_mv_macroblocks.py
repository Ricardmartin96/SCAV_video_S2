import subprocess

if __name__ == "__main__":

    subprocess.call(["ffmpeg", "-flags2", "+export_mvs", "-i", "BBB_cut.mp4",
                     "-vf", "codecview=mv=pf+bf+bb",
                     "BBB_mv_macroblocks.mp4"])
