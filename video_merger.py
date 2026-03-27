from moviepy import VideoFileClip,concatenate_videoclips

def merge_videos(video_paths, output_file="output_sign_translation.mp4"):

    clips = []

    for path in video_paths:
        try:
            clip = VideoFileClip(path)
            clips.append(clip)
        except:
            print("Error loading:", path)

    if len(clips) == 0:
        print("No videos to merge")
        return

    final_clip = concatenate_videoclips(clips, method="compose")

    final_clip.write_videofile(
        output_file,
        codec="libx264",
        audio=False
    )

    print("\n✅ Final video saved as:", output_file)