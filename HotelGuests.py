class HotelGuests:
    def __init__(self, date="1-1-2000", name="No Name", duration="One-Day", amount=0.0):
        self.date = date
        self.name = name
        self.duration = duration
        self.amount = amount

    def load_records_from_file(self, filename):

        records = []
        try:
            file = open(filename, "r")
            for line in file:
                parts = line.strip().split(",")
                date = parts[0]
                name = parts[1]
                duration = parts[2]
                amount = float(parts[3])
                record = HotelGuests(date, name, duration, amount)
                records.append(record)

        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        return records

    def save_records_to_file(self, records, filename):

        file = open(filename, "w")
        for record in records:
            file.write(f"{record.date}, {record.name}, {record.duration}, {record.amount}\n")
    def generate_report(self, filename):

        file = open(filename, "r")
        alldata = file.readlines()
        for line in alldata:
            parts = line.strip().split(",")
            date = parts[0]
            name = parts[1]
            duration = parts[2]
            amount = float(parts[3])
            record = HotelGuests(date, name,duration, amount)
            print(f"Date:{record.date} - Name: {record.name} - Duration: {record.duration} - Amount: {record.amount}JOD")