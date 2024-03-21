"""Sector table and view."""


from sqlalchemy import String, select
from sqlalchemy.orm import Mapped, mapped_column

from hapi_schema.utils.base import Base
from hapi_schema.utils.view_params import ViewParams


class DBSector(Base):
    __tablename__ = "sector"

    code: Mapped[str] = mapped_column(String(32), primary_key=True)
    name: Mapped[str] = mapped_column(String(512), nullable=False, index=True)


view_params_sector = ViewParams(
    name="sector_view",
    metadata=Base.metadata,
    selectable=select(*DBSector.__table__.columns),
)
