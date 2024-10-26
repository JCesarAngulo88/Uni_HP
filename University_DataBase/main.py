#   *Create a Class named SchoolDatabase Base following the next conditions:
#   -Use a py as a database where all constants are assigned (teachers, students, trainees, coaches, topics, etc etc) -> Done
#   -Use list and tuples -> Done
#   -In the init the list or tuples should be empty/None and check this attribute
#   -Create Methods to add/remove teachers, students etc etc
#   -Create Methods to show all the values of the lists class
#   -Create a Class named XXXXteam (sports team) that inherits SchoolDataBase

from db.db_school import *
from db.db_quidditch import *

class TooManyStudents(Exception):
    pass

class SchoolDataBase:
    #Constructor
    def __init__(self, instructor=None, trainee=None, subject=''): #Attributes should be None
        '''if instructor not in [['Severus Snape'], ['Albus Dumbledore'], ['Alastor Moody'], ['Rubeos Hagrid'], ['Rolanda Hooch'], None]:
            raise ValueError('Invalid instructor')
        if trainee not in [['Harry Potter'], ['Ron Weasley'], ['Hermione Granger'], ['Draco Malfoy'], ['Luna Lovegood'], ['Cho Chang'], ['Cedric Diggory'], ['Neville Longbottom'], ['Ginny Weasley'], ['Fleur Delacour'], None]:
            raise ValueError('Invalid trainee')
        if subject not in ['Defense Against the Dark Arts', 'Potions', 'Transfiguration', 'Charms',
                           'History of Magic', 'Astronomy', 'Herbology', 'How to get the Golden Snitch', '']:
            raise ValueError('Invalid subject')'''
        if instructor not in [None]:
            raise ValueError('Instructor Box/Var/List should be empty')
        if trainee not in [None]:
            raise ValueError('trainee Box/Var/List should be empty')
        if subject not in ['']:
            raise ValueError('subject Box/Var/List should be empty')
        #Instance attributes
        self.instructor = instructor if instructor is not None else []
        self.trainee = trainee if trainee is not None else []
        self.subject = subject  # if subject is not None else []

    def add_trainee(self, trainee_name): #Instance methods
        """Add a trainee to the school database"""
        if trainee_name not in self.trainee:
            if len(self.trainee) <= 9:
                self.trainee.append(trainee_name)
                print(f"{trainee_name} has been added as a trainee.")
            else:
                print('\nEnter\n')
                raise TooManyStudents
        else:
            print(f"{trainee_name} is already a student.")

    def remove_trainee(self, trainee_name):
        """Remove a trainee from the school database"""
        if trainee_name in self.trainee:
            self.trainee.remove(trainee_name)
            print(f"{trainee_name} has been removed from the database.")
        else:
            print(f"{trainee_name} is not found in the database.")

    def add_instructor(self, instructor_name):
        """Add a teacher to the classroom."""
        if instructor_name not in self.instructor:
            self.instructor.append(instructor_name)
            print(f"{instructor_name} has been added as a database.")
        else:
            print(f"{instructor_name} is already a database.")

    def remove_instructor(self, instructor_name):
        """Remove a teacher from the classroom."""
        if instructor_name in self.instructor:
            self.instructor.remove(instructor_name)
            print(f"{instructor_name} has been removed from the database.")
        else:
            print(f"{instructor_name} is not found in the database.")

    def show_info(self):
        print(f"\nClassroom of {self.subject} trainees")
        for trainee_name in self.trainee:
            print(f'- {trainee_name}')

        print(f"\nTotal number of trainees: {len(self.trainee)}")

        print("\nTeachers in the classroom: \n")
        for instructor_name in self.instructor:
            print(f"- {instructor_name}")

        print(f"Total number of instructors: {len(self.instructor)} \n")

class QuidditchTeam(SchoolDataBase):
    def __init__(self, instructor=None, trainee=None, subject='', position='', house=''):
        super().__init__(instructor, trainee, subject)
        if position not in ['']:
            raise ValueError('Position Box/Var/List should be empty')
        if house not in ['']:
            raise ValueError('House Box/Var/List should be empty')
        self.position = position
        self.house = house

    def show_info(self):
        print(f"\nHouse of {self.house} players Quidditch team")
        for trainee_name in self.trainee:
            print(f'- {trainee_name}')

        print(f"\nTotal number of Quidditch players: {len(self.trainee)}")

        print("\nCoaches in the Quidditch team:")
        for instructor_name in self.instructor:
            print(f"- {instructor_name}")

        print(f"Total number of instructors: {len(self.instructor)}")

def add_init_dada_elements(dada_classroom, _dada_students, _dada_teachers, dada_subject):
    # Classroom objects

    dada_classroom.add_instructor(_dada_teachers[default_dada_teacher])
    dada_classroom.subject = dada_subject
    for inc, element in enumerate(_dada_students):
        dada_classroom.add_trainee(_dada_students[inc])


    ##print(
      #  f'The Teacher is {dada_classroom.instructor[0]} the students are {dada_classroom.trainee} and the subject is {dada_classroom.subject}\n')


def add_init_quidditch_gryffindor_elements(quidditch_gryffindor_team, data_gryffindor_players, quidditch_coaches):
    '''gryffindor_house = QuidditchTeam(['Rolanda Hooch'],
                                     ['Harry Potter'],
                                     'How to get the Golden Snitch',
                                     'Seeker',
                                     'Gryffindor')'''
    #gryffindor_house = QuidditchTeam()
    quidditch_gryffindor_team.add_instructor(quidditch_coaches[0])
    quidditch_gryffindor_team.subject = 'How to get the Golden Snitch'
    quidditch_gryffindor_team.house = general_houses[GRYFF_HOUSE]
    quidditch_gryffindor_team.position = general_quidditch_positions[0]

    for inc, element in enumerate(data_gryffindor_players):
        quidditch_gryffindor_team.add_trainee(data_gryffindor_players[inc])

    quidditch_gryffindor_team.show_info()

def main():
    dada_classroom = SchoolDataBase()
    '''add_init_dada_elements(dada_classroom, dada_students, dada_teachers, 'Defense Against the Dark Arts')
    dada_classroom.show_info()

    dada_classroom.add_trainee('Harry Potter')
    dada_classroom.show_info()

    dada_classroom.remove_trainee('Luna Lovegood')
    dada_classroom.show_info()

    dada_classroom.remove_instructor('Barty Crouch Jr')
    dada_classroom.show_info()'''

    quidditch_gryffindor_team = QuidditchTeam()
    add_init_quidditch_gryffindor_elements(quidditch_gryffindor_team, data_gryffindor_players, quidditch_coaches)

    quidditch_gryffindor_team.add_trainee('Luna Lovegood')
    quidditch_gryffindor_team.show_info()

    quidditch_gryffindor_team.remove_trainee('Harry Potter')
    quidditch_gryffindor_team.show_info()

    quidditch_gryffindor_team.remove_instructor('Rolanda Hooch')
    quidditch_gryffindor_team.show_info()

    quidditch_gryffindor_team.add_instructor('Julio Cesar')
    quidditch_gryffindor_team.show_info()

    quidditch_gryffindor_team.add_trainee('Harry Potter')
    quidditch_gryffindor_team.show_info()

    #quidditch_gryffindor_team.add_trainee('Hermione Granger')
    #quidditch_gryffindor_team.show_info()

if __name__ == "__main__":
    main()
