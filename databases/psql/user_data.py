from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.dialects.postgresql import ARRAY


class Base(DeclarativeBase):
    pass

class UserProfile(Base):
    __tablename__ = "user_profile"

    id: Mapped[int]                  = mapped_column(primary_key=True)
    phone_number: Mapped[str]        = mapped_column(String(30))
    email: Mapped[str]               = mapped_column(String(100))
    address: Mapped[str]             = mapped_column(String(500))
    payment_cards: Mapped[list[int]] = mapped_column(ARRAY(Integer))