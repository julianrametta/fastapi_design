from fastapi import APIRouter

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
    return read_all_bookings()


@router.get("/booking/{booking_id}")
def api_read_booking(booking_id: int):
    return read_booking(booking_id)


@router.post("/booking")
def api_add_booking(new_booking: BookingCreateData):
    return create_booking(new_booking)


@router.delete("/booking/{booking_id}")
def api_delete_booking(booking_id: int):
    return delete_booking(booking_id)
