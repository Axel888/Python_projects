class SoccerPlayer:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goals = 1):  # голы.
        self.goals += goals

    def make_assist(self, assists = 1):  # передачи.
        self.assists += assists

    def statistics(self):  # статистика.
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')
