
class Grading:

    def __init__(self):

        self.student_id = None
        self.first_name = None
        self.last_name = None
        self.student_list = []
        self.alist = []
        self.outoff = None
        self.a1_marks = None

    def class_list(self):
        file = open('class.txt', 'r')
        for line in file:
            data = line.rstrip('\n')
            self.student_list.append(data.split('|'))
        print('Student List')
        for i in range(len(self.student_list)):
            for j in range(len(self.student_list[i])):
                if j == 0:
                    self.student_id = self.student_list[i][j]
                elif j == 1:
                    self.first_name = self.student_list[i][j]
                elif j == 2:
                    self.last_name = self.student_list[i][j]
            print(self.student_id, "  ", self.first_name, "  ", self.last_name)
        file.close()

    def a(self, fname ):
        file = open(fname, 'r')
        self.alist = []
        for line in file:
            data = line.rstrip('\n')
            self.alist.append(data.split('|'))
        print('Assignment',fname)
        for i in range(1, len(self.alist)):
            for j in range(len(self.alist[i])):
                self.outoff = self.alist[0][0]
                if j == 0:
                    self.student_id = self.alist[i][j]
                elif j == 1:
                    self.marks = self.alist[i][j]
            print(self.student_id,' >> ', self.marks, '/', self.outoff)

    def choice(self, id):
        if( id in self.student_list[0]):
            print(self.student_list[0])


if __name__ == "__main__":
    grade = Grading()
    grade.class_list()
    grade.a('a1.txt')
    grade.a('a2.txt')
    grade.choice('9798')