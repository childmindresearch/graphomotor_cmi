# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pygame",
#   "pylsl",
#   "opencv-python",
#   "moviepy"
# ]
# ///

import pygame 
import time
import cv2
import numpy as np
from moviepy import VideoFileClip
import threading
from pylsl import StreamInfo, StreamOutlet

# Initialize pygame 
pygame.init()

# Set up screen to display
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((1600,1200))
screen_width, screen_height = screen.get_size()


# Set up LSL stream
info = StreamInfo(name='experiment_stream', type='Markers', channel_count=1,
                  channel_format='int32', source_id='uniqueid12345')
outlet = StreamOutlet(info)

# Event Trigger
outlet.push_sample([1])

#################################################
############### EXPERIMENT START ################
#################################################
font = pygame.font.Font(None, 60)
text_lines = [
    "Welcome to the Graphomotor Protocol!",
    "",
    "",
    "Press any key to continue"
]

# Render and display each line of text centered on the screen
y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
for line in text_lines:
    text_surface = font.render(line, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
    screen.blit(text_surface, text_rect)
    y_offset += font.get_linesize()

pygame.display.flip()

# Wait for a mouse click or key press
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            waiting = False

# Clear the screen
screen.fill((0, 0, 0))
pygame.display.flip()
# Event Trigger
outlet.push_sample([3])

#################################################
############### RESTING STATE ###################
#################################################
font = pygame.font.Font(None, 60)
text_lines = [
    "You will now start the resting state task",
    "Please keep your eyes on the cross at the center of the screen.",
    "",
    "",
    "Press any key when you are ready to start."
]

# Render and display each line of text centered on the screen
y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
for line in text_lines:
    text_surface = font.render(line, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
    screen.blit(text_surface, text_rect)
    y_offset += font.get_linesize()

pygame.display.flip()

# Wait for a mouse click or key press
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            waiting = False

# Clear the screen
screen.fill((0, 0, 0))
pygame.display.flip()
# Event Trigger
outlet.push_sample([3])

font = pygame.font.Font(None, 90)
text_lines = [
    "+"
]

# Render and display each line of text centered on the screen
y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
for line in text_lines:
    text_surface = font.render(line, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
    screen.blit(text_surface, text_rect)
    y_offset += font.get_linesize()

pygame.display.flip()

# to test use 10 secs
pygame.time.delay(10000)
# pygame.time.delay(300000) --> use this for actual experiment: 5 mins 

# Clear the screen
screen.fill((0, 0, 0))
pygame.display.flip()

#################################################
############### MINDLOGGER IPAD TASKS ###########
#################################################
font = pygame.font.Font(None, 60)
text_lines = [
    "Now it is time to play on the iPad!",
    "Please listen to the research assistant.",
    "",
    "",
    "Press any key once you finish the iPad tasks."
]

# # Render and display each line of text
# y_offset = 500
# for line in text_lines:
#     text_surface = font.render(line, True, (255, 255, 255))
#     screen.blit(text_surface, (1000, y_offset)) 
#     y_offset += font.get_linesize()

# Render and display each line of text centered on the screen
y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
for line in text_lines:
    text_surface = font.render(line, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
    screen.blit(text_surface, text_rect)
    y_offset += font.get_linesize()

pygame.display.flip()

# Wait for a mouse click or key press
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            waiting = False

# Clear the screen
screen.fill((0, 0, 0))
pygame.display.flip()
# Event Trigger
outlet.push_sample([3])

#################################################
############### SYNC AUDIO TEST #################
#################################################

# ############### VOLUME ADJUSTMENT ###############
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "VOLUME ADJUSTMENT",
#     "In the next step you will listen to an audio.",
#     "Once the audio starts playing increase the volume",
#     "as much as possible without being uncomfortable.",
#     "",
#     "",
#     "Press any key to continue"
# ]

# # # Render and display each line of text
# # y_offset = 500
# # for line in text_lines:
# #     text_surface = font.render(line, True, (255, 255, 255))
# #     screen.blit(text_surface, (1000, y_offset)) 
# #     y_offset += font.get_linesize()

# # Render and display each line of text centered on the screen
# y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
# for line in text_lines:
#     text_surface = font.render(line, True, (255, 255, 255))
#     text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
#     screen.blit(text_surface, text_rect)
#     y_offset += font.get_linesize()

# pygame.display.flip()

# # Event Trigger
# outlet.push_sample([2])

# # Wait for a mouse click or key press
# waiting = True
# while waiting:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             waiting = False
#         elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
#             waiting = False

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()
# # Event Trigger
# outlet.push_sample([3])

# ##### Increase Volume (and play volume)
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Increase the volume to a loud, but comfortable level."
# ]

# # Render and display each line of text centered on the screen
# y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
# for line in text_lines:
#     text_surface = font.render(line, True, (255, 255, 255))
#     text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
#     screen.blit(text_surface, text_rect)
#     y_offset += font.get_linesize()

# pygame.display.flip()

# # Play audio
# audio_file = r"C:\Users\MoBI\Desktop\From Old Setup\sync_test\volume_ExpAcc_ffmpeg.wav"
# pygame.mixer.music.load(audio_file)
# pygame.mixer.music.play(4)
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)
# outlet.push_sample([2])
# print("send marker: volume_stim_start")

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()
# # Send marker for the start of the experiment
# outlet.push_sample([4])

# ############### TRAINING PART 1: Synchrony Test ###############
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "SYNCHRONY TEST",
#     "",
#     "We will evaluate your degree of synchrony. In this task you will listen to",
#     "a strange voice thorugh your headphones. While listening to the voice",
#     "you should whisper continuously and in synch with the voice the",
#     "syllable 'tah' (in synch means with the same rhythm at the same pace).",
#     "Let's show you how to whisper rhythmically by doing a short training.",
#     "", 
#     "",
#     "Press any key to continue"
# ]

# # Render and display each line of text centered on the screen
# y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
# for line in text_lines:
#     text_surface = font.render(line, True, (255, 255, 255))
#     text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
#     screen.blit(text_surface, text_rect)
#     y_offset += font.get_linesize()

# pygame.display.flip()

# # Wait for a mouse click or key press
# waiting = True
# while waiting:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             waiting = False
#         elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
#             waiting = False

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()
# outlet.push_sample([2])
# print("pressed key")

# ############### Speaking Rate Training ###############
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "SPEAKING RATE TRAINING",
#     "",
#     "Now you are going to hear a set of sounds. After listening to the audio,",
#     "you must whipser the syllable 'ta' (ta ta ta...) continuously and at the",
#     "same rate as teh sounds you just heard. Press any key when ready."
    
# ]

# # Render and display each line of text centered on the screen
# y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
# for line in text_lines:
#     text_surface = font.render(line, True, (255, 255, 255))
#     text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
#     screen.blit(text_surface, text_rect)
#     y_offset += font.get_linesize()

# pygame.display.flip()

# # Wait for a mouse click or key press
# waiting = True
# while waiting:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             waiting = False
#         elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
#             waiting = False

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()
# outlet.push_sample([2])
# print("pressed key")


# #### Please pay attention to the rate and remain silent
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Please pay attention to the rate and remain silent."
# ]

# # Render and display each line of text centered on the screen
# y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
# for line in text_lines:
#     text_surface = font.render(line, True, (255, 255, 255))
#     text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
#     screen.blit(text_surface, text_rect)
#     y_offset += font.get_linesize()

# pygame.display.flip()

# # Play audio
# audio_file = r"C:\Users\MoBI\Desktop\From Old Setup\sync_test\example_ExpAcc.wav"
# pygame.mixer.music.load(audio_file)
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)
# outlet.push_sample([2])
# print("send marker: volume_stim_start")

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()


# ############### Now it is your turn! ###############
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Now it is your turn!",
#     "As soon as you PRESS ANY KEY TO CONTINUE, start whispering 'ta'",
#     "continuously ('ta ta ta ...') and at the SAME RATE as the sounds",
#     "you heard previously."
    
# ]

# # Render and display each line of text centered on the screen
# y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
# for line in text_lines:
#     text_surface = font.render(line, True, (255, 255, 255))
#     text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
#     screen.blit(text_surface, text_rect)
#     y_offset += font.get_linesize()

# pygame.display.flip()

# # Wait for a mouse click or key press
# waiting = True
# while waiting:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             waiting = False
#         elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
#             waiting = False

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()

# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Recording! Continue to whisper 'ta ta ta'."
# ]

# # Render and display each line of text centered on the screen
# y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
# for line in text_lines:
#     text_surface = font.render(line, True, (255, 255, 255))
#     text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
#     screen.blit(text_surface, text_rect)
#     y_offset += font.get_linesize()

# pygame.display.flip()

# pygame.time.delay(10000)

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()

# ############### TESTING PART 1: SYNCHRONY TEST ###############
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "SYNCHRONY TEST",
#     "",
#     "You will now listen to an audio that contains several sounds",
#     "presented rhythmically. Your task is to whisper the syllable 'ta'",
#     "SIMULTANEOUSLY AND IN SYNCH with the sounds throughout the ENTIRE",
#     "presentation of the audio. Keep in mind that:",
#     "1. You must WHISPER (softly, as if telling a secret), not speak loudly",
#     "2. You must repeat 'ta ta ta' CONTINUOUSLY, SIMULTANEOUSLY, and IN SYNCH",
#     "           with the audio. Do not stop before audio ends.",
#     "3. Fix your gaze on a cross that will appear in the center of the screen.",
#     "",
#     "",
#     "Click when ready!"
# ]

# # Render and display each line of text centered on the screen
# y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
# for line in text_lines:
#     text_surface = font.render(line, True, (255, 255, 255))
#     text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
#     screen.blit(text_surface, text_rect)
#     y_offset += font.get_linesize()

# pygame.display.flip()

# # Wait for a mouse click or key press
# waiting = True
# while waiting:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             waiting = False
#         elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
#             waiting = False

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()
# outlet.push_sample([2])
# print("pressed key")

# ############### Play Stimulus Audio ###############
# font = pygame.font.Font(None, 75)
# text_lines = [
#     "+"
# ]

# # Render and display each line of text centered on the screen
# y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
# for line in text_lines:
#     text_surface = font.render(line, True, (255, 255, 255))
#     text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
#     screen.blit(text_surface, text_rect)
#     y_offset += font.get_linesize()

# pygame.display.flip()

# # Play audio
# audio_file = r"C:\Users\MoBI\Desktop\From Old Setup\sync_test\stimulus_ExpAcc_filt_ffmpeg.wav"
# pygame.mixer.music.load(audio_file)
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()

# ###############################################################
# ############### TRAINING PART 2: Synchrony Test ###############
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "SYNCHRONY TEST",
#     "",
#     "We will evaluate your degree of synchrony. In this task you will listen to",
#     "a strange voice thorugh your headphones. While listening to the voice",
#     "you should whisper continuously and in synch with the voice the",
#     "syllable 'tah' (in synch means with the same rhythm at the same pace).",
#     "Let's show you how to whisper rhythmically by doing a short training.",
#     "", 
#     "",
#     "Press any key to continue"
# ]

# # Render and display each line of text centered on the screen
# y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
# for line in text_lines:
#     text_surface = font.render(line, True, (255, 255, 255))
#     text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
#     screen.blit(text_surface, text_rect)
#     y_offset += font.get_linesize()

# pygame.display.flip()

# # Wait for a mouse click or key press
# waiting = True
# while waiting:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             waiting = False
#         elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
#             waiting = False

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()
# outlet.push_sample([2])
# print("pressed key")

# ############### Speaking Rate Training ###############
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "SPEAKING RATE TRAINING",
#     "",
#     "Now you are going to hear a set of sounds. After listening to the audio,",
#     "you must whipser the syllable 'ta' (ta ta ta...) continuously and at the",
#     "same rate as teh sounds you just heard. Press any key when ready."
    
# ]

# # Render and display each line of text centered on the screen
# y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
# for line in text_lines:
#     text_surface = font.render(line, True, (255, 255, 255))
#     text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
#     screen.blit(text_surface, text_rect)
#     y_offset += font.get_linesize()

# pygame.display.flip()

# # Wait for a mouse click or key press
# waiting = True
# while waiting:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             waiting = False
#         elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
#             waiting = False

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()
# outlet.push_sample([2])
# print("pressed key")


# #### Please pay attention to the rate and remain silent
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Please pay attention to the rate and remain silent."
# ]

# # Render and display each line of text centered on the screen
# y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
# for line in text_lines:
#     text_surface = font.render(line, True, (255, 255, 255))
#     text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
#     screen.blit(text_surface, text_rect)
#     y_offset += font.get_linesize()

# pygame.display.flip()

# # Play audio
# audio_file = r"C:\Users\MoBI\Desktop\From Old Setup\sync_test\example_ExpAcc.wav"
# pygame.mixer.music.load(audio_file)
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)
# outlet.push_sample([2])
# print("send marker: volume_stim_start")

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()


# ############### Now it is your turn! ###############
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Now it is your turn!",
#     "As soon as you PRESS ANY KEY TO CONTINUE, start whispering 'ta'",
#     "continuously ('ta ta ta ...') and at the SAME RATE as the sounds",
#     "you heard previously."
    
# ]

# # Render and display each line of text centered on the screen
# y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
# for line in text_lines:
#     text_surface = font.render(line, True, (255, 255, 255))
#     text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
#     screen.blit(text_surface, text_rect)
#     y_offset += font.get_linesize()

# pygame.display.flip()

# # Wait for a mouse click or key press
# waiting = True
# while waiting:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             waiting = False
#         elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
#             waiting = False

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()

# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Recording! Continue to whisper 'ta ta ta'."
# ]

# # Render and display each line of text centered on the screen
# y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
# for line in text_lines:
#     text_surface = font.render(line, True, (255, 255, 255))
#     text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
#     screen.blit(text_surface, text_rect)
#     y_offset += font.get_linesize()

# pygame.display.flip()

# pygame.time.delay(10000)

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()

# ############### TESTING PART 1: SYNCHRONY TEST ###############
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "SYNCHRONY TEST",
#     "",
#     "You will now listen to an audio that contains several sounds",
#     "presented rhythmically. Your task is to whisper the syllable 'ta'",
#     "SIMULTANEOUSLY AND IN SYNCH with the sounds throughout the ENTIRE",
#     "presentation of the audio. Keep in mind that:",
#     "1. You must WHISPER (softly, as if telling a secret), not speak loudly",
#     "2. You must repeat 'ta ta ta' CONTINUOUSLY, SIMULTANEOUSLY, and IN SYNCH",
#     "           with the audio. Do not stop before audio ends.",
#     "3. Fix your gaze on a cross that will appear in the center of the screen.",
#     "",
#     "",
#     "Click when ready!"
# ]

# # Render and display each line of text centered on the screen
# y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
# for line in text_lines:
#     text_surface = font.render(line, True, (255, 255, 255))
#     text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
#     screen.blit(text_surface, text_rect)
#     y_offset += font.get_linesize()

# pygame.display.flip()

# # Wait for a mouse click or key press
# waiting = True
# while waiting:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             waiting = False
#         elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
#             waiting = False

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()
# outlet.push_sample([2])
# print("pressed key")

# ############### Play Stimulus Audio ###############
# font = pygame.font.Font(None, 75)
# text_lines = [
#     "+"
# ]

# # Render and display each line of text centered on the screen
# y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
# for line in text_lines:
#     text_surface = font.render(line, True, (255, 255, 255))
#     text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
#     screen.blit(text_surface, text_rect)
#     y_offset += font.get_linesize()

# pygame.display.flip()

# # Play audio
# audio_file = r"C:\Users\MoBI\Desktop\From Old Setup\sync_test\stimulus_ExpAcc_filt_ffmpeg.wav"
# pygame.mixer.music.load(audio_file)
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()

#################################################
############### VIDEOS ##########################
#################################################
font = pygame.font.Font(None, 60)
text_lines = [
    "You will now watch some videos!",
    "",
    "",
    "Press any key to continue."
]

# Render and display each line of text centered on the screen
y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
for line in text_lines:
    text_surface = font.render(line, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
    screen.blit(text_surface, text_rect)
    y_offset += font.get_linesize()

pygame.display.flip()

# Wait for a mouse click or key press
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            waiting = False

# Load the video using OpenCV
video_path = r"C:\Users\MoBI\Desktop\From Old Setup\sync_test\Diary_of_a_Wimpy_Kid_Trailer.mp4"
# --- Function to play audio using MoviePy ---
def play_audio(video_path):
    clip = VideoFileClip(video_path)
    clip.audio.preview()  # This plays audio in real-time

# Start audio playback in a separate thread
audio_thread = threading.Thread(target=play_audio, args=(video_path,))
audio_thread.start()

cap = cv2.VideoCapture(video_path)

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) or 30  # fallback to 30 FPS if not available

# Set up Pygame window
screen = pygame.display.set_mode((frame_width, frame_height))
pygame.display.set_caption("Video + Audio Player")

# Main loop
running = True
clock = pygame.time.Clock()

while running and cap.isOpened():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    ret, frame = cap.read()
    if not ret:
        break  # End of video

    # Convert BGR (OpenCV) to RGB (Pygame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)  # Optional: rotate if needed
    frame_surface = pygame.surfarray.make_surface(frame)

    # Display the frame
    screen.blit(frame_surface, (0, 0))
    pygame.display.update()

    # Maintain video framerate
    clock.tick(fps)

# Clear the screen
screen.fill((0, 0, 0))
pygame.display.flip()
# Event Trigger
outlet.push_sample([3])

# Cleanup
cap.release()
pygame.quit()