import pygame
import random
import time
import sys  # Import sys to exit the program

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
w, h = screen.get_size()

# Define settings
state = {
    "fps": 50,
    "color": (0, 255, 0),  # RGB green
    "charset": "0123456789ABCDEFabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]{}|;:,.<>?/~`",
    "size": 16,
    "fadeEffect": True
}

# Font for rendering characters
font = pygame.font.SysFont("monospace", state["size"])

# Array to track column positions
p = [0] * (w // state["size"])

# Create a surface to hold the previous frame for fading
fade_surface = pygame.Surface((w, h))
fade_surface.fill((0, 0, 0))  # Start with a black background

# Time tracking variables
last_activity_time = time.time()  # Last time user interacted
inactivity_limit = 0 * 0  # 5 minutes in seconds
screensaver_active = False  # Track if screensaver is running

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()  # Exit the program immediately when the window is closed

        # If there is any event (mouse move, key press), reset the inactivity timer
        if event.type in [pygame.KEYDOWN, pygame.MOUSEMOTION]:
            last_activity_time = time.time()  # Reset the inactivity timer
            if screensaver_active:
                # If the screensaver is active and any key/mouse event happens, stop the screensaver and exit
                running = False

    # Check if the user has been inactive for 5 minutes
    if not screensaver_active and time.time() - last_activity_time > inactivity_limit:
        screensaver_active = True  # Activate the screensaver after 5 minutes of inactivity

    if screensaver_active:
        # Optional fade effect for a better visual appearance
        if state["fadeEffect"]:
            fade_surface.fill((0, 0, 0))  # Reset the fade surface
            fade_surface.set_alpha(10)  # Adjust transparency for smooth fade
            screen.blit(fade_surface, (0, 0))  # Draw the faded surface
        else:
            screen.fill((0, 0, 0))  # Full clear if fade is off

        # Loop through each column and draw characters
        for i in range(len(p)):
            char = random.choice(state["charset"])
            text = font.render(char, True, state["color"])
            screen.blit(text, (i * state["size"], p[i] * state["size"]))

            # Reset position when character reaches the bottom
            if p[i] * state["size"] > h and random.random() > 0.975:
                p[i] = 0
            p[i] += 1

        # Update the fade surface for next frame
        fade_surface.blit(screen, (0, 0))

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(state["fps"])

# Quit pygame
pygame.quit()
sys.exit()  # Exit the program after the game loop ends