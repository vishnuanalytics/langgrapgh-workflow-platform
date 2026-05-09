from pydantic import BaseModel

class TicketCreate(BaseModel):
    message: str
    customer_email: str

