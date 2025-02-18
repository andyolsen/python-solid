from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, Field, model_validator
from typing import Self

class TicketType(Enum):
    ECONOMY = "ECONOMY"
    BUSINESS = "BUSINESS"
    FIRST = "FIRST"
    TARDIS = "TARDIS"

class FlightReservation(BaseModel):
    unique_id: UUID = Field(default_factory=uuid4, frozen=True) 
    ticket_holder: str = Field(min_length=3)
    airport_from: str = Field(pattern=r"[A-Z]{3}")
    airport_to: str = Field(pattern=r"[A-Z]{3}")
    flight_datetime: datetime = Field(alias="when")
    ticket_cost: float = Field(gt=100)
    ticket_type: TicketType
    cancellable: bool

    @model_validator(mode="after")
    def check_flight_not_in_past_unless_using_tardis(self) -> Self:
        if self.flight_datetime < datetime.now() and \
           self.ticket_type != TicketType.TARDIS:
            raise ValueError("Flight is in past and not using a Tardis")
        return self
    
    
reservation_good_1 = FlightReservation(
    ticket_holder="John Smith",
    airport_from="LHR",
    airport_to="OSL",
    when=datetime(2026, 10, 13, 14, 35),
    ticket_cost=250,
    ticket_type="ECONOMY",
    cancellable=False
)

reservation_good_2 = FlightReservation(
    ticket_holder="John Smith",
    airport_from="LHR",
    airport_to="OSL",
    when=datetime(2011, 12, 25, 7, 0),
    ticket_cost=250,
    ticket_type="TARDIS",
    cancellable=False
)

reservation_bad = FlightReservation(
    ticket_holder="John Smith",
    airport_from="LHR",
    airport_to="OSL",
    when=datetime(2011, 12, 25, 7, 0),
    ticket_cost=250,
    ticket_type="ECONOMY",
    cancellable=False
)