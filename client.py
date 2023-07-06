from aiohttp import ClientSession


class Client:

    def __init__(self, token):
        self.token = token
        self.session = None

    @property
    def url(self):
        return f"https://tapi.bale.ai/bot{self.token}"

    async def connect(self):
        self.session = ClientSession()

    async def disconnect(self):
        self.session.close()
        self.session = None

    # messages
    async def send_message(self, chat_id, text, reply_markup=None, reply_to_message_id=None):
        json = {"chat_id": chat_id, "text": text, "reply_markup": reply_markup, "reply_to_message_id": reply_to_message_id}
        async with self.session.post(f"{self.url}/sendMessage", json=json) as response:
            return await response.json()

    # messages
    async def edit_message_text(self, chat_id, message_id, text):
        json = {"chat_id": chat_id, "message_id": message_id, "text": text}
        async with self.session.post(f"{self.url}/editMessageText", json=json) as response:
            return await response.json()

    # messages
    async def delete_message(self, chat_id, message_id):
        json = {"chat_id": chat_id, "message_id": message_id}
        async with self.session.get(f"{self.url}/deleteMessage", json=json) as response:
            return await response.json()

    # updates
    async def get_updates(self, offset=0, limit=0):
        json = {"offset": offset, "limit": limit}
        async with self.session.post(f"{self.url}/getUpdates", json=json) as response:
            return await response.json()

    # updates
    async def set_webhook(self, url):
        json = {"url": url}
        async with self.session.post(f"{self.url}/setWebhook", json=json) as response:
            return await response.json()

    # updates
    async def delete_webhook(self):
        async with self.session.get(f"{self.url}/deleteWebhook") as response:
            return await response.json()

    # users
    async def get_me(self):
        async with self.session.get(f"{self.url}/getMe") as response:
            return await response.json()

    # attachments
    async def send_photo(self, chat_id, photo, caption=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "photo": photo, "caption": caption, "reply_to_message_id": reply_to_message_id}
        async with self.session.get(f"{self.url}/sendPhoto", json=json) as response:
            return await response.json()

    # attachments
    async def send_audio(self, chat_id, audio, caption=0, duration=0, title=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "audio": audio, "caption": caption, "duration": duration, "title": title, "reply_to_message_id": reply_to_message_id}
        async with self.session.get(f"{self.url}/sendAudio", json=json) as response:
            return await response.json()

    # attachments
    async def send_document(self, chat_id, document, caption=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "document": document, "caption": caption, "reply_to_message_id": reply_to_message_id}
        async with self.session.get(f"{self.url}/sendDocument", json=json) as response:
            return await response.json()

    # attachments
    async def send_video(self, chat_id, video, duration=0, width=0, height=0, caption=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "video": video, "duration": duration, "width": width, "height": height, "caption": caption, "reply_to_message_id": reply_to_message_id}
        async with self.session.get(f"{self.url}/sendVideo", json=json) as response:
            return await response.json()

    # attachments
    async def send_voice(self, chat_id, voice, caption=0, duration=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "voice": voice, "caption": caption, "duration": duration, "reply_to_message_id": reply_to_message_id}
        async with self.session.get(f"{self.url}/sendVoice", json=json) as response:
            return await response.json()

    # attachments
    async def send_location(self, chat_id, latitude, longitude, reply_to_message_id=0):
        json = {"chat_id": chat_id, "latitude": latitude, "longitude": longitude, "reply_to_message_id": reply_to_message_id}
        async with self.session.get(f"{self.url}/sendLocation", json=json) as response:
            return await response.json()

    # attachments
    async def send_contact(self, chat_id, phone_number, first_name, last_name=0, reply_to_message_id=0):
        json = {"chat_id": chat_id, "phone_number": phone_number, "first_name": first_name, "last_name": last_name, "reply_to_message_id": reply_to_message_id}
        async with self.session.get(f"{self.url}/sendContact", json=json) as response:
            return await response.json()

    # attachments
    async def get_file(self, file_id):
        json = {"file_id": file_id}
        async with self.session.get(f"{self.url}/getFile", json=json) as response:
            return await response.json()

    # chats
    async def get_chat(self, chat_id):
        json = {"chat_id": chat_id}
        async with self.session.get(f"{self.url}/getChat", json=json) as response:
            return await response.json()

    # chats
    async def get_chat_administrators(self, chat_id):
        json = {"chat_id": chat_id}
        async with self.session.get(f"{self.url}/getChatAdministrators", json=json) as response:
            return await response.json()

    # chats
    async def get_chat_members_count(self, chat_id):
        json = {"chat_id": chat_id}
        async with self.session.get(f"{self.url}/getChatMembersCount", json=json) as response:
            return await response.json()

    # chats
    async def get_chat_member(self, chat_id, user_id):
        json = {"chat_id": chat_id, "user_id": user_id}
        async with self.session.get(f"{self.url}/getChatMember", json=json) as response:
            return await response.json()

    # payments
    async def send_invoice(self, chat_id, title, description, provider_token, prices):
        json = {"chat_id": chat_id, "title": title, "description": description, "provider_token": provider_token, "prices": prices}
        async with self.session.get(f"{self.url}/sendInvoice", json=json) as response:
            return await response.json()
