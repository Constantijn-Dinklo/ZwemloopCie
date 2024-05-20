from functools import partial
from PySide6 import QtWidgets

from clock import Clock
from participants import Participants

import csv

class MyWidget(QtWidgets.QWidget):

    def __init__(self, clock: Clock, participants: Participants):
        super().__init__()

        self.clock = clock
        self.logged_times = []
        self.participants = participants


        self.time_table = QtWidgets.QTableWidget(100, 2)
        self.time_table.setHorizontalHeaderLabels(["Time", "Remove"])


        self.result_table = QtWidgets.QTableWidget(100, 3)
        self.result_table.setHorizontalHeaderLabels(["Participant Number", "Time"])

        self.participant_num_input = QtWidgets.QLineEdit()
        self.participant_num_input.textChanged.connect(self.updateParticipantNum)
        self.participant_num_enter = QtWidgets.QPushButton("Add")
        self.participant_num_enter.clicked.connect(self.addParticipant)

        self.start_time_input = QtWidgets.QLineEdit()
        # self.start_time_input.textChanged.connect()
        self.start_time_button = QtWidgets.QPushButton("(Re)-Start Time")
        self.start_time_button.clicked.connect(self.restartTime)


        self.log_time_button = QtWidgets.QPushButton("Log Time")
        self.log_time_button.clicked.connect(self.logTime)

        self.create_result_file_button = QtWidgets.QPushButton("Results")
        self.create_result_file_button.clicked.connect(self.createResultFile)

        # self.show_results_button = QtWidgets.QPushButton("Show Results")
        # self.show_results_button.clicked.connect(self.showResults)



        self.layout = QtWidgets.QGridLayout(self)
        # self.layout.addWidget(self.time_table, 1, 0, 1, 3)
        # self.layout.addWidget(self.participant_num_input, 2, 0, 1, 1)
        # self.layout.addWidget(self.participant_num_enter, 2, 1, 1, 1)
        self.layout.addWidget(self.result_table, 1, 0, 1, 1)
        self.layout.addWidget(self.start_time_input, 4, 0, 1, 2)
        self.layout.addWidget(self.start_time_button, 4, 2, 1, 2)
        self.layout.addWidget(self.log_time_button, 5, 0)
        self.layout.addWidget(self.create_result_file_button, 6, 0)
        # self.layout.addWidget(self.show_results_button, 5, 0)

    def restartTime(self):
        # print(self.start_time_input.value)

        self.clock.startClock()
    
    # def updateStartText(self):

    def logTime(self):
        elapsed_time = self.clock.elapsedTime()
        self.participants.addParticipant(time=elapsed_time)
        self.constructResultTable()

    def updateParticipantNum(self, index, text):        
        self.participants.updateParticipantNum(index=index, participantNum=text)


    def constructTimeTable(self):

        self.time_table.clearContents()

        for index, time in enumerate(self.logged_times):
            time_entry = QtWidgets.QTableWidgetItem(str(time))
            self.time_table.setItem(index, 0, time_entry)
    
    def constructResultTable(self):

        self.result_table.clearContents()

        for index, participant in enumerate(self.participants.participants):

            # ----- Number -----
            participant_num_entry = QtWidgets.QLineEdit(str(participant['ParticipantNum']))
            participant_num_entry.textChanged.connect(partial(self.updateParticipantNum, index))
            self.result_table.setCellWidget(index, 0, participant_num_entry)

            # participant_num_entry = QtWidgets.QTableWidgetItem(str(participant['ParticipantNum']))
            # self.result_table.setItem(index, 0, participant_num_entry)

            # ----- Time -----
            time = participant['Time']

            if time == -1:
                log_time_button = QtWidgets.QPushButton("Log Time")
                log_time_button.clicked.connect(partial(self.logParticipantTime, index))
                self.result_table.setCellWidget(index, 1, log_time_button)
            else:
                participant_time_entry = QtWidgets.QTableWidgetItem(str(participant['Time']))
                self.result_table.setItem(index, 1, participant_time_entry)

            # ----- Remove Button -----
            remove_participant_button = QtWidgets.QPushButton("Remove")
            remove_participant_button.clicked.connect(partial(self.remove_entry, index))
            self.result_table.setCellWidget(index, 2, remove_participant_button)
    
   
    def showResults(self):
        self.participants.showResults()


    def addParticipant(self):
        self.participants.addParticipant()

        self.constructResultTable()

    def logParticipantTime(self, index):
        elapsed_time = self.clock.elapsedTime()

        self.participants.logParticipantTime(index=index, time=elapsed_time)

        self.constructResultTable()

    def remove_entry(self, index):

        self.participants.removeParticipant(index)
        self.constructResultTable()

    def createResultFile(self):

        with open('results.csv', 'w', newline='') as csvfile:

            fieldnames = ['Participant Number', 'Time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for participant in self.participants.participants:

                writer.writerow({'Participant Number': participant['ParticipantNum'], 'Time': participant['Time']})

