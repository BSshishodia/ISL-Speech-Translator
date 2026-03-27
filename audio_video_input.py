import moviepy.editor as mp
import os

def extract_audio_from_video(video_path, output_audio_path="extracted_audio.wav"):
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(output_audio_path)
    return output_audio_path