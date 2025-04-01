from sqlalchemy import Integer, String, Text, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass

class Units(Base):
    __tablename__ = "units"

    id: Mapped[int]   = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(10))

class Categories(Base):
    __tablename__ = "categories"

    id: Mapped[int]          = mapped_column(primary_key=True)
    name: Mapped[str]        = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)

class Goods(Base):
    __tablename__ = "goods"

    id: Mapped[int]          = mapped_column(primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    name: Mapped[str]        = mapped_column(String(100))
    quantity: Mapped[float]  = mapped_column(Float)
    unit_type: Mapped[int]   = mapped_column(ForeignKey("units.id"))
    price: Mapped[float]     = mapped_column(Float)
    description: Mapped[str] = mapped_column(Text)
    image_link: Mapped[str]  = mapped_column(Text)
