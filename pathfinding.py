import sys
import pygame
from collections import deque

# Program Settings
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
COLUMNS = 25
ROWS = 25

# Program Colors
GRID_COLOR = (19,19,26)
BOX_COLOR = (30,33,45)

# Game Colors
START_COLOR = (240,240,240)
WALL_COLOR = (19,19,26)
TARGET_COLOR = (240,240,240)

# Algorithm Colors
QUEUED_COLOR = (89,94,118)
VISITED_COLOR = (127,152,188)
PATH_COLOR = (198,201,208)

class Box:
    def __init__(self, x, y, box_width, box_height):
        self.x = x
        self.y = y
        self.box_width = box_width
        self.box_height = box_height
        self.start = False
        self.wall = False
        self.target = False
        self.queued = False
        self.visited = False 
        self.neighbors = []
        self.prior = None

    def draw(self, win, color):
        # Draw the boxes in the window
        pygame.draw.rect(win, color, (self.x * self.box_width, self.y * self.box_height, self.box_width - 2, self.box_height - 2))
            
    def set_neighbors(self, grid):
        # Set the neighbors of the box. Left and right, up and down
        if self.x > 0: 
            self.neighbors.append(grid[self.x - 1][self.y]) 
        if self.x < len(grid) - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])
        if self.y < len(grid[0]) - 1:
            self.neighbors.append(grid[self.x][self.y + 1])

class Grid:
    def __init__(self, columns, rows, box_width, box_height):
        self.grid = []
        for i in range(columns):
            row = []
            for j in range(rows):
                row.append(Box(i, j, box_width, box_height))
            self.grid.append(row)
        for i in range(columns):
            for j in range(rows):
                self.grid[i][j].set_neighbors(self.grid)

class Game:
    def __init__(self, window_width, window_height, columns, rows):
        self.window = pygame.display.set_mode((window_width, window_height))
        
        pygame.display.set_caption("Dijkstra's Algorithm Visualizer")
        program_icon = pygame.image.load("program_icon.png")
        pygame.display.set_icon(program_icon)
        
        self.columns = columns
        self.rows = rows
        self.box_width = window_width // columns
        self.box_height = window_height // rows
        self.grid = Grid(columns, rows, self.box_width, self.box_height).grid
        self.start_box = self.grid[0][0]
        self.start_box.start = True
        self.start_box.visited = True
        self.queue = deque([self.start_box])
        self.path = []

    def reset(self):
        self.grid = Grid(self.columns, self.rows, self.box_width, self.box_height).grid
        self.start_box = self.grid[0][0]
        self.start_box.start = True
        self.start_box.visited = True
        self.queue = deque([self.start_box])
        self.path = []
        pygame.display.set_caption("Dijkstra's Algorithm Visualizer")

    def main(self):
        begin_search = False
        target_box_set = False
        searching = True
        target_box = None 

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset()
                        begin_search = False
                        target_box_set = False
                        searching = True
                    elif event.key == pygame.K_SPACE and target_box_set:
                        begin_search = True
                elif event.type == pygame.MOUSEMOTION:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if event.buttons[0] and searching:
                        i = x // self.box_width
                        j = y // self.box_height
                        self.grid[i][j].wall = True
                    if event.buttons[2] and not target_box_set:
                        i = x // self.box_width
                        j = y // self.box_height
                        target_box = self.grid[i][j]
                        target_box.target = True
                        target_box_set = True
                elif event.type == pygame.K_SPACE and target_box_set:
                    begin_search = True

            # Implementation of Dijkstra's Algorithm
            if begin_search:
                pygame.display.set_caption("Dijkstra's Algorithm Visualizer - Searching...")
                if len(self.queue) > 0 and searching:
                    current_box = self.queue.popleft()
                    current_box.visited = True
                    if current_box == target_box:
                        temp = current_box
                        while temp.prior != self.start_box:
                            self.path.append(temp.prior)
                            temp = temp.prior
                        pygame.display.set_caption(f"Dijkstra's Algorithm Visualizer - Path Found! Distance: {len(self.path)}")
                        searching = False
                        begin_search = False
                        while current_box.prior != self.start_box:
                            self.path.append(current_box.prior)
                            current_box = current_box.prior
                    else:
                        for neighbor in current_box.neighbors:
                            if not neighbor.queued and not neighbor.wall:
                                neighbor.queued = True
                                neighbor.prior = current_box
                                self.queue.append(neighbor)
                else:
                    if searching:
                        pygame.display.set_caption("Dijkstra's Algorithm Visualizer - No Solution Found")
                        searching = False
                        begin_search = False   

            self.window.fill(GRID_COLOR)
            for i in range(len(self.grid)):
                for j in range(len(self.grid[0])):
                    box = self.grid[i][j]
                    box.draw(self.window, BOX_COLOR)
                    if box.queued:
                        box.draw(self.window, QUEUED_COLOR)
                    if box.visited:
                        box.draw(self.window, VISITED_COLOR)
                    if box in self.path:
                        box.draw(self.window, PATH_COLOR)
                    if box.start:
                        box.draw(self.window, START_COLOR)
                    if box.wall:
                        box.draw(self.window, WALL_COLOR)
                    if box.target:
                        box.draw(self.window, TARGET_COLOR)

            pygame.display.update()

if __name__ == "__main__":
    game = Game(WINDOW_WIDTH, WINDOW_HEIGHT, COLUMNS, ROWS)
    game.main()