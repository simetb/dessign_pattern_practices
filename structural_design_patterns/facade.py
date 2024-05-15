"""
    Facade
    Facade pattern provides a simplified interface to a complex subsystem
"""


class Computer:
    def get_electro_shock():
        print("Ouch")
    
    def make_a_sound():
        print("Beep Beep")

    def show_loading_screen():
        print("Loading")
    
    def bam():
        print("ready to use!")

    def close_everything():
        print("bup bup bup buzzzzz")

    def sooth():
        print("Zzzz")

    def pull_current():
        print("Haaaah!")

class ComputerFacade():

    def __init__(self, computer : Computer):
        self.computer = computer
    
    def turn_on(self):
        self.computer.get_electro_shock()
        self.computer.make_a_sound()
        self.computer.show_loading_screen()
        self.computer.bam()
    
    def turn_off(self):
        self.computer.close_everything()
        self.computer.pull_current()
        self.computer.sooth()


if __name__ == "__main__":
    computer = ComputerFacade(Computer)
    print("Powering On!")
    computer.turn_on()
    print("\nPowering Off!")
    computer.turn_off()