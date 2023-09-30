from Room2 import *
from HotelGuests import *
from FinancialRecord2 import *
import tkinter as tk
# Room Information
def RoomsInfo():
    rooms = [Room(room_number) for room_number in range(1, 11)]
    while True:

        print("\nHotel Room Management")
        print("1. View All Rooms")
        print("2. Check-In")
        print("3. Check-Out")
        choice = input("Enter your choice: ")
        if choice == "1":
            c=1
            for room in rooms:
                if room.is_occupied:
                    status = "Occupied"
                elif not room.is_occupied:
                    status = "Available"
                print(f"Room {c} {status}")
                c+=1
        elif choice=="2":
            room_number = int(input("Enter room number: "))
            if room_number>=1 and room_number<= 10:
                room = rooms[room_number-1]
                if not room.is_occupied:
                    room.occupy()
                    print(f"Checked into Room {room_number}")
                else:
                    print(f"Room {room_number} is already occupied")

            else:
                print("Invalid room number. Please choose a valid room.")

        elif choice=="3":
            room_number = int(input("Enter room number: "))
            if room_number >= 1 and room_number <= 10:
                room = rooms[room_number - 1]
                if room.is_occupied:
                    room.available()
                    print(f"Checked out Room {room_number}")
                else:
                    print(f"Room {room_number} is already available")
            else:
                print("Invalid room number. Please choose a valid room ")

        else:
            print("Invalid choice. Please choose again")
# RoomsInfo()

# Guests Information
def GuestInfo():
    while True:
        print("Guests Information System:")
        print("1. Add A Guest")
        print("2. Generate All Guests Info")
        choice = input("Enter your choice: ")
        if choice == "1":
            date = input("Enter date (DD-MM-YYYY): ")
            name = input("Enter name of the guest: ")
            duration = input("Enter duration: ")
            amount = float(input("Enter income amount: "))
            hotel_guests = HotelGuests(date, name, duration, amount)
            records = hotel_guests.load_records_from_file("GuestsFile.txt")
            records.append(hotel_guests)
            hotel_guests.save_records_to_file(records, "GuestsFile.txt")
            print("Guest added")
        elif choice=="2":
            hotel_guests = HotelGuests()
            hotel_guests.generate_report("GuestsFile.txt")

        else:
            print("Invalid choice. Please choose again")

# GuestInfo()
# Financial Records
def FinancialTracker():
    tracker = YearlyFinancialTracker()
    while True:
        print("Yearly Financial Tracker")
        print("1. Enter Yearly profits and Expenses")
        print("2. Read Records from File")
        choice = input("Enter your choice:")
        if choice == "1":
            tracker.prompt_user()
            tracker.write_records_to_file()
        elif choice == "2":
            tracker.generate_report("financial_records.txt")

        else:
            print("Invalid choice. Please choose again")







def Start():
    print("Leen's Hotel Management")
    print("1. Hotel Room Management")
    print("2. Guests Information System")
    print("3. Yearly Financial Tracker")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice =="1":
        print("______________________________________________________________")
        RoomsInfo()
    elif choice=="2":
        print("______________________________________________________________")
        GuestInfo()
    elif choice=="3":
        print("______________________________________________________________")
        FinancialTracker()
    elif choice == "4":
        while True:
            print("Exiting....")
            break
    else:
        print("Invalid choice. Please choose again")

# GUI


root = tk.Tk()
root.title("Leen's Hotel Management")

room_management_button = tk.Button(root, text="Hotel Room Management", command=RoomsInfo)
guest_info_button = tk.Button(root, text="Guests Information System", command=GuestInfo)
financial_tracker_button = tk.Button(root, text="Yearly Financial Tracker", command=FinancialTracker)
exit_button = tk.Button(root, text="Exit", command=root.destroy)

room_management_button.pack()
guest_info_button.pack()
financial_tracker_button.pack()
exit_button.pack()

# Start the GUI main loop
root.mainloop()

