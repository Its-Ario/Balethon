from . import Object
from balethon import objects


class Chat(Object):

    def __init__(
            self,
            id: int = None,
            type: str = None,
            title: str = None,
            username: str = None,
            first_name: str = None,
            last_name: str = None,
            all_members_are_administrators: bool = None,
            description: str = None,
            invite_link: str = None,
            pinned_message: "objects.Message" = None,
            sticker_set_name: str = None,
            can_set_sticker_set: bool = None,
            photo: "objects.ChatPhoto" = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: int = id
        self.type: str = type
        self.title: str = title
        self.username: str = username
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.all_members_are_administrators: bool = all_members_are_administrators
        self.description: str = description
        self.invite_link: str = invite_link
        self.pinned_message: "objects.Message" = pinned_message
        self.sticker_set_name: str = sticker_set_name
        self.can_set_sticker_set: bool = can_set_sticker_set
        self.photo: "objects.ChatPhoto" = photo

    def __str__(self):
        return f"[{self.full_name}](https://web.bale.ai/chat?uid={self.id})"

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        if self.first_name:
            return self.first_name
        if self.title:
            return self.title
        return ""

    async def ban_member(self, user_id):
        return await self.client.ban_chat_member(self.id, user_id)

    async def delete_photo(self):
        return await self.client.delete_chat_photo(self.id)

    async def get(self):
        return await self.client.get_chat(self.id)

    async def get_administrators(self):
        return await self.client.get_chat_administrators(self.id)

    async def get_member(self, user_id):
        return await self.client.get_chat_member(self.id, user_id)

    async def get_members_count(self):
        return await self.client.get_chat_members_count(self.id)

    async def invite_user(self, user_id):
        return await self.client.invite_user(self.id, user_id)

    async def leave(self):
        return await self.client.leave_chat(self.id)

    async def pin_message(self, message_id):
        return await self.client.pin_chat_message(self.id, message_id)

    async def promote_member(self, user_id, *args, **kwargs):
        return await self.client.promote_chat_member(self.id, user_id, *args, **kwargs)

    async def send_action(self, action="typing"):
        return await self.client.send_chat_action(self.id, action)

    async def set_description(self, description):
        return await self.client.set_chat_description(self.id, description)

    async def set_photo(self, photo):
        return await self.client.set_chat_photo(self.id, photo)

    async def set_title(self, title):
        return await self.client.set_chat_title(self.id, title)

    async def unban_member(self, user_id, only_if_banned=True):
        return await self.client.unban_chat_member(self.id, user_id, only_if_banned)

    async def unpin_message(self, message_id=None):
        return await self.client.unpin_chat_message(self.id, message_id)
