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
from pylsl import StreamInfo, StreamOutlet
from ffpyplayer.player import MediaPlayer 
import random 

# SETUP ######################
##############################

# Initialize pygame 
pygame.init()

# Start Screen
start_screen = pygame.display.set_mode((1600,1200))
start_screen_width, start_screen_height = start_screen.get_size()


# Set up LSL stream
info = StreamInfo(name='experiment_stream', type='Markers', channel_count=1,
                  channel_format='int32', source_id='uniqueid12345')
outlet = StreamOutlet(info)

# FUNCTIONS ##################
##############################

def start_button(start_screen):
    """Draws a centered "Start" button on the given Pygame screen and returns its rectangle."""
    btn_w, btn_h = 150, 60
    # Place center 
    margin = 30
    x = (start_screen_width - btn_w) // 2
    y = (start_screen_height - btn_h) // 2
    start_rect = pygame.Rect(x, y, btn_w, btn_h)
    # White button
    pygame.draw.rect(start_screen, (255, 255, 255), start_rect)
    font = pygame.font.Font(None, 48)
    # Black text for button
    start_surf = font.render("Start", True, (0, 0, 0))
    start_screen.blit(start_surf, start_surf.get_rect(center=start_rect.center))
    return start_rect

def show_start_screen():
    """Display the start screen with a button to begin and send event marker."""
    start_screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 60)
    title_surface = font.render("Graphomotor Protocol", True, (255, 255, 255))
    title_rect = title_surface.get_rect(center=(start_screen_width // 2, start_screen_height // 4))
    start_screen.blit(title_surface, title_rect)

    start_rect = start_button(start_screen)
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

def draw_back_button(screen):
    """Draws a "Back" button at the bottom left corner of the given Pygame screen."""
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
    """Draws a "Next" button at the bottom right corner of the given Pygame screen."""
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
    """Show text on screen with 'Back' and 'Next' buttons."""
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
    # print("event markers:", event_markers)
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

def show_text_no_buttons(text_lines, duration_ms, event_markers):
    """Show text on screen wihtout buttons. Need to specify duration in milliseconds."""
    # Event Marker Start
    markers = event_markers
    outlet.push_sample([markers[0]])
    # print("start marker:", markers[0])
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
    # Wait for the specified duration
    pygame.time.delay(duration_ms)
    screen.fill((0, 0, 0))
    pygame.display.flip()
    # Event Marker End 
    # print("end marker:", markers[1])
    outlet.push_sample([markers[1]])


def play_audio(audio_file, num_times_play, text_lines, event_markers):
    """Play an audio file a specified number of times and display text on screen."""
    # Event Marker Start
    markers = event_markers
    outlet.push_sample([markers[0]])
    # print("start marker:", markers[0])
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
    pygame.mixer.music.play(num_times_play) # number of times to play audio file
    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    # Event Marker End 
    outlet.push_sample([markers[1]])
    # print("end marker:", markers[1])

def play_video(video_path):
    """Play a video file with a background image with ET air tags."""
    background_image_path = r"C:\Users\MoBI\Documents\graphomotor_protocol_2025\videos\video_graphomotor2.jpg"
    background_image = pygame.image.load(background_image_path)
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    # to play video:
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

def play_videos_in_random_order(video_paths, event_markers):
    """
    Plays all videos in the provided list in random order.
    Sends event markers (start, end) for each video.
    event_markers_video must be a dict: {video_path: [start_marker, end_marker], ...}
    """
    random_order = video_paths[:]
    random.shuffle(random_order)
    for video in random_order:
        # Send start marker for this video
        if video in event_markers:
            outlet.push_sample([event_markers[video][0]])
            # print("start marker:", event_markers[video][0])
        print(video)
        play_video(video)
        # Send end marker for this video
        if video in event_markers:
            outlet.push_sample([event_markers[video][1]])
            # print("end marker:", event_markers[video][1])
        # Wait for a key press to continue to the next video
        text_lines = ["Press 'Next' to watch the next video."]
        show_text_screen(text_lines)


# SCREENS ####################
##############################

# Experiment screens
experiment_start = ["Welcome to the Graphomotor Protocol", "", "", "Click 'Next' to continue."]
resting_state_instrc = [
    "You will now start the resting state task",
    "Please keep your eyes on the cross at the center of the screen.",
    "", "", "Click 'Next' when you are ready to start."
]
cross = ["+"]

# Mind Logger screens
mindlogger_start = ["Now it is time to play on the iPad!", "Please listen to the research assistant.", "", "", "Click 'Next' when task is complete."]
name_hand_writing_instrc = ["When you are ready, click 'Next' to begin Name Handwriting Task.", "", "", "Click 'Next' to continue."]
name_hand_writing = ["Name Handwriting Task", "", "", "Click 'Next' when you are finished."]
rey_copy_instrc = ["When you are ready, click 'Next' to begin Rey Copy Task.", "", "", "Click 'Next' to continue."]
rey_copy = ["Rey Copy", "", "", "Click 'Next' when you are finished."]
alpha_instrc = ["When you are ready, click 'Next' to begin Alpha Task.", "", "", "Click 'Next' to continue."]
alpha = ["Alpha", "", "", "Click 'Next' when you are finished."]
sprial_dominat_instrc = ["When you are ready, click 'Next' to begin Spiral Drawing Dominant.", "", "", "Click 'Next' to continue."]
sprial_dominat = ["Spiral Drawing Dominant", "", "", "Click 'Next' when you are finished."]
spiral_nondominat_instrc = ["When you are ready, click 'Next' to beging Spiral Drawing Non-Dominant.", "", "", "Click 'Next' to continue."]
spiral_nondominat = ["Spiral Drawing Non-Dominant", "", "", "Click 'Next' when you are finished."]
digit_symbol_sub_instrc = ["When you are ready, click 'Next' to begin Digit Symbol Subsitution.", "", "", "Click 'Next' to continue."]
digit_symbol_sub = ["Digit Symbol Substitution", "", "", "Click 'Next' when you are finished."]
rey_delay_instrc = ["When you are ready, click 'Next' to begin Rey Delay.", "", "", "Click 'Next' to continue."]
rey_delay = ["Rey Delay", "", "", "Click 'Next' when you are finished."]
trails_instrc = ["When you are ready, click 'Next' to begin Trails.", "", "", "Click 'Next' to continue."]
trails = ["Trails", "", "", "Click 'Next' when you are finished."]

# Sync Audio Screens
sync_audio_instrc = [
    "VOLUME ADJUSTMENT",
    "In the next step you will listen to an audio.",
    "Once the audio starts playing increase the volume",
    "as much as possible without being uncomfortable.",
    "", "", "Press 'Next' to continue"
]
increase_vol = ["Increase the volume to a loud, but comfortable level."]
sync_test_instruc_1 = [
    "SYNCHRONY TEST", "",
    "We will evaluate your degree of synchrony. In this task you will listen to",
    "a strange voice thorugh your headphones. While listening to the voice",
    "you should whisper continuously and in synch with the voice the",
    "syllable 'tah' (in synch means with the same rhythm at the same pace).",
    "Let's show you how to whisper rhythmically by doing a short training.",
    "", "", "Press 'Next' to continue"
]
speaker_rate_training_instrct = [
    "SPEAKING RATE TRAINING", "",
    "Now you are going to hear a set of sounds. After listening to the audio,",
    "you must whipser the syllable 'ta' (ta ta ta...) continuously and at the",
    "same rate as the sounds you just heard. Press 'Next' when ready."
]
speaker_rate_training = ["Please pay attention to the rate and remain silent."]
whisper_ta_instrc = [
    "Now it is your turn!",
    "As soon as you PRESS ANY KEY TO CONTINUE, start whispering 'ta'",
    "continuously ('ta ta ta ...') and at the SAME RATE as the sounds",
    "you heard previously."
]
whisper_ta = ["Recording! Continue to whisper 'ta ta ta'."]
sync_test_instruc_2 = [
    "SYNCHRONY TEST", "",
    "You will now listen to an audio that contains several sounds",
    "presented rhythmically. Your task is to whisper the syllable 'ta'",
    "SIMULTANEOUSLY AND IN SYNCH with the sounds throughout the ENTIRE",
    "presentation of the audio. Keep in mind that:",
    "1. You must WHISPER (softly, as if telling a secret), not speak loudly",
    "2. You must repeat 'ta ta ta' CONTINUOUSLY, SIMULTANEOUSLY, and IN SYNCH",
    "           with the audio. Do not stop before audio ends.",
    "3. Fix your gaze on a cross that will appear in the center of the screen.",
    "", "", "Click 'Next' when ready!"
]

# Video Screens
video_start_instrc = ["You will now watch some videos!", "", "", "Press 'Next' to continue."]

# PROTOCOL ##################
##############################

### Start Screen 
show_start_screen()

# Set Full Screen 
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# screen = pygame.display.set_mode((1600,1200))
screen_width, screen_height = screen.get_size()

### Experiment Start, Resting State 
protocol_flow(experiment_start, resting_state_instrc, event_markers=[[2,3], [4,5]])

### Resting State
show_text_no_buttons(cross, 120000, event_markers=[6,7])

### MindLogger
protocol_flow(mindlogger_start, name_hand_writing_instrc, name_hand_writing, 
              rey_copy_instrc, rey_copy, alpha_instrc, alpha, sprial_dominat_instrc, 
              sprial_dominat, spiral_nondominat_instrc, spiral_nondominat, 
              digit_symbol_sub_instrc, digit_symbol_sub, rey_delay_instrc,
              rey_delay, trails_instrc, trails, 
              event_markers=[[8,9], [10,11],[12,13],[14,15], [16,17],
              [18,19],[20,21],[22,23],[24,25], [26,27],[28,29],[30,31],
              [32,33],[34,35],[36,37],[38,39],[40,41]])

### Sync Audio Test
protocol_flow(sync_audio_instrc, event_markers=[[42,43]])
play_audio(r"C:\Users\MoBI\Documents\graphomotor_protocol_2025\sync_test\volume_ExpAcc_ffmpeg.wav", 4, increase_vol, event_markers=[44,45])
protocol_flow(sync_test_instruc_1, speaker_rate_training_instrct, event_markers=[[46,47], [48,49]])
play_audio(r"C:\Users\MoBI\Documents\graphomotor_protocol_2025\sync_test\example_ExpAcc.wav", 1, speaker_rate_training, event_markers=[50,51])
protocol_flow(whisper_ta_instrc, event_markers=[[52,53]])
show_text_no_buttons(whisper_ta, 10000, event_markers=[54,55])
protocol_flow(sync_test_instruc_2, event_markers=[[56,57]])
play_audio(r"C:\Users\MoBI\Documents\graphomotor_protocol_2025\sync_test\stimulus_ExpAcc_filt_ffmpeg.wav", 1, cross, event_markers=[58,59])
# Run through a 2nd time
protocol_flow(sync_test_instruc_1, speaker_rate_training_instrct, event_markers=[[60,61], [62,63]])
play_audio(r"C:\Users\MoBI\Documents\graphomotor_protocol_2025\sync_test\example_ExpAcc.wav", 1, speaker_rate_training, event_markers=[64,65])
protocol_flow(whisper_ta_instrc, event_markers=[[66,67]])
show_text_no_buttons(whisper_ta, 5000, event_markers=[68,69])
protocol_flow(sync_test_instruc_2, event_markers=[[70,71]])
play_audio(r"C:\Users\MoBI\Documents\graphomotor_protocol_2025\sync_test\stimulus_ExpAcc_filt_ffmpeg.wav", 1, cross, event_markers=[72,73])

### Videos 
protocol_flow(video_start_instrc, event_markers=[[74,75]])
video_files = [
    r"C:\Users\MoBI\Documents\graphomotor_protocol_2025\videos\Diary of a Wimpy Kid Trailer.mp4",
    r"C:\Users\MoBI\Documents\graphomotor_protocol_2025\videos\despicable_me_clip.mp4",
    r"C:\Users\MoBI\Documents\graphomotor_protocol_2025\videos\the_present.mp4",
    r"C:\Users\MoBI\Documents\graphomotor_protocol_2025\videos\fun_with_fractuals_vol_adj.mp4"
]


video_event_markers = {
    video_files[0]: [76, 77],
    video_files[1]: [78, 79],
    video_files[2]: [80, 81],
    video_files[3]: [82, 83]
}

play_videos_in_random_order(video_files, video_event_markers)

### Send final end marker   
outlet.push_sample([84])

