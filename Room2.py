class Room:
    def __init__(self, room_number=0, price_per_night=50, is_occupied=False):
        self.room_number = room_number
        self.price_per_night = price_per_night
        self.is_occupied = is_occupied

    def occupy(self):
        # Mark room as occupied
        self.is_occupied = True

    def available(self):
        # Mark room as available
        self.is_occupied = False

