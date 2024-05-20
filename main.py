import sys
from PySide6 import QtWidgets

from clock import Clock
from participants import Participants
from mainScreen import MyWidget
from timeScreen import TimeScreen

# num_participants = input("Enter the number of participants: ")

# print(num_participants)


# input("Press enter to start the race!!")
# clock = Clock()


# print("The race has started at")
# print(clock.getStartTime())

# participants_line = []

# # logged_times = {}
# logged_times = []

if __name__ == "__main__":

    clock = Clock()
    participants = Participants()


    print("The race has started at")
    print(clock.getStartTime())

    app = QtWidgets.QApplication([])

    widget = MyWidget(clock=clock, participants=participants)
    widget.resize(1200, 600)
    widget.show()

    time_widget = TimeScreen(clock=clock)
    time_widget.resize(1200, 600)
    time_widget.show()

    sys.exit(app.exec())

# entered_input = ''
# while True:

#     entered_input = input("Press enter to set a time (enter e to end the race): ")
#     if(entered_input == 'e'):
#         break

#     if(len(entered_input) > 0):
#         participant_nums = entered_input.split()
#         for participant_num_str in participant_nums:
#             participant_num = int(participant_num_str)
#             participants_line.append(participant_num)

#     else:
#         elapsedTime = clock.elapsedTime()
#         print(elapsedTime)

#         finisher_num = -1
#         if(len(participants_line) > 0):
#             finisher_num = participants_line.pop(0)
#             print(participants_line)

#         # logged_times[finisher_num] = time_diff
#         logged_times.append({finisher_num: elapsedTime})

# print(logged_times)
