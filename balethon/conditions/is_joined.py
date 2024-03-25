from typing import Union

from .condition import Condition
from ..errors import RPCError


class IsJoined(Condition):

    def __init__(self, *chat_ids: Union[int, str]):
        super().__init__(chat_ids)
        self.chat_ids = chat_ids

    async def __call__(self, client, event) -> bool:
        for chat_id in self.chat_ids:
            try:
                chat_member = await client.get_chat_member(chat_id, event.author.id)
            except RPCError:
                return False
            else:
                if chat_member.status not in ("member", "administrator", "creator"):
                    return False
        return True
