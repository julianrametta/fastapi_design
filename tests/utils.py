from src.operations.interface import DataObject


class DataInterfaceStub:
    def read_by_id(self, id: int) -> DataObject:
        raise NotImplementedError

    def read_all(self) -> list[DataObject]:
        raise NotImplementedError

    def create(self, data: DataObject) -> DataObject:
        raise NotImplementedError

    def update(self, id: int, data: DataObject) -> DataObject:
        raise NotImplementedError

    def delete(self, id: int) -> DataObject:
        raise NotImplementedError


class RoomInterface(DataInterfaceStub):
    def read_by_id(self, id: int) -> DataObject:
        return {"id": id, "number": "101", "size": 10, "price": 150_00}


class BookingInterface(DataInterfaceStub):
    def create(self, data: DataObject) -> DataObject:
        booking = dict(data)
        booking["id"] = 1
        return booking
