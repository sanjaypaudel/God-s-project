# remember to install python 362
# brew install python3
from DatabaseConfiguration import dbconfig
import csv

class FileParser:

    #==============================================================
    # Behaviour Declaration
    #==============================================================

    def _nonblank_lines(self, f):
        for l in f:
            line = l.rstrip()
            if line:
                yield line

    def __init__(self, filename):

        db=DBConfig()
        with open(filename) as file:
            if filename[-3:]=="csv":
                csent = csv.reader(file, delimiter=",")
                for line in csent:
                    print(line) #incomplete
            else:
                for line in self._nonblank_lines(file):
                    if line[:1] != "#":
                        add_testcases = "INSERT INTO testcases(source) VALUES(%s)"
                        db.cursor.execute(add_testcases,(line,))
                    # for language: db.cursor.execute("INSERT INTO languages (name) VALUE ('%s')" %line)

        # close file
        file.close()

        # commit just in case
        db.db.commit()


#==============================================================
# Example of Class Declaration
#==============================================================

#filename = input("Please enter a filename: ")
#fileClass = FileParser(filename)