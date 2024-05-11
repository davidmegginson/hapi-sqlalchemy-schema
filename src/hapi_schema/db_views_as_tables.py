from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column

from hapi_schema.utils.base import Base


class DBAdmin1VAT(Base):
    __tablename__ = "admin1_vat"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    location_ref: Mapped[int] = mapped_column(Integer)
    code: Mapped[str] = mapped_column(String(128), index=True)
    name: Mapped[str] = mapped_column(String(512), index=True)
    is_unspecified: Mapped[bool] = mapped_column(Boolean)
    reference_period_start: Mapped[datetime] = mapped_column(
        DateTime, index=True
    )
    reference_period_end: Mapped[datetime] = mapped_column(
        DateTime, index=True
    )
    location_code: Mapped[str] = mapped_column(String(128), index=True)
    location_name: Mapped[str] = mapped_column(String(512), index=True)


class DBAdmin2VAT(Base):
    __tablename__ = "admin2_vat"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    admin1_ref: Mapped[int] = mapped_column(Integer)
    code: Mapped[str] = mapped_column(String(128), index=True)
    name: Mapped[str] = mapped_column(String(512), index=True)
    is_unspecified: Mapped[bool] = mapped_column(Boolean)
    reference_period_start: Mapped[datetime] = mapped_column(
        DateTime, nullable=True, index=True
    )
    reference_period_end: Mapped[datetime] = mapped_column(
        DateTime, nullable=True, index=True
    )
    admin1_code: Mapped[str] = mapped_column(String(128))
    admin1_name: Mapped[str] = mapped_column(String(512))
    admin1_is_unspecified: Mapped[bool] = mapped_column(Boolean)
    location_code: Mapped[str] = mapped_column(String(128), index=True)
    location_name: Mapped[str] = mapped_column(String(512), index=True)
