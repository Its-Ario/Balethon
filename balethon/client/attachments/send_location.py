from ...objects import Message


class SendLocation:

    async def send_location(self, chat_id, latitude, longitude, reply_to_message_id=None):
        json = {"chat_id": chat_id, "latitude": latitude, "longitude": longitude, "reply_to_message_id": reply_to_message_id}
        result = await self.connection.execute("post", "sendLocation", json)
        return Message.wrap(result)
