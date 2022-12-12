from numpy import mean


class Person:
    def __init__(self, firstname, lastname, person_id) -> None:
        self.first = firstname
        self.last = lastname
        self.person_id = person_id

    def toString(self) -> str:
        return f'Name: {self.last}, {self.first}\nID: {self.person_id}'


class Student(Person):
    def __init__(self, firstname, lastname, person_id, scores) -> None:
        Person.__init__(self, firstname, lastname, person_id)
        self.scores = scores

    def calculate(self):
        average = mean(self.scores)/len(self.scores)
        if average >= 90:
            return 'O'
        elif average >= 80:
            return 'E'
        elif average >= 7:
            return 'A'
        elif average >= 55:
            return 'P'
        elif average >= 40:
            return 'D'
        else:
            return 'T'
