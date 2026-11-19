
from bus_booking import BusReservation


def test_book_seat():
    bus = BusReservation(5)
    assert bus.book_seat(1) == "Seat booked successfully"


def test_book_same_seat():
    bus = BusReservation(5)
    bus.book_seat(1)
    assert bus.book_seat(1) == "Seat already booked"


def test_invalid_seat():
    bus = BusReservation(5)
    assert bus.book_seat(6) == "Invalid seat number"


def test_cancel_seat():
    bus = BusReservation(5)
    bus.book_seat(1)
    assert bus.cancel_seat(1) == "Booking cancelled successfully"


def test_available_seats():
    bus = BusReservation(5)
    bus.book_seat(1)
    bus.book_seat(2)
    assert bus.available_seats() == 3
