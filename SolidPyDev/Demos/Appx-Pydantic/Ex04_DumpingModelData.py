from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel

class TicketType(Enum):
    ECONOMY = "ECONOMY"
    BUSINESS = "BUSINESS"
    FIRST = "FIRST"

class FlightReservation(BaseModel):
    unique_id: UUID = uuid4() 
    ticket_holder: str
    airport_from: str
    airport_to: str
    flight_datetime: datetime
    ticket_cost: float
    ticket_type: TicketType
    cancellable: bool


reservation = FlightReservation(
    ticket_holder="John Smith",
    airport_from="LHR",
    airport_to="OSL",
    flight_datetime=datetime(2026, 10, 13, 14, 35),
    ticket_cost=250,
    ticket_type="ECONOMY",
    cancellable=False
)


reservation_as_dict = reservation.model_dump()
print("\nReservation as Python dict:")
print(reservation_as_dict)

reservation_as_json = reservation.model_dump_json()
print("\nReservation as JSON:")
print(reservation_as_json)

reservation_as_json_schema = reservation.model_json_schema()
print("\nReservation as JSON schema:")
print(reservation_as_json_schema)