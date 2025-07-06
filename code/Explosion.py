import pygame

class Explosion:
    def __init__(self, image_path, frame_size, num_frames, position):
        self.sprite_sheet = pygame.image.load(image_path).convert_alpha()
        self.frame_width, self.frame_height = frame_size
        self.num_frames = num_frames
        self.frames = [
            self.sprite_sheet.subsurface((i * self.frame_width, 0, self.frame_width, self.frame_height))
            for i in range(num_frames)
        ]
        self.index = 0
        self.position = (position[0] - self.frame_width // 2, position[1] - self.frame_height // 2)
        self.done = False
        self.frame_delay = 4
        self.counter = 0

    def update(self):
        self.counter += 1
        if self.counter >= self.frame_delay:
            self.counter = 0
            self.index += 1
            if self.index >= self.num_frames:
                self.done = True

    def draw(self, surface):
        if not self.done:
            surface.blit(self.frames[self.index], self.position)

# Developed by: Saulo Ruan Nascimento Oliveira