import datetime
class YearlyFinancialTracker:
    def __init__(self):
        self.records = []
        self.date_format = "%Y-%m-%d"
        self.filename = "financial_records.txt"
    def prompt_user(self):
        try:
            year = int(input("Enter the year: "))
            income = float(input(f"Enter monthly summary income for {year}: "))
            expenses = float(input(f"Enter monthly summary expenses for {year}: "))
            Total_Income = income * 12
            Total_Expenses = expenses * 12
            record = {
                "year": year,
                "income": Total_Income,
                "expenses": Total_Expenses
            }
            self.records.append(record)
            print("Yearly financial data recorded.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    def write_records_to_file(self):
        file = open(self.filename, "a")
        for record in self.records:
            file.write(f"{record['year']}, {record['income']}, {record['expenses']}\n")
        print(f"Records written to '{self.filename}' successfully.")
    def read_records_from_file(self):
        try:
            file = open(self.filename, "r")
            for line in file:
                parts = line.strip().split(",")
                year = parts[0]
                income = float(parts[1])
                expenses = float(parts[2])
                self.records.append({"year": year, "income": income, "expenses": expenses})

            print(f"Records loaded from '{self.filename}' successfully.")

        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
    def generate_report(self, filename):

        file = open(filename, "r")
        alldata = file.readlines()
        for line in alldata:
            parts = line.strip().split(",")
            year = parts[0]
            income = float(parts[1])
            expenses = float(parts[2])

            print(
                f"Year:{year} - Income: {income} - expenses: {expenses}")
