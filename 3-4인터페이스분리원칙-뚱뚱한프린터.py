from abc import ABC, abstractmethod

class IPrint(ABC):
    @abstractmethod
    def print_file(self, file:str) -> bool:
        pass

class IScan(ABC):
    @abstractmethod
    def scan(self, content:str) -> bool:
        pass


class SamsungPrinter(IPrint, IScan):
    def __init__(self, has_ink, has_paper, is_connected):
        self.has_ink= has_ink
        self.has_paper = has_paper
        self.is_connected = is_connected

    def print_file(self, file):
        if self.has_ink and self.has_paper and self.is_connected :
            print("Printing {}".format(file))
            return True

        return False

    def scan(self, content):
        if self.is_connected:
            print("Scanning {}".format(content))
            return True

        return  False

class LGPrinter(IPrint):
    def __init__(self, has_ink, has_paper, is_connected):
        self.has_ink =has_ink
        self.has_paper= has_paper
        self.is_connected = is_connected

    def print_file(self, file):
        if self.has_ink and self.has_paper and self.is_connected:
            print("Printing {}".format(file))
            return True

        return False

    # def scan(self, content):
    #     print("The printer has no scan function.")
    #     return False


samsung_printer = SamsungPrinter( True, True, True)
lg_printer =LGPrinter(True,True,True)

samsung_printer.print_file("Report1.docx")
lg_printer.print_file("Report2.docx")

samsung_printer.scan("scan test")
#lg_printer.scan("scan test")

print(SamsungPrinter.mro())
print(LGPrinter.mro())

