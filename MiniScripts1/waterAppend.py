from moviepy import ImageClip, VideoFileClip, CompositeVideoClip, concatenate_videoclips, vfx
import os

# --- 1. CONFIGURATION (Edit filenames here if needed) ---
INTRO_IMAGE_PATH = "front.jpg"
WATERMARK_IMAGE_PATH = "logo.jpg"
MAIN_VIDEO_PATH = "main_video.mp4"
FINAL_FILENAME = "Final_Flood_Project_LPU.mp4"

# --- 2. PREPARE THE MAIN VIDEO SECTION (WITH WATERMARK) ---
print(f"Step 1: Loading main video and applying watermark...")

if not os.path.exists(MAIN_VIDEO_PATH):
    raise FileNotFoundError(f"Error: Video '{MAIN_VIDEO_PATH}' not found in this folder.")

# Load the main video
original_video = VideoFileClip(MAIN_VIDEO_PATH)

# Load and style the watermark
print(f"Step 2: Styling the logo...")
if not os.path.exists(WATERMARK_IMAGE_PATH):
    raise FileNotFoundError(f"Error: Logo '{WATERMARK_IMAGE_PATH}' not found.")

logo = (ImageClip(WATERMARK_IMAGE_PATH)
        .resized(width=150)                    # Adjust size
        .with_opacity(0.8)                     # 80% visible
        .with_duration(original_video.duration) # Matches video length
        .with_position(('right', 'top')))       # Top-right corner

# Apply watermark on top of the video
video_with_logo = CompositeVideoClip([original_video, logo])

# --- 3. PREPARE THE INTRO CLIP (THE TITLE CARD) ---
print(f"Step 3: Preparing the title card with fade-in...")

if not os.path.exists(INTRO_IMAGE_PATH):
    raise FileNotFoundError(f"Error: Intro image '{INTRO_IMAGE_PATH}' not found.")

# Prepend the image with a 0.5s fade-in effect
title_card = (ImageClip(INTRO_IMAGE_PATH)
              .with_duration(1)
              .with_effects([vfx.FadeIn(0.5)])) # New v2.x syntax

# --- 4. ASSEMBLE THE FINAL PROJECT ---
print("Step 4: Joining everything together...")

# method="compose" ensures different resolutions/aspect ratios are handled
final_clip = concatenate_videoclips([title_card, video_with_logo], method="compose")

# --- 5. EXPORT THE FINAL VIDEO ---
print(f"Step 5: Exporting {FINAL_FILENAME} (Please wait)...")
final_clip.write_videofile(FINAL_FILENAME, fps=24, codec='libx264')

print("-" * 30)
print("SUCCESS: Your project video is ready!")
print("-" * 30)