from fastapi import FastAPI, Depends

from contextlib import asynccontextmanager
from contextlib import asynccontextmanager

from app.db.init_db import init_db
from app.db.session import get_db
from app.schemas.ticket import TicketCreate
from app.services.event_service import create_event

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from app.queues.event_queue import publish_events



@asynccontextmanager
async def lifespan(app: FastAPI):

    await init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "AI Workflow Engine Running"}


@app.post("/webhook/ticket")
async def receive_ticket(
    ticket: TicketCreate,
    db: AsyncSession = Depends(get_db)
):

    event = await create_event(db, ticket)

    await publish_events({
        "event_id": event.id,
        "event_type" : event.event_type,
        "message": event.message,
        "customer_email": event.customer_email
    })

    return {
        "status": "saved",
        "event_id": event.id,
        "customer_email": event.customer_email
    }