class Printer:
    def print_document(self):
        print("Printing document")


class Scanner:
    def scan_document(self):
        print("Scanning document")


class MultifunctionDevice(Printer, Scanner):
    def display(self):
        self.print_document()
        self.scan_document()


m = MultifunctionDevice()
m.display()