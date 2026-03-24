# from moviepy import VideoFileClip, ImageClip, CompositeVideoClip

# # Load your video and logo
# video = VideoFileClip("input_video.mp4")

# # Change height=100 to (None, 100) or use the resize function explicitly
# logo = (ImageClip("logo.png")
#         .resized(height=100) # In v2.x, use 'resized' instead of 'resize'
#         .set_opacity(0.5) 
#         .set_position(("right", "bottom")) 
#         .set_duration(video.duration))

# # Overlay the logo onto the video
# final_video = CompositeVideoClip([video, logo])

# # Export the result
# final_video.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac")

from moviepy import VideoFileClip, ImageClip, CompositeVideoClip

# 1. Load the media (Make sure these files are in the MIniScripts folder!)
video = VideoFileClip("input_video.mp4")
logo = (ImageClip("images.jpg")
        .resized(height=video.h // 6)
        .with_opacity(0.3)
        .with_position(("right", "bottom"))
        .with_duration(video.duration))

# 2. Overlay and Save
final_video = CompositeVideoClip([video, logo])
final_video.write_videofile("translucent_output.mp4", codec="libx264", audio_codec="aac", threads=4)