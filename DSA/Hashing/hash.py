'''dict  = {"day1" : "5hr", "day2" : "3hrs" , "day3" : "5hrs" ,
"day5" : "6hrs"}

class hesh:
    def __init__(self):
        self.size = 10
        self.ar =  [None] * self.size

    def gethash(self, word):
        h = 0
        for i in word:
            h += ord(i)
        return h % self.size

    def __setitem__(self, key , val):
        h = self.gethash(key)
        self.ar[h] = val

    def __getitem__(self, key):
        h = self.gethash(key)
        return self.ar[h]

    def __delitem__(self, key):
        h = self.gethash(key)
        self.ar[h] = None

t = hesh()
#t.add('day3' , '10hrs')
t['day10'] = '2hrs'
t['day11'] = '1hrs'
#print(t['day10'])
del t["day1"]
print(t.ar)'''


class Hash_table:
    def __init__(self):
       self.max = 10
       self.arr = [None] * self.max

    def get_hesh(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.max

    def __setitem__(self, key, val):
        h = self.get_hesh( key)
        self.arr[h] = val

    def __getitem__(self, key):
        h =self.get_hesh(key)
        return self.arr[h]


ha = Hash_table()
ha['suman'] = 30
ha['su'] = 27
ha['suu'] = 26

ha['priya'] = 25

print(ha['priya'])

