'''
SRP - Single responsibility principle
 
Generic code:

class Report:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        return f"Report Data: {self.data}"

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(self.generate_report())

'''
# using SRP now

class Report:
    def __init__(self, data):
        self.data=data

    def generate_report(self):
        return self.data

class SaveReport:
    @staticmethod
    def save_report_to_file(report:Report, filename):
        with open(filename,"w") as file:
            file.write(report.generate_report())
        print(f"file written successfully")

def main():
    report=Report("test data")
    generated_report=report.generate_report()
    print(f"Generated report is {generated_report}")

    save_report=SaveReport()
    save_report.save_report_to_file(report,"abhi.txt")

if __name__=='__main__':
    main()

