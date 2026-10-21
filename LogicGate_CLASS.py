from Connector import Connector

class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label
        
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
        
class BinaryGate(LogicGate):
    def __init__(self,n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate" + self.getLabel() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()
    
    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate" + self.getLabel() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()
    
    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA =source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")
    

class UnaryGate(LogicGate):
    def __init__(self,n):
        super().__init__(n)
        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate" + self.getLabel() + "-->"))
        else:
            return self.pin.getFrom().getOutput()


    def setNextPin(self,source):
        if self.pin == None:
            self.pin =source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

