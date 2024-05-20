
class Participants:

    def __init__(self):
        self.incomingParticipants = []
        self.participants = []


    def addParticipant(self, participantNum: int = -1, time = -1):
        new_entry = {
            'ParticipantNum': participantNum,
            'Time': time
        }
        self.participants.append(new_entry)

    def updateParticipantNum(self, index: int, participantNum: int):
        self.participants[index]['ParticipantNum'] = participantNum

    def logParticipantTime(self, index: int, time):
        self.participants[index]['Time'] = time
    
    def removeParticipant(self, index: int):
        self.participants.pop(index)


    def addIncomingParticipant(self, participantNum: int):
        self.incomingParticipants.append(participantNum)
    
    
    def setParticipantTime(self, index, time):
        if(len(self.participants) < index):
            return

        self.participants[index]['Time'] = time


    def showResults(self):

        for participant in self.participants:
            print(participant)