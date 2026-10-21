class Connector:
    def __init__(self,fgate,tgate):
        self.formgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.formgate
    
    def getTo(self):
        return self.togate
    
def setNextPin(self,source):
    if self.pinA == None:
        self.pinA =source
    else:
        if self.pinB == None:
            self.pinB = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")