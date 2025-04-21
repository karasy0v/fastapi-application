from typing import Annotated
from datetime import datetime
from sqlalchemy import String, TIMESTAMP, func
from sqlalchemy.orm import mapped_column

str_not_nullable_and_uniq = Annotated[str, mapped_column(nullable=False, unique=True)]
str_not_nullable_an = Annotated[str, mapped_column(nullable=False)]
bool_not_nullable_and_default_false = Annotated[bool, mapped_column(nullable=False, server_default="false")]
str_nullable_an = Annotated[str | None, mapped_column(nullable=True)]

float_not_nullable_an = Annotated[float, mapped_column(nullable=False)]
float_nullable_an = Annotated[float | None, mapped_column(nullable=True)]

int_not_nullable_an = Annotated[int, mapped_column(nullable=False)]
int_nullable_an = Annotated[int | None, mapped_column(nullable=True)]

phone_number_an = Annotated[str, mapped_column(String(10), nullable=False)]

datetime_now_not_nullable_an = Annotated[
    datetime,
    mapped_column(TIMESTAMP, nullable=False, server_default=func.now()),
]
