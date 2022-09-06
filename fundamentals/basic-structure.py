# Class
# Syntax

# Brand, Memory RAM, Video Board

# Constructor. This method called when an object is created from the class
#  it allow the class to initialize the attributes of a class.
class Computer():
    def __init__(self, brand, memory_ram, video_board):
        self.video_board = video_board
        self.memory_ram = memory_ram
        self.brand = brand

