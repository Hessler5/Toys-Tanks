import pygame
from projectile import Projectile

class Seeker_Projectile(Projectile):
    def __init__(self, x, y, rotation):
        Projectile.__init__(self, x, y, rotation)
        self.initial_rotation = rotation

