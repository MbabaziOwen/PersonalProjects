import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spinning Dice")

# Load dice images (Make sure you have dice images like 1.png, 2.png, ..., 6.png)
dice_images = [pygame.image.load(f"{i}.png") for i in range(1, 7)]

# Clock to control the frame rate
clock = pygame.time.Clock()

# Function to rotate an image
def rotate_image(image, angle):
    return pygame.transform.rotate(image, angle)

def main():
    running = True
    angle = 0
    current_dice = random.choice(dice_images)

    while running:
        screen.fill((0, 0, 0))  # Clear screen with black color

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Press space to roll the dice
                    current_dice = random.choice(dice_images)

        # Rotate the dice
        angle += 5  # Increment the angle
        rotated_dice = rotate_image(current_dice, angle)

        # Get the rectangle of the rotated image and center it
        rect = rotated_dice.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(rotated_dice, rect.topleft)

        pygame.display.flip()  # Update the display
        clock.tick(30)  # Run at 30 frames per second

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
