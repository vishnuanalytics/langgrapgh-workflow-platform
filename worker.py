import asyncio
import json

from app.ai.graph import graph
from app.queues.redis_client import redis_client


QUEUE_NAME = "ticket_events"

async def worker():

    print("worker started")

    while True:
        _,event = await redis_client.blpop(QUEUE_NAME)
        data = json.loads(event)
        print("Processing event:")

        result = graph.invoke({
            "message": data["message"],
            "customer_email": data.get("customer_email", "unknown@test.com")
        })
        print("GRAPH RESULT:")
        print(result)

        await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(worker())