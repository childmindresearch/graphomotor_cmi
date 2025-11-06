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
start_screen = pygame.display.set_mode((2560, 1400), pygame.RESIZABLE) # 1600x1200 
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
    #start_screen.blit(background_image, (0,0))
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
    btn_w, btn_h = 130, 60
    margin = 35
    # Place at bottom left
    x = margin 
    y = screen_height - btn_h - margin
    back_rect = pygame.Rect(x, y, btn_w, btn_h)
    # Black button
    pygame.draw.rect(screen, (0, 0, 0), back_rect) # white button (255, 255, 255)
    font = pygame.font.Font(None, 48)
    # White text for button 
    back_surf = font.render("Back", True, (255,255,255)) # black text (0, 0, 0)
    screen.blit(back_surf, back_surf.get_rect(center=back_rect.center))
    return back_rect

def draw_forward_button(screen):
    """Draws a "Next" button at the bottom right corner of the given Pygame screen."""
    btn_w, btn_h = 130, 60
    margin = 35
    x = screen_width - btn_w - margin
    y = screen_height - btn_h - margin
    forward_rect = pygame.Rect(x, y, btn_w, btn_h)
    pygame.draw.rect(screen, (0, 0, 0), forward_rect)
    font = pygame.font.Font(None, 48)
    forward_surf = font.render("Next", True, (255,255,255))
    screen.blit(forward_surf, forward_surf.get_rect(center=forward_rect.center))
    return forward_rect

def draw_skip_button_video(screen):
    """Draws a "Skip" button for the videos."""
    btn_w, btn_h = 300, 300
    margin = 30
    # x = ((screen_width - btn_w) // 2) 
    x = margin
    # y = screen_height - btn_h - margin
    y = margin
    forward_rect = pygame.Rect(x, y, btn_w, btn_h)
    pygame.draw.rect(screen, (0,0,0), forward_rect)
    font = pygame.font.Font(None, 20)
    forward_surf = font.render("Skip", True, (200,200,200))
    screen.blit(forward_surf, forward_surf.get_rect(center=forward_rect.center))
    return forward_rect

def draw_end_experiment_button(screen):
    """ Draws an 'End Experiment' button."""
    btn_w, btn_h = 150, 60
    margin = 30
    x = ((screen_width - btn_w) // 2 ) 
    y = screen_height - btn_h - margin
    forward_rect = pygame.Rect(x, y, btn_w, btn_h)
    pygame.draw.rect(screen, (0,0,0), forward_rect)
    font = pygame.font.Font(None, 20)
    forward_surf = font.render("End Experiment", True, (200,200,200))
    screen.blit(forward_surf, forward_surf.get_rect(center=forward_rect.center))
    return forward_rect

def show_text_screen(text_lines):
    """Show text on screen with 'Back' and 'Next' buttons."""
    # screen.fill((0, 0, 0))
    screen.blit(background_image, (0,0))
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

def show_text_screen_videos(text_lines):
    """Show text on screen with 'Back' and 'Next' buttons."""
    # screen.fill((0, 0, 0))
    screen.blit(background_image, (0,0))
    font = pygame.font.Font(None, 60)
    y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
    for line in text_lines:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(text_surface, text_rect)
        y_offset += font.get_linesize()
    back_rect = draw_back_button(screen)
    forward_rect = draw_forward_button(screen)
    end_rect = draw_end_experiment_button(screen)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    return "back"
                if forward_rect.collidepoint(event.pos):
                    return "next"
                if end_rect.collidepoint(event.pos):
                    outlet.push_sample([84]) # Send final marker
                    pygame.quit()
                    exit()
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

def protocol_flow_with_result(*screens, event_markers):
    """Modified protocol_flow that returns the final result instead of handling navigation internally."""
    protocol = list(screens)
    if event_markers is None or len(event_markers) != len(protocol):
        raise ValueError("You must provide event_markers as a list of [start_marker, end_marker] for each screen.")
    
    for i, screen in enumerate(protocol):
        marker = event_markers[i]
        outlet.push_sample([marker[0]])
        result = show_text_screen(screen)
        outlet.push_sample([marker[1]])
        
        if result in ['back', 'quit']:
            return result
    
    return 'next'

def play_audio_with_result(audio_file, num_times_play, text_lines, event_markers):
    """Modified play_audio that adds back button functionality."""
    markers = event_markers
    outlet.push_sample([markers[0]])
    screen.blit(background_image, (0,0))
    font = pygame.font.Font(None, 60)
    y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
    
    # Store text rectangles for click detection
    text_rects = []
    for line in text_lines:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
        text_rects.append(text_rect)
        screen.blit(text_surface, text_rect)
        y_offset += font.get_linesize()
    
    # Add back button
    back_rect = draw_back_button(screen)
    pygame.display.flip()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play(num_times_play)
    
    # Wait for the audio to finish playing, pumping events and checking for clicks
    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check for back button click
                if back_rect.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    outlet.push_sample([markers[1]])
                    return 'back'
                # Check if click is on any text line
                for text_rect in text_rects:
                    if text_rect.collidepoint(event.pos):
                        pygame.mixer.music.stop()  # Stop the audio
                        break
            elif event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                outlet.push_sample([markers[1]])
                return 'quit'
        
        pygame.time.Clock().tick(10)
    
    outlet.push_sample([markers[1]])
    return 'next'

def show_text_no_buttons_with_result(text_lines, duration_ms, event_markers):
    """Modified show_text_no_buttons that adds back button functionality."""
    markers = event_markers
    outlet.push_sample([markers[0]])
    screen.blit(background_image, (0,0))
    font = pygame.font.Font(None, 60)
    y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
    
    # Store text rectangles for click detection
    text_rects = []
    for line in text_lines:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
        text_rects.append(text_rect)
        screen.blit(text_surface, text_rect)
        y_offset += font.get_linesize()
    
    # Add back button
    back_rect = draw_back_button(screen)
    pygame.display.flip()
    
    # Wait for the specified duration, pumping events and checking for clicks
    wait_time = 0
    interval = 50  # ms
    while wait_time < duration_ms:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check for back button click
                if back_rect.collidepoint(event.pos):
                    outlet.push_sample([markers[1]])
                    return 'back'
                # Check if click is on any text line
                for text_rect in text_rects:
                    if text_rect.collidepoint(event.pos):
                        wait_time = duration_ms
                        break
            elif event.type == pygame.QUIT:
                outlet.push_sample([markers[1]])
                return 'quit'
        
        if wait_time < duration_ms:
            pygame.time.delay(interval)
            wait_time += interval
    
    screen.blit(background_image, (0,0))
    pygame.display.flip()
    outlet.push_sample([markers[1]])
    return 'next'

def sync_audio_flow():
    """Handle the entire sync audio test sequence with back/forward navigation."""
    
    # Define all the steps in the sync audio sequence
    steps = [
        # Step 0: Instructions
        ('protocol_flow', [sync_audio_instrc], [[40,41]]),
        # Step 1: Volume adjustment
        ('play_audio', r"C:\Users\MoBI\Documents\speech_sync_task\volume.wav", 4, increase_vol, [42,43]),
        # Step 2: Test instructions
        ('protocol_flow', [sync_test_instruc_1, speaker_rate_training_instrct], [[44,45], [46,47]]),
        # Step 3: Example audio
        ('play_audio', r"C:\Users\MoBI\Documents\speech_sync_task\example.wav", 1, speaker_rate_training, [48,49]),
        # Step 4: Whisper instructions
        ('protocol_flow', [whisper_ta_instrc], [[50,51]]),
        # Step 5: Practice recording
        ('show_text_no_buttons', whisper_ta, 10000, [52,53]),
        # Step 6: Final instructions
        ('protocol_flow', [sync_test_instruc_2], [[54,55]]),
        # Step 7: Main test
        ('play_audio', r"C:\Users\MoBI\Documents\speech_sync_task\stimulus.wav", 1, cross, [56,57]),
        
        # Second round
        # Step 8: Test instructions again
        ('protocol_flow', [sync_test_instruc_1, speaker_rate_training_instrct], [[58,59], [60,61]]),
        # Step 9: Example audio again
        ('play_audio', r"C:\Users\MoBI\Documents\speech_sync_task\example.wav", 1, speaker_rate_training, [62,63]),
        # Step 10: Whisper instructions again
        ('protocol_flow', [whisper_ta_instrc], [[64,65]]),
        # Step 11: Practice recording again
        ('show_text_no_buttons', whisper_ta, 5000, [66,67]),
        # Step 12: Final instructions again
        ('protocol_flow', [sync_test_instruc_2], [[68,69]]),
        # Step 13: Main test again
        ('play_audio', r"C:\Users\MoBI\Documents\speech_sync_task\stimulus.wav", 1, cross, [70,71])
    ]
    
    current_step = 0
    
    while current_step < len(steps):
        step = steps[current_step]
        step_type = step[0]
        
        if step_type == 'protocol_flow':
            screens = step[1]
            event_markers = step[2]
            result = protocol_flow_with_result(*screens, event_markers=event_markers)
            
        elif step_type == 'play_audio':
            audio_file = step[1]
            num_times = step[2]
            text_lines = step[3]
            event_markers = step[4]
            result = play_audio_with_result(audio_file, num_times, text_lines, event_markers)
            
        elif step_type == 'show_text_no_buttons':
            text_lines = step[1]
            duration = step[2]
            event_markers = step[3]
            result = show_text_no_buttons_with_result(text_lines, duration, event_markers)
        
        # Handle navigation
        if result == 'back':
            if current_step > 0:
                current_step -= 1
        elif result == 'quit':
            break
        else:  # 'next' or None
            current_step += 1

def show_text_no_buttons(text_lines, duration_ms, event_markers):
    """Show text on screen without buttons. Need to specify duration in milliseconds."""
    markers = event_markers
    outlet.push_sample([markers[0]])
    # screen.fill((0, 0, 0))
    screen.blit(background_image, (0,0))
    font = pygame.font.Font(None, 60)
    y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
    
    # Store text rectangles for click detection
    text_rects = []
    for line in text_lines:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
        text_rects.append(text_rect)
        screen.blit(text_surface, text_rect)
        y_offset += font.get_linesize()
    
    pygame.display.flip()
    
    # Wait for the specified duration, pumping events and checking for clicks
    wait_time = 0
    interval = 50  # ms
    while wait_time < duration_ms:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if click is on any text line
                for text_rect in text_rects:
                    if text_rect.collidepoint(event.pos):
                        # Skip ahead by breaking out of the time loop
                        wait_time = duration_ms
                        break
            elif event.type == pygame.QUIT:
                wait_time = duration_ms  # Exit the loop
                break
        
        if wait_time < duration_ms:  # Only delay if we haven't skipped
            pygame.time.delay(interval)
            wait_time += interval
    
    screen.fill((0, 0, 0))
    pygame.display.flip()
    outlet.push_sample([markers[1]])

def play_audio(audio_file, num_times_play, text_lines, event_markers):
    """Play an audio file a specified number of times and display text on screen."""
    markers = event_markers
    outlet.push_sample([markers[0]])
    # screen.fill((0, 0, 0))
    screen.blit(background_image, (0,0))
    font = pygame.font.Font(None, 60)
    y_offset = (screen_height - len(text_lines) * font.get_linesize()) // 2
    
    # Store text rectangles for click detection
    text_rects = []
    for line in text_lines:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
        text_rects.append(text_rect)
        screen.blit(text_surface, text_rect)
        y_offset += font.get_linesize()
    
    pygame.display.flip()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play(num_times_play)
    
    # Wait for the audio to finish playing, pumping events and checking for clicks
    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if click is on any text line
                for text_rect in text_rects:
                    if text_rect.collidepoint(event.pos):
                        pygame.mixer.music.stop()  # Stop the audio
                        break
            elif event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                break
        
        pygame.time.Clock().tick(10)
    
    outlet.push_sample([markers[1]])

def play_video(video_path):
    """Play a video file with a background image with ET air tags."""
    # background_image_path = r"C:\Users\MoBI\Desktop\Custom_MoBI_Software\files for protocol\video_graphomotor2.jpg"
    # background_image = pygame.image.load(background_image_path)
    # background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

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
            skip_rect = draw_skip_button_video(screen) 
            screen.blit(background_image, (0, 0))
            screen.blit(frame_surface, video_pos)
            pygame.display.flip()

        # Handle quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if skip_rect.collidepoint(event.pos):
                    return "next"
            #     if end_rect.collidepoint(event.pos):
            #         outlet.push_sample([84])  # Send final event marker
            #         pygame.quit()
            #         exit()

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
        show_text_screen_videos(text_lines)


# SCREENS ####################
##############################

# Experiment screens
experiment_start = ["Welcome to the Graphomotor Protocol", "", "", "Click 'Next' to continue."]
resting_state_instrc = [
    "You will now start the resting state task",
    "You will now be asked to keep your eyes open and eyes closed",
    "To start, please keep your eyes open and stare at the cross.",
    "", "", "Click 'Next' when you are ready to start."
]
cross = ["+"]
eyes_open = ["Please open your eyes and stare at the cross."]
eyes_closed = ["Please close your eyes. I will tell you when you can open them again."]

# Mind Logger screens
mindlogger_start = ["Now it is time to play on the iPad!", "Please listen to the research assistant.", "", "", "Click 'Next' when task is complete."]
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

# NEW Sync Audio Screens
sync_audio_instrc = [
    "VOLUME ADJUSTMENT",
    "We are going to play a game where you will listen",
    "to sounds and need to whisper with the sounds. Before",
    "we start our game, we need to make sure you can hear",
    "the sounds in the headphones. I will help you adjust the",
    "volume as loud as you can without hurting your ears.",
    "", "", "Press 'Next' to continue."
]
increase_vol = ["Increase the volume to a loud, but comfortable level."]
sync_test_instruc_1 = [
    "SYNCHRONY TEST", "",
    "We are going to play a game where you have to whisper the word 'ta' at",
    "the same speed as a set of sounds you are going to hear. When you hear",  
    "the sound, you will whisper 'ta' at the same speed at the same pace.",
    "Let's do some practice!",
    "", "", "Press 'Next' to continue."
]
speaker_rate_training_instrct = [
    "SPEAKING RATE TRAINING", "",
    "Now you are going to hear a set of sounds. Please be quiet and pay attention",
    "to the speed the sounds are being spoken.",
    "","", "Press 'Next' when you are ready."
]
speaker_rate_training = ["Please pay attention to the speed of sounds and remain silent."]
whisper_ta_instrc = [
    "Now it is your turn!",
    "When I say 'Go', start whispering 'ta' at the SAME SPEED as the",
    "sound you just heard. Can you practice whispering 'ta' for me?",
    "","(Practice whispering 'ta'.)",
    "", "Press 'Next' to continue."
]
whisper_ta = ["Recording! Continue to whisper 'ta ta ta'."]
sync_test_instruc_2 = [
    "SYNCHRONY TEST", "",
    "We are ready to play the game! You will now hear some sounds through your",
    "headphones. While the sounds are playing, you will whisper 'ta', like we",
    "practiced AT THE SAME TIME. You will whisper 'ta' while you are listening to",
    "the sounds and you must whisper 'ta' at the same speed as the sounds. "
    "Remember, you are going to:", "", "", 
    "1) Whisper and do not speak loudly.", "",
    "2) You must whisper 'ta' the entire time the sounds are playing at the same speed the sounds are playing.", "",
    "3) Make sure you look at the cross on the screen while you do it.",
    "", "", "Press 'Next' when ready!"
]

# Video Screens
video_start_instrc = ["You will now watch some videos!", "", "", "Press 'Next' to continue."]

# Break Screen 
break_screen = ["Awesome job! Let's do another task!", "", "", "Press 'Next' to continue."]

# PROTOCOL ##################
##############################

### Start Screen 
show_start_screen()

# Set Full Screen 
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((2560, 1340), pygame.NOFRAME) # 1600x1200, 1920x1080, 1280x1024, 1920,1200, 2560, 1440
screen_width, screen_height = screen.get_size()

# Load background image globally
background_image_path = r"C:\Users\MoBI\Desktop\Custom_MoBI_Software\files for protocol\video_graphomotor2.jpg"
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

### Experiment Start, Resting State 
protocol_flow(experiment_start, resting_state_instrc, event_markers=[[2,3], [4,5]])

### Resting State 
# Eyes Open 1
play_audio(r"C:\Users\MoBI\Documents\resting_state_task\open_eyes.wav", 1, cross, event_markers=[6,7])
show_text_no_buttons(cross, 30000, event_markers=[85,86])
# Eyes Closed 1
play_audio(r"C:\Users\MoBI\Documents\resting_state_task\close_eyes.wav", 1, cross, event_markers=[87,88])
show_text_no_buttons(cross, 30000, event_markers=[89,90])
# Eyes Open 2
play_audio(r"C:\Users\MoBI\Documents\resting_state_task\open_eyes.wav", 1, cross, event_markers=[91,92])
show_text_no_buttons(cross, 30000, event_markers=[93,94])
# Eyes Closed 2
play_audio(r"C:\Users\MoBI\Documents\resting_state_task\close_eyes.wav", 1, cross, event_markers=[95,96])
show_text_no_buttons(cross, 30000, event_markers=[97,98])
# Eyes Open 3
play_audio(r"C:\Users\MoBI\Documents\resting_state_task\open_eyes.wav", 1, cross, event_markers=[99,100])
show_text_no_buttons(cross, 30000, event_markers=[101,102])
# Eyes Closed 3
play_audio(r"C:\Users\MoBI\Documents\resting_state_task\close_eyes.wav", 1, cross, event_markers=[103,104])
show_text_no_buttons(cross, 30000, event_markers=[105,106])
# Eyes Open 4
play_audio(r"C:\Users\MoBI\Documents\resting_state_task\open_eyes.wav", 1, cross, event_markers=[107,108])
show_text_no_buttons(cross, 30000, event_markers=[109,110])
# Eyes Closed 4
play_audio(r"C:\Users\MoBI\Documents\resting_state_task\close_eyes.wav", 1, cross, event_markers=[111,112])
show_text_no_buttons(cross, 30000, event_markers=[113,114])
# Eyes Open 5
play_audio(r"C:\Users\MoBI\Documents\resting_state_task\open_eyes.wav", 1, cross, event_markers=[115,116])
show_text_no_buttons(cross, 30000, event_markers=[117,118])
# Eyes Closed 5
play_audio(r"C:\Users\MoBI\Documents\resting_state_task\close_eyes.wav", 1, cross, event_markers=[119,120])
show_text_no_buttons(cross, 30000, event_markers=[121,122])

### MindLogger
protocol_flow(mindlogger_start, rey_copy_instrc, rey_copy, alpha_instrc, alpha, sprial_dominat_instrc, 
              sprial_dominat, spiral_nondominat_instrc, spiral_nondominat, 
              digit_symbol_sub_instrc, digit_symbol_sub, rey_delay_instrc,
              rey_delay, trails_instrc, trails, 
              event_markers=[[8,9], [10,11],[12,13],[14,15], [16,17],
              [18,19],[20,21],[22,23],[24,25], [26,27],[28,29],[30,31],
              [32,33],[34,35],[36,37]])

### Break 
protocol_flow(break_screen, event_markers=[[38, 39]])

### Sync Audio Test
sync_audio_flow()

### Break 
protocol_flow(break_screen, event_markers=[[72, 73]])

### Videos 
protocol_flow(video_start_instrc, event_markers=[[74,75]])
video_files = [
    r"C:\Users\MoBI\Desktop\Custom_MoBI_Software\files for protocol\Diary of a Wimpy Kid Trailer.mp4",
    r"C:\Users\MoBI\Desktop\Custom_MoBI_Software\files for protocol\despicable_me_clip.mp4",
    r"C:\Users\MoBI\Desktop\Custom_MoBI_Software\files for protocol\the_present.mp4",
    r"C:\Users\MoBI\Desktop\Custom_MoBI_Software\files for protocol\fun_with_fractuals_vol_adj.mp4"
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

