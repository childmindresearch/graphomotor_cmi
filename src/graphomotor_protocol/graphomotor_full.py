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

print("the script updated: 11:56am")

###########################################
################## SETUP ##################
###########################################

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

###########################################
############## FUNCTIONS ##################
###########################################

def start_button(screen):
    btn_w, btn_h = 150, 60
    # Place center 
    margin = 30
    x = (screen_width - btn_w) // 2
    y = (screen_height - btn_h) // 2
    start_rect = pygame.Rect(x, y, btn_w, btn_h)
    # White button
    pygame.draw.rect(screen, (255, 255, 255), start_rect)
    font = pygame.font.Font(None, 48)
    # Black text for button
    start_surf = font.render("Start", True, (0, 0, 0))
    screen.blit(start_surf, start_surf.get_rect(center=start_rect.center))
    return start_rect

def show_start_screen():
    """Display the start screen with a button to begin."""
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 60)
    title_surface = font.render("Graphomotor Protocol", True, (255, 255, 255))
    title_rect = title_surface.get_rect(center=(screen_width // 2, screen_height // 4))
    screen.blit(title_surface, title_rect)

    start_rect = start_button(screen)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    outlet.push_sample([1])
                    return "start"

# Set up Buttons on Screen 
def draw_back_button(screen):
    btn_w, btn_h = 150, 60
    margin = 30
    # Place at bottom left
    x = margin 
    y = screen_height - btn_h - margin
    back_rect = pygame.Rect(x, y, btn_w, btn_h)
    # White button
    pygame.draw.rect(screen, (255, 255, 255), back_rect)
    font = pygame.font.Font(None, 48)
    # Black text for button 
    back_surf = font.render("Back", True, (0,0,0))
    screen.blit(back_surf, back_surf.get_rect(center=back_rect.center))
    return back_rect

def draw_forward_button(screen):
    btn_w, btn_h = 150, 60
    margin = 30
    x = screen_width - btn_w - margin
    y = screen_height - btn_h - margin
    forward_rect = pygame.Rect(x, y, btn_w, btn_h)
    pygame.draw.rect(screen, (255, 255, 255), forward_rect)
    font = pygame.font.Font(None, 48)
    forward_surf = font.render("Next", True, (0,0,0))
    screen.blit(forward_surf, forward_surf.get_rect(center=forward_rect.center))
    return forward_rect


def show_text_screen(text_lines):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 60)
    y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
    for line in text_lines:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(text_surface, text_rect)
        y_offset += font.get_linesize()
    back_rect = draw_back_button(screen)
    forward_rect = draw_forward_button(screen)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    return "back"
                elif forward_rect.collidepoint(event.pos):
                    return "next"
            # elif event.type == pygame.KEYDOWN:
                # Optionally, you can keep this to allow keyboard navigation
                # return "next"
    return "next"

def protocol_flow(*screens, event_markers):
    """
    Display a sequence of instruction screens.
    Each argument should be a list of text lines for one screen.
    Sends the specified event markers to LSL at the start and end of each screen.
    event_markers must be a list of [start_marker, end_marker] for each screen.
    Returns when the sequence is finished or user quits.
    """
    protocol = list(screens)
    if event_markers is None or len(event_markers) != len(protocol):
        raise ValueError("You must provide event_markers as a list of [start_marker, end_marker] for each screen.")
    idx = 0
    while idx < len(protocol):
        marker = event_markers[idx]
        # Send start marker
        if isinstance(marker, (list, tuple)) and len(marker) == 2:
            outlet.push_sample([marker[0]])
        else:
            raise ValueError("Each event_markers entry must be a [start_marker, end_marker] pair.")
        result = show_text_screen(protocol[idx])
        # Send end marker
        outlet.push_sample([marker[1]])
        if result == 'back':
            if idx > 0:
                idx -= 1
        elif result == 'quit':
            break
        else:
            idx += 1


def show_cross(duration_ms=10000):
    """Display a centered cross for the given duration (in ms), with no buttons."""
    # Event Marker Start
    outlet.push_sample([6])
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 90)
    cross = "+"
    text_surface = font.render(cross, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    pygame.time.delay(duration_ms)
    screen.fill((0, 0, 0))
    pygame.display.flip()
    # Event Marker End
    outlet.push_sample([7])

def play_audio(audio_file, text_lines, event_markers):
    # Event Marker Start
    markers = event_markers
    print(markers)
    print(markers[0])
    outlet.push_sample([markers[0]])
    # Display screen
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 60)
    y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
    for line in text_lines:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(text_surface, text_rect)
        y_offset += font.get_linesize()
    pygame.display.flip()
    # Play audio
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play(4) # play audio 4 times
    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    # Event Marker End 
    outlet.push_sample([markers[1]])


############### TESTING #################

### Create screens for experiment
experiment_start = ["Welcome to the Graphomotor Protocol", "", "", "Click 'Next' to continue."]
resting_state_instrc = ["You will now start the resting state task", "Please keep your eyes on the cross at the center of the screen.",
                 "", "", "Click 'Next' when you are ready to start."]


#### Mind Logger screens
mindlogger_start = ["Now it is time to play on the iPad!", "Please listen to the research assistant.",
                    "", "", "Click 'Next' when task is complete."]
# name_writing 
name_hand_writing_instrc = ["When you are ready, click 'Next' to begin Name Handwriting Task.", "", "", "Click 'Next' to continue."]
name_hand_writing = ["Name Handwriting Task", "", "", "Click 'Next' when you are finished."]
# rey copy
rey_copy_instrc = ["When you are ready, click 'Next' to begin Rey Copy Task.", "", "", "Click 'Next' to continue."]
rey_copy = ["Rey Copy", "", "", "Click 'Next' when you are finished."]
# alpha 
alpha_instrc = ["When you are ready, click 'Next' to begin Alpha Task.", "", "", "Click 'Next' to continue."]
alpha = ["Alpha", "", "", "Click 'Next' when you are finished."]
# spiral dominat 
sprial_dominat_instrc = ["When you are ready, click 'Next' to begin Spiral Drawing Dominat.", "", "", "Click 'Next' to continue."]
sprial_dominat = ["Spiral Drawing Dominat", "", "", "Click 'Next' when you are finished."]
# spiral non-dominat
spiral_nondominat_instrc = ["When you are ready, click 'Next' to beging Spiral Drawing Non-Dominat.", "", "", "Click 'Next' to continue."]
spiral_nondominat = ["Spiral Drawing Non-Dominat", "", "", "Click 'Next' when you are finished."]
# digit symbol subsitution
digit_symbol_sub_instrc = ["When you are ready, click 'Next' to begin Digit Symbol Subsitution.", "", "", "Click 'Next' to continue."]
digit_symbol_sub = ["Digit Symbol Substitution", "", "", "Click 'Next' when you are finished."]
# rey delay 
rey_delay_instrc = ["When you are ready, click 'Next' to begin Rey Delay.", "", "", "Click 'Next' to continue."]
rey_delay = ["Rey Delay", "", "", "Click 'Next' when you are finished."]
# trails 
trails_instrc = ["When you are ready, click 'Next' to begin Trails.", "", "", "Click 'Next' to continue."]
trails = ["Trails", "", "", "Click 'Next' when you are finished."]

#### Sync Audio Screens
sync_audio_instrc = [
    "VOLUME ADJUSTMENT",
    "In the next step you will listen to an audio.",
    "Once the audio starts playing increase the volume",
    "as much as possible without being uncomfortable.",
    "",
    "",
    "Press any key to continue"
]
increase_vol = ["Increase the volume to a loud, but comfortable level."]
sync_test_instruc = [
    "SYNCHRONY TEST",
    "",
    "We will evaluate your degree of synchrony. In this task you will listen to",
    "a strange voice thorugh your headphones. While listening to the voice",
    "you should whisper continuously and in synch with the voice the",
    "syllable 'tah' (in synch means with the same rhythm at the same pace).",
    "Let's show you how to whisper rhythmically by doing a short training.",
    "", 
    "",
    "Press any key to continue"
]
speaker_rate_training_instrct = [
    "SPEAKING RATE TRAINING",
    "",
    "Now you are going to hear a set of sounds. After listening to the audio,",
    "you must whipser the syllable 'ta' (ta ta ta...) continuously and at the",
    "same rate as teh sounds you just heard. Press any key when ready."
    
]
speaker_rate_training = ["Please pay attention to the rate and remain silent."]

#### PROTOCOL FLOW:

# Start Screen 
show_start_screen()

# # Experiment Start, Resting State 
# protocol_flow(experiment_start, resting_state_instrc, event_markers=[[2,3], [4,5]])

# # Resting State
# show_cross(5000)

# # MindLogger
# protocol_flow(mindlogger_start, name_hand_writing_instrc, name_hand_writing, 
#               rey_copy_instrc, rey_copy, alpha_instrc, alpha, sprial_dominat_instrc, 
#               sprial_dominat, spiral_nondominat_instrc, spiral_nondominat, 
#               digit_symbol_sub_instrc, digit_symbol_sub, rey_delay_instrc,
#               rey_delay, trails_instrc, trails, 
#               event_markers=[[8,9], [10,11],[12,13],[14,15], [16,17],
#               [18,19],[20,21],[22,23],[24,25], [26,27],[28,29],[30,31],
#               [32,33],[34,35],[36,37],[38,39],[40,41]])

# Sync Audio Test
protocol_flow(sync_audio_instrc, event_markers=[[42,43]])
play_audio(r"C:\Users\MoBI\Desktop\From Old Setup\sync_test\volume_ExpAcc_ffmpeg.wav", increase_vol, event_markers=[44,45])
protocol_flow(sync_test_instruc, speaker_rate_training_instrct, event_markers=[[46,47], [48,49]])
play_audio(r"C:\Users\MoBI\Desktop\From Old Setup\sync_test\example_ExpAcc.wav", speaker_rate_training, event_markers=[50,51])


# ################################################
# ############## SYNC AUDIO TEST #################
# ################################################



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

# #################################################
# ############### VIDEOS ##########################
# #################################################
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "You will now watch some videos!",
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

# # Event Trigger - Video 1 Start
# outlet.push_sample([41])

# ############### VIDEO 1 #####################
# #### Load the JPEG background
# background_image_path = r"C:\Users\MoBI\Desktop\From Old Setup\graphomotor_protocol\videos\video_graphomotor2.jpg" # path for HARLEM/MORGEN
# # background_image_path = r"C:\Users\MoBI\Documents\graphomotor_protocol_2025\videos\video_graphomotor2.jpg" # path for MIDTWON/MOIRA

# background_image = pygame.image.load(background_image_path)
# background_image = pygame.transform.scale(background_image, (screen_width, screen_height)) 

# video_path = r"C:\Users\MoBI\Desktop\From Old Setup\graphomotor_protocol\new_videos\Diary of a Wimpy Kid Trailer.mp4"

# def PlayVideo(video_path):
#     player = MediaPlayer(video_path)
#     clock = pygame.time.Clock()

#     # Set video size (smaller than screen to see background)
#     video_width = int(screen_width * 0.8)
#     video_height = int(screen_height * 0.8)
#     video_pos = ((screen_width - video_width) // 2, (screen_height - video_height) // 2)

#     running = True
#     start_time = time.time()
#     base_video_time = None

#     while running:
#         frame, val = player.get_frame()
#         if val == 'eof':
#             print("End of video")
#             break
#         if frame is not None:
#             img, t = frame  # t is the timestamp in seconds
#             if base_video_time is None:
#                 base_video_time = time.time() - t  # Align video time to wall clock

#             # Synchronize: wait if video is ahead of real time
#             real_time = time.time() - base_video_time
#             if t > real_time:
#                 time.sleep(t - real_time)

#             w, h = img.get_size()
#             frame_array = img.to_bytearray()[0]
#             frame_surface = pygame.image.frombuffer(frame_array, (w, h), 'RGB')
#             frame_surface = pygame.transform.scale(frame_surface, (video_width, video_height))

#             # Draw background, then video frame
#             screen.blit(background_image, (0, 0))
#             screen.blit(frame_surface, video_pos)
#             pygame.display.flip()

#         # Handle quit events
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
#                 running = False

#         clock.tick(60)  # Limit to 60 FPS for smoothness

#     player.close_player()

# PlayVideo(video_path)

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()

# # Event Trigger - Video 1 End 
# outlet.push_sample([42])


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

# video_path = r"C:\Users\MoBI\Desktop\From Old Setup\graphomotor_protocol\new_videos\despicable_me_clip.mp4" # path for HARLEM/MORGEN

# PlayVideo(video_path)

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()

# # Event Trigger - Video 2 End 
# outlet.push_sample([44])

# ############### VIDEO 3 #####################
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

# # Event Trigger - Video 3 Start
# outlet.push_sample([45])

# # Load the JPEG background
# background_image_path = r"C:\Users\MoBI\Desktop\From Old Setup\graphomotor_protocol\videos\video_graphomotor2.jpg" # path for HARLEM/MORGEN
# # background_image_path = r"C:\Users\MoBI\Documents\graphomotor_protocol_2025\videos\video_graphomotor2.jpg" # path for MIDTWON/MOIRA
# background_image = pygame.image.load(background_image_path)
# background_image = pygame.transform.scale(background_image, (screen_width, screen_height)) 

# video_path = r"C:\Users\MoBI\Desktop\From Old Setup\graphomotor_protocol\new_videos\the_present.mp4" # path for HARLEM/MORGEN

# PlayVideo(video_path)

# # Clear the screen
# screen.fill((0, 0, 0))
# pygame.display.flip()

# # Event Trigger - Video 3 End 
# outlet.push_sample([46])


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
# outlet.push_sample([48])

# Quit
pygame.quit()







# #########################################
# ############### EXPERIMENT START ########
# #########################################
# # Event Trigger - Intro Start
# outlet.push_sample([1])

# # Set up font and text 
# font = pygame.font.Font(None, 60)
# text_lines = [
#     "Welcome to the Graphomotor Protocol!",
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

# # Event Trigger - Intro End 
# outlet.push_sample([2])

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

# def protocol_flow(*screens): --> this function works, sans event markers 
#     """
#     Display a sequence of instruction screens.
#     Each argument should be a list of text lines for one screen.
#     Returns when the sequence is finished or user quits.
#     """
#     idx = 0
#     protocol = list(screens)
#     while idx < len(protocol):
#         result = show_text_screen(protocol[idx])
#         if result == 'back':
#             if idx > 0:
#                 idx -= 1
#         elif result == 'quit':
#             break
#         else:
#             idx += 1

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