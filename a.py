from decimal import Decimal

from typing_extensions import Annotated

from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import registry

str_30 = Annotated[str, 30]
str_50 = Annotated[str, 50]
num_12_4 = Annotated[Decimal, 12]
num_6_2 = Annotated[Decimal, 6]


class Base(DeclarativeBase):
    registry = registry(
        type_annotation_map={
            str_30: String(30),
            str_50: String(50),
            num_12_4: Numeric(12, 4),
            num_6_2: Numeric(6, 2),
        }
    )


class SomeClass(Base):
    __tablename__ = "some_table"

    short_name: Mapped[str_30] = mapped_column(primary_key=True)
    long_name: Mapped[str_50]
    num_value: Mapped[num_12_4]
    short_num_value: Mapped[num_6_2]


from sqlalchemy.schema import CreateTable

print(CreateTable(SomeClass.__table__))
