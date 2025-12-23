class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.is_occupied = False
        self.guest_name = None

    def check_in(self, guest_name):
        if not self.is_occupied:
            self.is_occupied = True
            self.guest_name = guest_name
            return f"Room {self.room_number} booked for {guest_name}."
        else:
            return f"Room {self.room_number} is already occupied."

    def check_out(self):
        if self.is_occupied:
            guest = self.guest_name
            self.is_occupied = False
            self.guest_name = None
            return f"{guest} has checked out of Room {self.room_number}."
        else:
            return f"Room {self.room_number} is already free."
