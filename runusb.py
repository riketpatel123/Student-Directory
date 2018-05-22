
class Grading:

    def __init__(self):

        self.student_id = None
        self.first_name = None
        self.last_name = None
        self.marks = None

    def class_list(self):
        file = open('class.txt', 'r')
        for line in file:
            line = line.rstrip('\n')
            line = line.split('|')

            self.student_id = line[0]
            self.a('a1.txt')
            self.display()
            self.a('a2.txt')
        file.close()

    def a(self, fname ):
        file = open(fname, 'r')
        for line in file:
            line = line.rstrip('\n')
            line = line.split('|')
            if self.student_id in line:
                print('find ',line[1])
                self.marks = line[1]

        file.close()

    def display(self):
        print('>', self.student_id, " == ", self.marks)

if __name__ == "__main__":
    grade = Grading()
    grade.class_list()

    grade.display()