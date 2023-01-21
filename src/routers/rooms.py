from fastapi import APIRouter

from src.operations.rooms import read_all_rooms, read_room

from src.db.db_interface import DBInterface
from src.db.models import DBRoom

router = APIRouter()


@router.get("/rooms")
def api_read_all_rooms():
    room_interface = DBInterface(DBRoom)
    return read_all_rooms(room_interface)


@router.get("/room/{room_id}")
def api_read_room(room_id: int):
    return read_room(room_id, room_interface=DBInterface(DBRoom))
