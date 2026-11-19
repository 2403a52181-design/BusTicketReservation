
class BusReservation:

    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.booked_seats = set()

    def book_seat(self, seat_number):

        if seat_number < 1 or seat_number > self.total_seats:
            return "Invalid seat number"

        if seat_number in self.booked_seats:
            return "Seat already booked"

        self.booked_seats.add(seat_number)
        return "Seat booked successfully"

    def cancel_seat(self, seat_number):

        if seat_number in self.booked_seats:
            self.booked_seats.remove(seat_number)
            return "Booking cancelled successfully"

        return "Seat not booked"

    def available_seats(self):
        return self.total_seats - len(self.booked_seats)
