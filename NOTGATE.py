from LogicGate_CLASS import UnaryGate   
from Connector import Connector
from ANDGATE import AndGate
from ORGATE import OrGate


class NotGate(UnaryGate):
    def __init__(self,n):
        super().__init__(n)

    def performGateLogic(self):
        pin = self.getPin()
        if pin ==1:
            return 0
        else: 
            return 1


g1 =AndGate("G1")
g2 =AndGate("G2")
g3 =OrGate("G3")
g4 =NotGate("G4")
c1 = Connector(g1,g3)
c2 = Connector(g2,g3)
c3 = Connector(g3,g4)
print(g4.getOutput())