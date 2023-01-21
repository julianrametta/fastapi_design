from src.operations.interface import DataInterface


def read_all_rooms(room_interface: DataInterface):
    return room_interface.read_all()


def read_room(room_id: int, room_interface: DataInterface):
    return room_interface.read_by_id(room_id)
