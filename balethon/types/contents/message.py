from ..object import Object


class Message(Object):

    @classmethod
    def from_dict(cls, client, message_dict):
        if message_dict.get("from"):
            message_dict["from_user"] = message_dict.pop("from")
        message_dict["client"] = client
        return cls(**message_dict)

    def __init__(
            self,
            message_id=None,
            from_user=None,
            date=None,
            chat=None,
            forward_from=None,
            forward_from_chat=None,
            forward_from_message_id=None,
            forward_date=None,
            reply_to_message=None,
            edit_date=None,
            text=None,
            entities=None,
            caption_entities=None,
            audio=None,
            document=None,
            photo=None,
            video=None,
            voice=None,
            caption=None,
            contact=None,
            location=None,
            new_chat_members=None,
            left_chat_member=None,
            new_chat_title=None,
            new_chat_photo=None,
            delete_chat_photo=None,
            group_chat_created=None,
            supergroup_chat_created=None,
            channel_chat_created=None,
            pinned_message=None,
            invoice=None,
            successful_payment=None,
            client=None,
            **kwargs
    ):
        super().__init__(client)
        self.id = message_id
        self.from_user = from_user
        self.date = date
        self.chat = chat
        self.forward_from = forward_from
        self.forward_from_chat = forward_from_chat
        self.forward_from_message_id = forward_from_message_id
        self.forward_date = forward_date
        self.reply_to_message = reply_to_message
        self.edit_date = edit_date
        self.text = text
        self.entities = entities
        self.caption_entities = caption_entities
        self.audio = audio
        self.document = document
        self.photo = photo
        self.video = video
        self.voice = voice
        self.caption = caption
        self.contact = contact
        self.location = location
        self.new_chat_members = new_chat_members
        self.left_chat_member = left_chat_member
        self.new_chat_title = new_chat_title
        self.new_chat_photo = new_chat_photo
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created
        self.supergroup_chat_created = supergroup_chat_created
        self.channel_chat_created = channel_chat_created
        self.pinned_message = pinned_message
        self.invoice = invoice
        self.successful_payment = successful_payment

    async def reply(self, text, reply_markup=None, reply_to_message_id=None):
        if reply_to_message_id is None:
            reply_to_message_id = self.id
        await self.client.send_message(self.chat["id"], text, reply_markup, reply_to_message_id)

    async def edit_text(self, text, reply_markup=None):
        await self.client.edit_message_text(self.chat["id"], self.id, text, reply_markup)

    async def delete(self):
        await self.client.delete_message(self.chat["id"], self.id)
