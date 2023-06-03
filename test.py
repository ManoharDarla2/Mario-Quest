import pyglet
import math
from utils.resources import brick_img

class Enemy(pyglet.sprite.Sprite):
    def __init__(self, x, y, dest1, dest2):
        super().__init__(brick_img, x, y)
        self.destinations = [dest1[0], dest2[0]]  # List of destinations to move between
        self.current_destination = 1  # Index of the current destination

    def move(self, dt):
        dest_x = self.destinations[self.current_destination]
        speed = 100  # Adjust this value to control the enemy's speed

        if abs(dest_x - self.x) < speed * dt:
            # The enemy has reached the current destination
            self.current_destination = (self.current_destination + 1) % len(self.destinations)
        else:
            # Move towards the current destination
            if dest_x > self.x:
                self.x += speed * dt
            else:
                self.x -= speed * dt

# Create a window
window = pyglet.window.Window(800, 600)

# Create an enemy
enemy = Enemy(100, 100, (400, 300), (700, 500))

@window.event
def on_draw():
    window.clear()
    enemy.draw()

def update(dt):
    enemy.move(dt)

# Schedule the update function to be called every frame
pyglet.clock.schedule_interval(update, 1/60.0)

pyglet.app.run()
