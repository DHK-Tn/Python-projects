#import module
from moviepy.editor import *
path_Video = input("Enter the Path and the name for your video >> ")
video = VideoFileClip(path_Video)
name_GIF = input("Enter a Name For Your GIF >> ")
name_GIF = name_GIF+".gif"
video.write_gif(name_GIF)
print("\nDone !")