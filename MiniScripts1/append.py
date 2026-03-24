from moviepy import ImageClip, VideoFileClip, concatenate_videoclips

# 1. Load the title card image
image_path = "photo_6201711142686627155_w.jpg"

# .with_duration(1) sets the image to stay for 1 second
# .ifadein(0.5) makes it fade in from black over 0.5 seconds
title_card = ImageClip(image_path).with_duration(1).ifadein(0.5)

# 2. Load your main video (ensure the filename matches your file)
main_video = VideoFileClip("main_video.mp4")

# 3. Join them together
# method="compose" ensures the image fits the video's frame size
final_clip = concatenate_videoclips([title_card, main_video], method="compose")

# 4. Export the final project
final_clip.write_videofile("Flood_Prediction_FadeIn.mp4", fps=24)