# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pygame",
#   "pylsl",
#   "opencv-python",
#   "ffpyplayer"
# ]
# ///

import pygame 
import time
import cv2
from pylsl import StreamInfo, StreamOutlet
from ffpyplayer.player import MediaPlayer 

print("the script updated: 11am")

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

#################################################
############### EXPERIMENT START ################
#################################################
# Event Trigger - Intro Start
outlet.push_sample([1])

# Set up font and text 
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

# Event Trigger - Intro End 
outlet.push_sample([2])

# #################################################
# ############### RESTING STATE ###################
# #################################################

# # Event Trigger - Resting State Start
# outlet.push_sample([3])

# # Resting State Task
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "You will now start the resting state task",
#     "Please keep your eyes on the cross at the center of the screen.",
#     "",
#     "",
#     "Press any key when you are ready to start."
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

# font = pygame.font.Font(None, 90)
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

# # to test use 10 secs
# pygame.time.delay(10000)
# # pygame.time.delay(300000) --> use this for actual experiment: 5 mins 

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()

# # Event Trigger - Resting State End 
# outlet.push_sample([4])

# #################################################
# ############### MINDLOGGER IPAD TASKS ###########
# #################################################

# # Event Trigger - MindLogger Start
# outlet.push_sample([5])

# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Now it is time to play on the iPad!",
#     "Please listen to the research assistant.",
#     "",
#     "",
#     "Press any key once you finish the iPad tasks."
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

# #######################
# # Name Handwriting Task 
# #######################

# ####### Start Name Handwriting Task 
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "When you are ready, click next to begin Name Handwriting Task.",
#     "",
#     "",
#     "Press any key to continue."
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

# # Event Trigger - Name Handwriting Task Start
# outlet.push_sample([6])

# ####### Name Handwriting Task 
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Name Handwriting Task.",
#     "",
#     "",
#     "Press any key to when you are finished."
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

# # Event Trigger - Name Handwriting Task End
# outlet.push_sample([7])

# #######################
# # Rey-Osterrieth Complex Figure: Copy 
# #######################

# ####### Start ROC Figure: Copy  
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "When you are ready, click next to begin Rey-Osterrieth Complex Figure: Copy.",
#     "",
#     "",
#     "Press any key to continue."
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

# # Event Trigger - Rey-Osterrieth Complex Figure: Copy Task Start
# outlet.push_sample([8])

# ####### ROC Figure: Copy 
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Rey-Osterrieth Complex Figure: Copy.",
#     "",
#     "",
#     "Press any key to when you are finished."
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

# # Event Trigger - Rey-Osterrieth Complex Figure: Copy Task End
# outlet.push_sample([9])

# #######################
# # Rey-Osterrieth Complex Figure: Immediate Recall 
# #######################

# ####### Start ROC Figure: Immediate Recall  
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "When you are ready, click next to begin",
#     "Rey-Osterrieth Complex Figure: Immediate Recall.",
#     "",
#     "Press any key to continue."
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

# # Event Trigger - Rey-Osterrieth Complex Figure: Immediate Recall Task Start
# outlet.push_sample([10])

# ####### ROC Figure: Immediate Recall 
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Rey-Osterrieth Complex Figure:",
#     "Immediate Recall.",
#     "",
#     "",
#     "Press any key to when you are finished."
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

# # Event Trigger - Rey-Osterrieth Complex Figure: Immediate Recall Task Start End
# outlet.push_sample([11])

# #######################
# # Alphabetic Writing: Forward 
# #######################

# ####### Start Alphabetic Writing: Forward  
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "When you are ready, click next to begin",
#     "Alphabetic Writing: Forward",
#     "",
#     "Press any key to continue."
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

# # Event Trigger - Alphabetic Writing: Forward Start
# outlet.push_sample([12])

# ####### Alphabetic Writing: Forward 
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Alphabetic Writing: Forward",
#     "",
#     "",
#     "Press any key to when you are finished."
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

# # Event Trigger - Alphabetic Writing: Forward End
# outlet.push_sample([13])

# #######################
# # Alphabetic Writing: Backward
# #######################

# ####### Start Alphabetic Writing: Backward   
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "When you are ready, click next to begin",
#     "Alphabetic Writing: Backward",
#     "",
#     "Press any key to continue."
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

# # Event Trigger - Alphabetic Writing: Backward Start
# outlet.push_sample([14])

# ####### Alphabetic Writing: Backward
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Alphabetic Writing: Backward",
#     "",
#     "",
#     "Press any key to when you are finished."
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

# # Event Trigger - Alphabetic Writing: Backward End
# outlet.push_sample([15])

# #######################
# # Spiral Dominant Hand: Tracing
# #######################

# ####### Start Spiral Dominant Hand: Tracing   
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "When you are ready, click next to begin",
#     "Spiral Dominant Hand: Tracing",
#     "",
#     "Press any key to continue."
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

# # Event Trigger - Spiral Dominant Hand: Tracing Start
# outlet.push_sample([16])

# ####### Spiral Dominant Hand: Tracing
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Spiral Dominant Hand: Tracing",
#     "",
#     "",
#     "Press any key to when you are finished."
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

# # Event Trigger - Spiral Dominant Hand: Tracing End
# outlet.push_sample([17])

# #######################
# # Spiral Dominant Hand: Drawing from memory
# #######################

# ####### Start Spiral Dominant Hand: Drawing from memory   
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "When you are ready, click next to begin",
#     "Spiral Dominant Hand: Drawing from memory",
#     "",
#     "Press any key to continue."
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

# # Event Trigger - Spiral Dominant Hand: Drawing from memory Start
# outlet.push_sample([18])

# ####### Spiral Dominant Hand: Drawing from memory
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Spiral Dominant Hand: Tracing",
#     "",
#     "",
#     "Press any key to when you are finished."
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

# # Event Trigger - Spiral Dominant Hand: Drawing from memory End
# outlet.push_sample([19])


# #######################
# # Spiral Non-Dominant Hand: Tracing
# #######################

# ####### Start Spiral Non-Dominant Hand: Tracing   
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "When you are ready, click next to begin",
#     "Spiral Non-Dominant Hand: Tracing",
#     "",
#     "Press any key to continue."
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

# # Event Trigger - Spiral Non-Dominant Hand: Tracing Start
# outlet.push_sample([20])

# ####### Spiral Non-Dominant Hand: Tracing
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Spiral Dominant Hand: Tracing",
#     "",
#     "",
#     "Press any key to when you are finished."
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

# # Event Trigger - Spiral Non-Dominant Hand: Tracing End
# outlet.push_sample([21])

# #######################
# # Spiral Non-Dominant Hand: Drawing from memory
# #######################

# ####### Start Spiral Non-Dominant Hand: Drawing from memory  
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "When you are ready, click next to begin",
#     "Spiral Non-Dominant Hand: Drawing from memory",
#     "",
#     "Press any key to continue."
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

# # Event Trigger - Spiral Non-Dominant Hand: Drawing from memory Start
# outlet.push_sample([22])

# ####### Spiral Non-Dominant Hand: Drawing from memory
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Spiral Non-Dominant Hand: Drawing from memory",
#     "",
#     "",
#     "Press any key to when you are finished."
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

# # Event Trigger - Spiral Non-Dominant Hand: Drawing from memory End
# outlet.push_sample([23])

# #######################
# # Digit Symbol Substitute Test: Transcription
# #######################

# ####### Digit Symbol Substitute Test: Transcription 
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "When you are ready, click next to begin",
#     "Digit Symbol Substitute Test: Transcription",
#     "",
#     "Press any key to continue."
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

# # Event Trigger - Digit Symbol Substitute Test: Transcription Start
# outlet.push_sample([24])

# ####### Digit Symbol Substitute Test: Transcription
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Digit Symbol Substitute Test: Transcription",
#     "",
#     "",
#     "Press any key to when you are finished."
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

# # Event Trigger - Digit Symbol Substitute Test: Transcription End
# outlet.push_sample([25])

# #######################
# # Digit Symbol Substitute Test: Incidental Learning
# #######################

# ####### Digit Symbol Substitute Test: Incidental Learning 
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "When you are ready, click next to begin",
#     "Digit Symbol Substitute Test: Incidental Learning",
#     "",
#     "Press any key to continue."
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

# # Event Trigger - Digit Symbol Substitute Test: Incidental Learning Start
# outlet.push_sample([26])

# ####### Digit Symbol Substitute Test: Incidental Learning
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Digit Symbol Substitute Test: Incidental Learning",
#     "",
#     "",
#     "Press any key to when you are finished."
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

# # Event Trigger - Digit Symbol Substitute Test: Incidental Learning End
# outlet.push_sample([27])

# #######################
# # The Rey-Osterrieth Complex Figure: 20min recall 
# #######################

# ####### The Rey-Osterrieth Complex Figure: 20min recall 
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "When you are ready, click next to begin",
#     "The Rey-Osterrieth Complex Figure: 20min recall",
#     "",
#     "Press any key to continue."
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

# # Event Trigger - The Rey-Osterrieth Complex Figure: 20min recall Start
# outlet.push_sample([28])

# ####### The Rey-Osterrieth Complex Figure: 20min recall Start
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "The Rey-Osterrieth Complex Figure: 20min recall Start",
#     "",
#     "",
#     "Press any key to when you are finished."
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

# # Event Trigger - The Rey-Osterrieth Complex Figure: 20min recall End
# outlet.push_sample([29])

# ################################################
# ############## SYNC AUDIO TEST #################
# ################################################

# # Event Trigger - Sync Audio Test Start
# outlet.push_sample([30])

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

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()

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

# # Event Trigger - Speaker Rate Training Start
# outlet.push_sample([31])

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

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()

# # Event Trigger - Speaker Rate Training End
# outlet.push_sample([32])


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

# # Event Trigger - Sync Test Practice Start
# outlet.push_sample([33])

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

# # Event Trigger - Sync Test Practice End
# outlet.push_sample([34])

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

# # Event Trigger - Sync Test Part 1 Start
# outlet.push_sample([35])

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

# # Event Trigger - Sync Test Part 1 End
# outlet.push_sample([36])

# ###############################################################
# ############### TRAINING PART 2: Synchrony Test ###############
# ###############################################################
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

# # Event Trigger - Training Part 2 Start
# outlet.push_sample([37])

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

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()

# # Event Trigger - Training Part 2 End
# outlet.push_sample([38])


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

# # Event Trigger - Sync Test Part 2 Start
# outlet.push_sample([39])

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

# # Event Trigger - Sync Test Part 2 Start
# outlet.push_sample([40])

# # ############### TESTING PART 1: SYNCHRONY TEST ############### --> I think this is here in error 
# # font = pygame.font.Font(None, 60)
# # text_lines = [
# #     "SYNCHRONY TEST",
# #     "",
# #     "You will now listen to an audio that contains several sounds",
# #     "presented rhythmically. Your task is to whisper the syllable 'ta'",
# #     "SIMULTANEOUSLY AND IN SYNCH with the sounds throughout the ENTIRE",
# #     "presentation of the audio. Keep in mind that:",
# #     "1. You must WHISPER (softly, as if telling a secret), not speak loudly",
# #     "2. You must repeat 'ta ta ta' CONTINUOUSLY, SIMULTANEOUSLY, and IN SYNCH",
# #     "           with the audio. Do not stop before audio ends.",
# #     "3. Fix your gaze on a cross that will appear in the center of the screen.",
# #     "",
# #     "",
# #     "Click when ready!"
# # ]

# # # Render and display each line of text centered on the screen
# # y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
# # for line in text_lines:
# #     text_surface = font.render(line, True, (255, 255, 255))
# #     text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
# #     screen.blit(text_surface, text_rect)
# #     y_offset += font.get_linesize()

# # pygame.display.flip()

# # # Wait for a mouse click or key press
# # waiting = True
# # while waiting:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             waiting = False
# #         elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
# #             waiting = False

# # # Clear the screen
# # screen.fill((0, 0, 0))
# # pygame.display.flip()
# # outlet.push_sample([2])
# # print("pressed key")

# # ############### Play Stimulus Audio ###############
# # font = pygame.font.Font(None, 75)
# # text_lines = [
# #     "+"
# # ]

# # # Render and display each line of text centered on the screen
# # y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
# # for line in text_lines:
# #     text_surface = font.render(line, True, (255, 255, 255))
# #     text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
# #     screen.blit(text_surface, text_rect)
# #     y_offset += font.get_linesize()

# # pygame.display.flip()

# # # Play audio
# # audio_file = r"C:\Users\MoBI\Desktop\From Old Setup\sync_test\stimulus_ExpAcc_filt_ffmpeg.wav"
# # pygame.mixer.music.load(audio_file)
# # pygame.mixer.music.play()
# # while pygame.mixer.music.get_busy():
# #     pygame.time.Clock().tick(10)

# # # Clear the screen
# # screen.fill((0, 0, 0))
# # pygame.display.flip()

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

# Event Trigger - Video 1 Start
outlet.push_sample([41])

############### VIDEO 1 #####################
#### Load the JPEG background
background_image_path = r"C:\Users\MoBI\Desktop\From Old Setup\graphomotor_protocol\videos\video_graphomotor2.jpg" # path for HARLEM/MORGEN
# background_image_path = r"C:\Users\MoBI\Documents\graphomotor_protocol_2025\videos\video_graphomotor2.jpg" # path for MIDTWON/MOIRA

background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (screen_width, screen_height)) 

video_path = r"C:\Users\MoBI\Desktop\From Old Setup\graphomotor_protocol\new_videos\Diary of a Wimpy Kid Trailer.mp4"

def PlayVideo(video_path):
    player = MediaPlayer(video_path)
    clock = pygame.time.Clock()

    # Set video size (smaller than screen to see background)
    video_width = int(screen_width * 0.8)
    video_height = int(screen_height * 0.8)
    video_pos = ((screen_width - video_width) // 2, (screen_height - video_height) // 2)

    running = True
    start_time = time.time()
    base_video_time = None

    while running:
        frame, val = player.get_frame()
        if val == 'eof':
            print("End of video")
            break
        if frame is not None:
            img, t = frame  # t is the timestamp in seconds
            if base_video_time is None:
                base_video_time = time.time() - t  # Align video time to wall clock

            # Synchronize: wait if video is ahead of real time
            real_time = time.time() - base_video_time
            if t > real_time:
                time.sleep(t - real_time)

            w, h = img.get_size()
            frame_array = img.to_bytearray()[0]
            frame_surface = pygame.image.frombuffer(frame_array, (w, h), 'RGB')
            frame_surface = pygame.transform.scale(frame_surface, (video_width, video_height))

            # Draw background, then video frame
            screen.blit(background_image, (0, 0))
            screen.blit(frame_surface, video_pos)
            pygame.display.flip()

        # Handle quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                running = False

        clock.tick(60)  # Limit to 60 FPS for smoothness

    player.close_player()

PlayVideo(video_path)

# Clear the screen
screen.fill((0, 0, 0))
pygame.display.flip()

# Event Trigger - Video 1 End 
outlet.push_sample([42])


# ############### VIDEO 2 #####################
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Let's watch another video!",
#      "",
#      "",
#      "Press any key to continue."
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

# # Display the screen for 5 seconds
# pygame.time.delay(5000)

# # Event Trigger - Video 2 Start
# outlet.push_sample([43])

# # Load the JPEG background
# background_image_path = r"C:\Users\MoBI\Desktop\From Old Setup\graphomotor_protocol\videos\video_graphomotor2.jpg" # path for HARLEM/MORGEN
# # background_image_path = r"C:\Users\MoBI\Documents\graphomotor_protocol_2025\videos\video_graphomotor2.jpg" # path for MIDTWON/MOIRA
# background_image = pygame.image.load(background_image_path)
# background_image = pygame.transform.scale(background_image, (screen_width, screen_height)) 

# video_path = r"C:\Users\MoBI\Desktop\From Old Setup\graphomotor_protocol\videos\Three_Little_Kittens_Despicable_Me.mp4" # path for HARLEM/MORGEN

# PlayVideo(video_path)

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()

# # Event Trigger - Video 2 End 
# outlet.push_sample([44])

############### VIDEO 3 #####################
font = pygame.font.Font(None, 60)
text_lines = [
    "Let's watch another video!",
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

# Event Trigger - Video 3 Start
outlet.push_sample([45])

# Load the JPEG background
background_image_path = r"C:\Users\MoBI\Desktop\From Old Setup\graphomotor_protocol\videos\video_graphomotor2.jpg" # path for HARLEM/MORGEN
# background_image_path = r"C:\Users\MoBI\Documents\graphomotor_protocol_2025\videos\video_graphomotor2.jpg" # path for MIDTWON/MOIRA
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (screen_width, screen_height)) 

video_path = r"C:\Users\MoBI\Desktop\From Old Setup\graphomotor_protocol\new_videos\the_present.mp4" # path for HARLEM/MORGEN

PlayVideo(video_path)

# Clear the screen
screen.fill((0, 0, 0))
pygame.display.flip()

# Event Trigger - Video 3 End 
outlet.push_sample([46])


# ############### VIDEO 4 #####################
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Let's watch another video!",
#     "",
#     "",
#     "Press any key to continue."
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

# # Event Trigger - Video 4 Start
# outlet.push_sample([47])

# # Load the JPEG background
# background_image_path = r"C:\Users\MoBI\Desktop\From Old Setup\graphomotor_protocol\videos\video_graphomotor2.jpg" # path for HARLEM/MORGEN
# # background_image_path = r"C:\Users\MoBI\Documents\graphomotor_protocol_2025\videos\video_graphomotor2.jpg" # path for MIDTWON/MOIRA
# background_image = pygame.image.load(background_image_path)
# background_image = pygame.transform.scale(background_image, (screen_width, screen_height)) 

# video_path = r"C:\Users\MoBI\Desktop\From Old Setup\graphomotor_protocol\videos\Fun_Fractals_v2_full.mp4" # path for HARLEM/MORGEN

# PlayVideo(video_path)

# Clear the screen
screen.fill((0, 0, 0))
pygame.display.flip()

# Event Trigger - Video 4 End 
outlet.push_sample([48])

# Quit
pygame.quit()