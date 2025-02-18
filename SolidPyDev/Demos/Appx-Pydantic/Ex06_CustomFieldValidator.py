from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, Field, field_validator

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

    @field_validator("flight_datetime")
    @classmethod
    def check_flight_not_in_past(cls, flight_datetime: datetime) -> datetime:
        if flight_datetime < datetime.now():
            raise ValueError("Flight is in the past dude")
        return datetime
    
reservation_good = FlightReservation(
    ticket_holder="John Smith",
    airport_from="LHR",
    airport_to="OSL",
    when=datetime(2026, 10, 13, 14, 35),
    ticket_cost=250,
    ticket_type="ECONOMY",
    cancellable=False
)

reservation_bad = FlightReservation(
    ticket_holder="John Smith",
    airport_from="LHR",
    airport_to="OSL",
    when=datetime(2011, 12, 3, 7, 0),
    ticket_cost=250,
    ticket_type="ECONOMY",
    cancellable=False
)