from numpy.core.shape_base import block
import pygame
from pygame.constants import K_r
from pygame.locals import K_DOWN, K_UP, K_LEFT, K_RIGHT, K_ESCAPE, \
    KEYDOWN, QUIT
import numpy as np

pygame.init()



BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
blockSize = 400//7 

def drawGrid():
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill((0,0,0))

def dfs(row, col):
        global board
        board[row][col].visited = True
        rect = pygame.Rect(row*blockSize, col*blockSize, blockSize, blockSize)
        pygame.draw.rect(screen, (255,0,0), rect, 1)
        for neighbor in board[row][col].neighbors:
            if neighbor.value == 2:
                rect = pygame.Rect(neighbor.row*blockSize, neighbor.col*blockSize, blockSize, blockSize)
                pygame.draw.rect(screen, (255,0,0), rect, 1)
                break
                
            if neighbor.visited == False:
                return dfs(neighbor.row,neighbor.col)
            
    

class Node:
    def __init__(self, row, col, value):
        self.value = value
        self.visited = False
        self.row = col
        self.col = row
        self.neighbors = []
    def add_neighbors(self):
        try:
            if (self.col+1)<7:
                neighbor = board[self.row][self.col+1]
                if neighbor.value != 1:
                    self.neighbors.append(neighbor)
        except Exception as e:
            pass
        try:
            if (self.row+1)<7:
                neighbor = board[self.row+1][self.col]
                if neighbor.value != 1:
                    self.neighbors.append(neighbor)
        except Exception as e:
            pass
        try:
            if (self.col-1)>=0:
                neighbor = board[self.row][self.col-1]
                if neighbor.value != 1:
                    self.neighbors.append(neighbor)
        except Exception as e:
            pass
        try:
            if (self.row-1)>=0:
                neighbor = board[self.row-1][self.col]
                if neighbor.value != 1:
                    self.neighbors.append(neighbor)
        except Exception as e:
            pass
    

global board
board = np.zeros((7,7))
board = board.tolist()
class Maze:
        
    def place(self, row, col):
        global board
        if board[row][col] == 0:
            board[row][col] = 1


global x, y
x = 0
y = 0


drawGrid()

game = Maze()
game_over = False
while not game_over:

    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_over=True
            elif event.key == K_RIGHT:
                for i in range(7):
                    for j in range(7):
                        board[i][j] = Node(i, j, board[i][j])
                for i in range(7):
                    for j in range(7):
                        board[i][j].add_neighbors()
                dfs(0,0)
              

            elif event.key == K_UP:
                pos = pygame.mouse.get_pos()
                y = (pos[0])//blockSize
                x = (pos[1])//blockSize
                rect = pygame.Rect(y*blockSize, x*blockSize, blockSize, blockSize)
                pygame.draw.rect(screen, (0,0,255), rect, 1)
                board[x][y] = 2
                print(board)
            elif event.key == K_LEFT:
                board = np.zeros((7,7))
                board = board.tolist()
                screen.fill((0,0,0))
                drawGrid()
           
                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = (pos[0])//blockSize
            row = (pos[1])//blockSize
            game.place(row,col)

        
    for i in range(7):
                for j in range(7): 
                        if(board[i][j]==1):
                            rect = pygame.Rect(j*blockSize, i*blockSize, blockSize, blockSize)
                            pygame.draw.rect(screen, BLACK, rect, 1)
    rect = pygame.Rect(0, 0, blockSize, blockSize)
    pygame.draw.rect(screen, (0,255,0), rect, 1)    
    pygame.display.update()
                