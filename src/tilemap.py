import pygame
import os
import csv

#Tile Type Constants
GRASS = 0 
WATER = 1
SAND = 2

#Tiles the player cannot walk on
SOLID_TILES = [WATER]

class Tilemap:
    """
    Manages the game world as a grid of tiles.
    Each cell in the grid contains a tile type integer.
    """

    def __init__(self, map_path, tile_size=32):
        self.tile_size = tile_size
        self.grid = []

        #Load tile images
        self.tiles = {
            GRASS: pygame.image.load(
                os.path.join("../assets/sprites/tile_grass.png")
            ),
            WATER: pygame.image.load(
                os.path.join("../assets/sprites/tile_water.png")
            ),
            SAND: pygame.image.load(
                os.path.join("../assets/sprites/tile_sand.png")
            ),
        }

        #Load map from csv
        self.load_map(map_path)


    def load_map(self, map_path):
        """Read the CSV file and build the grid"""
        self.grid = []
        with open(map_path, "r", encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            for row in reader:
                self.grid.append([int(tile) for tile in row])
    
    def is_solid(self, grid_x, grid_y):
        """
        Check if a tile at grid coordinates is solid.
        Returns True if the player cannot walk there.
        """
        #Check map boarders first
        if grid_x < 0 or grid_y < 0:
            return True
        if grid_y >= len(self.grid):
            return True
        if grid_x >= len(self.grid[grid_y]):
            return True
        
        #Check tile type
        return self.grid[grid_y][grid_x] in SOLID_TILES

    def draw(self, screen):
        """Draw every tile in the grid onto the screen."""
        for row_index, row in enumerate(self.grid):
            for col_index, tile_type in enumerate(row):
                x = col_index * self.tile_size
                y = row_index * self.tile_size
                screen.blit(self.tiles[tile_type], (x,y))