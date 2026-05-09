import json

from app.queues.redis_client import redis_client

QUEUE_NAME = "ticket_events"

async def publish_events(event_data: dict):

    await redis_client.rpush(
        QUEUE_NAME,
        json.dumps(event_data)
    )

