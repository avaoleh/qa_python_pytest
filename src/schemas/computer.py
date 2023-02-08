from pydantic import BaseModel, EmailStr, validator
from pydantic.types import PastDate, FutureDate, List, PaymentCardNumber
from pydantic.networks import IPv4Address, IPv6Address

from src.schemas.physical import Physical

"""
Именно в этом файле можно поиграться с уже готовой моделью и примером
тестового объекта для неё (Human).
That file gives to you possibility to play with ready to use model (Human).
"""

from src.enums.user_enums import Statuses


class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]


class Computer(BaseModel):
    id: int
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo