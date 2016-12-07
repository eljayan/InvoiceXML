
class XMLInvoice:
    def __int__(self):
        self.number = 0
        self.subtotalVAT = 0
        self.subtotalNoVAT = 0
        self.VAT = 0
        self.items = []

    def export(self):
        '''returs a dictionary with the data to be sent to db'''
        return

class XMLItem:
    def __init__(self):
        self.honoraryCode = None
        self.databaseCode = None
        self.subtotal = 0
        self.total = 0

    def setDatabaseCode(self):
        return



