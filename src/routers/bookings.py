from fastapi import APIRouter
from src.db.models import DBBooking, DBRoom
from src.db.db_interface import DBInterface

from src.operations.bookings import (
    BookingCreateData,
    create_booking,
    delete_booking,
    read_all_bookings,
    read_booking,
)

router = APIRouter()


@router.get("/bookings")
def api_read_all_bookings():
    booking_interface = DBInterface(DBBooking)
    return read_all_bookings(booking_interface)


@router.get("/booking/{booking_id}")
def api_read_booking(booking_id: int):
    booking_interface = DBInterface(DBBooking)
    return read_booking(booking_id, booking_interface)


@router.post("/booking")
def api_add_booking(new_booking: BookingCreateData):
    booking_interface = DBInterface(DBBooking)
    room_interface = DBInterface(DBRoom)
    return create_booking(new_booking, booking_interface, room_interface)


@router.delete("/booking/{booking_id}")
def api_delete_booking(booking_id: int):
    booking_interface = DBInterface(DBBooking)
    return delete_booking(booking_id, booking_interface)
