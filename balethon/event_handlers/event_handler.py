from typing import Callable
from inspect import iscoroutinefunction

from ..smart_call import remove_unwanted_parameters


class EventHandler:
    can_handle = object

    def __init__(self, callback: Callable, condition=None):
        self.callback = callback
        self.condition = condition

    async def __call__(self, client=None, event=None, /, *args, **kwargs):
        if client is not None:
            kwargs["client"] = client
        if event is not None:
            kwargs["event"] = event
        print([i for i in kwargs])
        args, kwargs = remove_unwanted_parameters(self.callback, *args, **kwargs)
        print([i for i in kwargs])
        if iscoroutinefunction(self.callback):
            return await self.callback(*args, **kwargs)
        return client.dispatcher.event_loop.run_in_executor(
            client.dispatcher.thread_pool_executor,
            self.callback,
            *args,
            **kwargs
        )

    async def check(self, client, event):
        if self.condition is None:
            return True
        return await self.condition(client, event)
