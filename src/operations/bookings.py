from datetime import date

from pydantic import BaseModel

from src.db.engine import DBSession
from src.db.models import DBBooking, DBRoom, to_dict


class InvalidDateError(Exception):
    pass


class BookingCreateData(BaseModel):
    room_id: int
    customer_id: int
    from_date: date
    to_date: date
    price: int


def read_all_bookings():
    session = DBSession()
    bookings = session.query(DBBooking).all()
    return [to_dict(c) for c in bookings]


def read_booking(booking_id: int):
    session = DBSession()
    booking = session.query(DBBooking).get(booking_id)
    return to_dict(booking)


def create_booking(data: BookingCreateData):
    session = DBSession()
    room = session.query(DBRoom).get(data.room_id)

    days = (data.to_date - data.from_date).days

    if days <= 0:
        raise InvalidDateError("Invalid dates.")

    booking_dict = data.dict()
    booking_dict["price"] = days * room.price
    booking = DBBooking(**booking_dict)
    session.add(booking)
    session.commit()
    return to_dict(booking)


def delete_booking(booking_id: int):
    session = DBSession()
    booking = session.query(DBBooking).get(booking_id)
    session.delete(booking)
    session.commit()
    return to_dict(booking)
