import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips

def repeat_video(input_file, target_duration):
    clip = VideoFileClip(input_file)

    # Calculate the number of times the video needs to be repeated
    num_repeats = int(target_duration / clip.duration)

    # Repeat the video
    repeated_clip = concatenate_videoclips([clip] * num_repeats, method="compose")

    # Trim the excess if necessary
    final_clip = repeated_clip.subclip(0, target_duration)

    # Get the input file's directory and filename
    input_dir, input_filename = os.path.split(input_file)
    
    # Construct the output file path
    output_filename = os.path.splitext(input_filename)[0] + "_1hour.mp4"
    output_file = os.path.join(input_dir, output_filename)

    # Write the final video to the output file
    final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    input_file = input("Enter the path to the input video file: ")
    target_duration = 60 * 60  # 1 hour in seconds

    repeat_video(input_file, target_duration)
