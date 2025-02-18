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

reservation_dict = {
    "ticket_holder": "John Smith",
    "airport_from": "LHR",
    "airport_to": "OSL",
    "flight_datetime": datetime(2026, 10, 13, 14, 35),
    "ticket_cost": 250,
    "ticket_type": "ECONOMY",
    "cancellable": False
}
reservation1 = FlightReservation.model_validate(reservation_dict)

reservation_json = """{
    "ticket_holder": "John Smith",
    "airport_from": "LHR",
    "airport_to": "OSL",
    "flight_datetime": "2026-10-13T14:35",
    "ticket_cost": 250,
    "ticket_type": "ECONOMY",
    "cancellable": false}
    """
reservation2 = FlightReservation.model_validate_json(reservation_json)