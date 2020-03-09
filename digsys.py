class LogicGate(object):
    def __init__(self, n):
        self.label = n
        self.output = None
    def __str__(self):
        return "Gate: label=%s output=%s" % \
               (self.label, self.output)
    def getLabel(self):
        return self.label
    def getOutput(self):
        self.output = self.performLogicGate()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None
    def getPinA(self):
        return int(input("Enter Pin A input for gate " +
                         self.getLabel() + '-->'))
    def getPinB(self):
        return int(input("Enter Pin B input for gate " +
                         self.getLabel() + '-->'))

class AndGate(BinaryGate):
    def __init__(self, n):
        super(AndGate, self).__init__(n)
    def performLogicGate(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, n):
        super(OrGate, self).__init__(n)
    def performLogicGate(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==0 and b==0:
            return 0
        else:
            return 1

class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None

    def getPin(self):
        return int(input("Enter Pin for gate " +
                         self.getLabel() + '-->'))

class NotGate(UnaryGate):
    def __init__(self):
        super(NotGate, self).__init__()

        def performLogicGate(self):
            if self.getPin() == 1:
                return 0
            else:
                return 1
