from src.operations.bookings import BookingCreateData, create_booking, InvalidDateError
from tests.utils import RoomInterface, BookingInterface
import pytest


def test_price_one_day():
    booking_data = BookingCreateData(
        room_id=1,
        customer_id=1,
        from_date="2021-12-24",
        to_date="2021-12-25",
        price=100,
    )
    booking = create_booking(
        data=booking_data,
        booking_interface=BookingInterface(),
        room_interface=RoomInterface(),
    )

    assert booking["price"] == 150_00


def test_date_error():
    booking_data = BookingCreateData(
        room_id=1,
        customer_id=1,
        from_date="2021-12-24",
        to_date="2021-12-24",
        price=100,
    )
    with pytest.raises(InvalidDateError):
        create_booking(
            data=booking_data,
            booking_interface=BookingInterface(),
            room_interface=RoomInterface(),
        )
