# Import required modules
import tkinter as tk
import datetime

# Define the Room class
class Room:
    def __init__(self, room_number=0, price_per_night=50, is_occupied=False):
        """
        Initialize a Room object.

        Args:
            room_number (int): The room number.
            price_per_night (float): The price per night for the room.
            is_occupied (bool): True if the room is occupied, False otherwise.
        """
        self.room_number = room_number
        self.price_per_night = price_per_night
        self.is_occupied = is_occupied

    def occupy(self):
        """
        Mark the room as occupied.
        """
        self.is_occupied = True

    def available(self):
        """
        Mark the room as available.
        """
        self.is_occupied = False

# Define the HotelGuests class
class HotelGuests:
    def __init__(self, date="1-1-2000", name="No Name", description="Check-In", amount=0.0):
        """
        Initialize a HotelGuests object.

        Args:
            date (str): The date of the guest's entry.
            name (str): The name of the guest.
            description (str): A description of the guest's entry (e.g., Check-In).
            amount (float): The amount of income associated with the guest's entry.
        """
        self.date = date
        self.name = name
        self.description = description
        self.amount = amount

    def load_records_from_file(self, filename):
        """
        Load guest records from a file.

        Args:
            filename (str): The name of the file to load records from.

        Returns:
            list: A list of loaded guest records.
        """
        records = []
        try:
            file = open(filename, "r")
            for line in file:
                parts = line.strip().split(",")
                date = parts[0]
                name = parts[1]
                description = parts[2]
                amount = float(parts[3])
                record = HotelGuests(date, name, description, amount)
                records.append(record)

        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        return records

    def save_records_to_file(self, records, filename):
        """
        Save guest records to a file.

        Args:
            records (list): A list of guest records to be saved.
            filename (str): The name of the file to save records to.
        """
        file = open(filename, "w")
        for record in records:
            file.write(f"{record.date}, {record.name}, {record.description}, {record.amount}\n")

    def generate_report(self, filename):
        """
        Generate and print a report of guest records.

        Args:
            filename (str): The name of the file containing guest records.
        """
        file = open(filename, "r")
        alldata = file.readlines()
        for line in alldata:
            parts = line.strip().split(",")
            date = parts[0]
            name = parts[1]
            description = parts[2]
            amount = float(parts[3])
            record = HotelGuests(date, name, description, amount)
            print(f"Date: {record.date} - Name: {record.name} - Description: {record.description} - Amount: {record.amount} JOD")

# Define the YearlyFinancialTracker class
class YearlyFinancialTracker:
    def __init__(self):
        """
        Initialize a YearlyFinancialTracker object.
        """
        self.records = []
        self.date_format = "%Y-%m-%d"
        self.filename = "financial_records.txt"

    def prompt_user(self):
        """
        Prompt the user to enter yearly income and expenses and calculate yearly totals.
        """
        try:
            year = int(input("Enter the year: "))
            income = float(input(f"Enter monthly summary income for {year}: "))
            expenses = float(input(f"Enter monthly summary expenses for {year}: "))
            total_income = income * 12
            total_expenses = expenses * 12
            record = {
                "year": year,
                "income": total_income,
                "expenses": total_expenses
            }
            self.records.append(record)
            print("Yearly financial data recorded.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def write_records_to_file(self):
        """
        Write yearly financial records to a file.
        """
        file = open(self.filename, "a")
        for record in self.records:
            file.write(f"{record['year']}, {record['income']}, {record['expenses']}\n")
        print(f"Records written to '{self.filename}' successfully.")

