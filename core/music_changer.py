from pydub import AudioSegment
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)

# Use forward slashes or raw string for the subdirectory
input_audio_path = os.path.join(script_dir, "music", "Mr.Kitty_-_After_Dark.mp3")
print(input_audio_path)

# Load the audio file
audio = AudioSegment.from_file(input_audio_path)


# # Function to change bass level
# def change_bass_level(audio, factor):
#     bass_boosted = audio.low_pass_filter(factor * 1000)
#     return bass_boosted
#
#
# # Function to speed up or slow down audio
# def change_speed(audio, speed_factor):
#     changed_speed = audio.speedup(playback_speed=speed_factor)
#     return changed_speed
#
#
# # Function to export modified audio
# def export_audio(audio, output_file):
#     audio.export(output_file, format="mp3")
#
#
# # Example usage
# modified_audio = change_bass_level(audio, 1.5)  # Increase bass level by 1.5 times
# modified_audio = change_speed(modified_audio, 1.2)  # Speed up audio by 20%
# export_audio(modified_audio, "output_audio.mp3")
