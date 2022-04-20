import sys
import time

'''rows = int(input("Enter the number of rows in your table:\n"))
if rows == 0:
    sys.exit()
elif rows == 1:
    sys.exit()
table = []'''
class getratio(object):
    def __init__(self, rows, table):
        self.rows = rows
        self.table = table
        for i in range(rows):
            self.currentrow = []
            self.x = float(input("Enter the x value:\n"))
            self.y = float(input("Enter the y value:\n"))
            self.currentrow.append(self.x)
            self.currentrow.append(self.y)
            table.append(self.currentrow)
    def findratios(self):
        self.changes = []
        for a in range(self.rows):
            if a>=1:
                self.ychangecurrentrow = self.table[a][1]/self.table[a-1][1]
                self.xchangecurrentrow = self.table[a][0]-self.table[a-1][0]
                self.currentrowratio = self.ychangecurrentrow/self.xchangecurrentrow
                self.changes.append(self.currentrowratio)
    def checkratio(self, list):
        for x in list:
            if x==list[0]:
                pass
            else:
                return False
        return True
    def makeequation(self, correct = True):
        if correct:
                ratio = self.changes[0]
                testy = self.table[0][1]
                testx = self.table[0][0]
                constx = ratio**testx
                a = testy/constx
                print(f"f(x) = {a}*{ratio}^x")
        else:
            print("No Constant")

'''if __name__ == '__main__':
    obj = getratio(rows, table)
    obj.findratios()
    a = obj.checkratio(obj.changes)
    obj.makeequation(a)'''
