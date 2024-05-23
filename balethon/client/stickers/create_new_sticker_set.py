from typing import Union

import balethon


class CreateNewStickerSet:

    async def create_new_sticker_set(
            self: "balethon.Client",
            user_id: Union[int, str],
            name: str,
            title: str,
            sticker=None
    ) -> bool:
        user_id = await self.resolve_peer_id(user_id)
        data = locals()
        del data["self"]
        return await self.execute("post", "createNewStickerSet", **data)
