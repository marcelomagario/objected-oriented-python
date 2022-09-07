# Class
# Syntax
# Brand, Memory RAM, Video Board

# Constructor. This method called when an object is created from the class
#  it allow the class to initialize the attributes of a class.
class Computer:
    def __init__(self, brand, memory_ram, video_board):
        self.brand = brand
        self.memory_ram = memory_ram
        self.video_board = video_board

    # Methods

    def turn_on(self):
        print(f"I'm turning the computer on the computer: {self.brand}")

    def turn_off(self):
        print(f"I'm turning the computer off the computer: {self.brand}")

    def computer_settings(self):
        print(self.brand, self.memory_ram, self.video_board)
# Instance
if __name__ == '__main__':
    computer1 = Computer(brand='Dell', memory_ram='128DDR', video_board='AMD Radeon')
    computer1.turn_on()
    computer1.turn_off()
    computer1.computer_settings()
