#This will include 4 functions
"""
1.To read a text file and extract list of students.
2.To verify if a student is in the list.
3.To count the number of times the name of a particular student showed in the list obtained from the text file.
4.To tell the position/line number at which certain student is in the list or first appeared in the list.
"""

def readTextFile(file):
    """ Function number 1 """
    list = []
    with open(file, 'r') as f:
        for name in f:
            list.append(name.rstrip())
    return list

def Is_Listed(item, lst):
    """ Function number 2 """
    for i in lst:
        if i == item:
            return True
    return False

def count(item, lst):
    """ Function number 3 """
    total = 0
    for i in lst:
        if i == item:
            total += 1
    return total


class MarksStudentNav:
    #Init funciton of this class
    def __init__(self, file):
        self.file = file

    #To get the list of items in file.txt
    def get_list(self):
        self.lst = []
        with open(self.file, 'r') as f:
            for value in f:
               self.lst.append(value.rstrip())
        return self.lst

    #To get the frequency of certain item in file.txt
    def count_frequence_item(self, item):
        self.lst = []
        with open(self.file, 'r') as f:
            for value in f:
               self.lst.append(value.rstrip())
        total = 0
        for i in self.lst:
            if i == item:
                total += 1
        if total == 0:
            return f"The item {item} is not found in {self.file}"
        else:
            return f"{item} has frequency {total} in {self.file}"

    #To count the total distinct item in file.txt
    def count_number_item(self):
        num_student = set(self.lst)
        return len(num_student)


