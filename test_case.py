import unittest
import pygame
import os

class TestMyGame(unittest.TestCase):
    def setUp(self):
        # Initialize Pygame
        pygame.init()

    def tearDown(self):
        # Quit Pygame
        pygame.quit()

    def test_game_setup(self):
        # Your provided code
        WIDTH, HEIGHT = 900, 500
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("My first game!")

        WHITE = (255, 255, 255)

        LIFE_FONT = pygame.font.SysFont("jumble", 40)
        WINNER_FONT = pygame.font.SysFont("Jumble", 110)

        SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 65, 45

        YELLOW_SPACESHIP_IMAGE = pygame.image.load(
            os.path.join("Assets", "Spaceship_yellow.png"))
        YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
            YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

        RED_SPACESHIP_IMAGE = pygame.image.load(
            os.path.join("Assets", "Spaceship_red.png"))
        RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
            RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

        # Run the game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Draw something on the screen
            WIN.fill(WHITE)
            WIN.blit(YELLOW_SPACESHIP, (100, 100))
            WIN.blit(RED_SPACESHIP, (400, 300))

            # Render and display the fonts
            life_text = LIFE_FONT.render("Life: 3", True, WHITE)
            WIN.blit(life_text, (10, 10))

            winner_text = WINNER_FONT.render("Winner!", True, WHITE)
            WIN.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2 - winner_text.get_height() // 2))

            # Update the display
            pygame.display.update()

            # Check if the window is closed
            if pygame.event.get(pygame.QUIT):
                break

        # Assert statements for your test
        self.assertEqual(WIDTH, 900)
        self.assertEqual(HEIGHT, 500)
        
 


    

if __name__ == "__main__":
    unittest.main()
