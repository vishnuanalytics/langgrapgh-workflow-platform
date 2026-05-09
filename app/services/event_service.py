from sqlalchemy.ext.asyncio import AsyncSession

from app.models.event import Event
from app.schemas.ticket import TicketCreate


async def create_event(
    db: AsyncSession,
    ticket: TicketCreate
):

    event = Event(
        event_type="ticket.created",
        message=ticket.message,
        customer_email=ticket.customer_email
    )

    db.add(event)

    await db.commit()

    await db.refresh(event)

    return event