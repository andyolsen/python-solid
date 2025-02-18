from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, Field

class TicketType(Enum):
    ECONOMY = "ECONOMY"
    BUSINESS = "BUSINESS"
    FIRST = "FIRST"

class FlightReservation(BaseModel):
    unique_id: UUID = Field(default_factory=uuid4, frozen=True) 
    ticket_holder: str = Field(min_length=3)
    airport_from: str = Field(pattern=r"[A-Z]{3}")
    airport_to: str = Field(pattern=r"[A-Z]{3}")
    flight_datetime: datetime = Field(alias="when")
    ticket_cost: float = Field(gt=100)
    ticket_type: TicketType
    cancellable: bool


reservation_good = FlightReservation(
    ticket_holder="John Smith",
    airport_from="LHR",
    airport_to="OSL",
    when=datetime(2026, 10, 13, 14, 35),
    ticket_cost=250,
    ticket_type="ECONOMY",
    cancellable=False
)
# This statement would cause a validation error, because unique_id is marked as frozen.
# reservation_good.unique_id = "7eb02700-c3cf-41dd-ad9c-558dc0a59abe" 

reservation_bad = FlightReservation(
    ticket_holder="Jo",
    airport_from="Heathrow",
    airport_to="SF",
    whendude=datetime(2026, 10, 13, 14, 35),
    ticket_cost=29.99,
    ticket_type="CARGO CLASS",
    cancellable="Yep"
)