from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class Event(Base):
    
    __tablename__ = "events"
    id: Mapped[int] = mapped_column(primary_key=True)
    event_type: Mapped[str] = mapped_column(String)
    message: Mapped[str] = mapped_column(String)
    customer_email: Mapped[str] = mapped_column(String)
