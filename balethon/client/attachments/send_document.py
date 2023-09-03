from ...objects import Message


class SendDocument:

    async def send_document(self, chat_id, document, caption=None, reply_to_message_id=None):
        json = {"chat_id": chat_id, "document": document, "caption": caption, "reply_to_message_id": reply_to_message_id}
        result = await self.connection.execute("post", "sendDocument", json)
        return Message.wrap(result)
