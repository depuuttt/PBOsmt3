import sys


class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def limitFunc(self):
        if self.hours > 24:
            print("Hours can not go past 24")
            print("Please try again. ^_^")
            return False
        if self.minutes > 60:
            print("Minutes can not go past 60")
            print("Please try again. ^_^")
            return False
        if self.seconds > 60:
            print("Seconds can not go past 60")
            print("Please try again. ^_^")
            return False
        else:
            return True

    def result(self):
        print(str(self.hours) + " : " +
              str(self.minutes) + " : " + str(self.seconds))


hours = input("Masukkan Jam   : ")
minutes = input("Masukkan Menit : ")
seconds = input("Masukkan Detik : ")

time = Time(int(hours), int(minutes), int(seconds))

if not time.limitFunc():
    exit()

time.result()
