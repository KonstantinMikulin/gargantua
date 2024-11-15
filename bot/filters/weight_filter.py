from aiogram.filters import BaseFilter
from aiogram.types import Message


class WeightIsFloat(BaseFilter):
    async def __call__(self, event: Message):
        try:
            msg_text = event.text.replace(",", ".")  # type:ignore
            float(msg_text)
        except ValueError:
            return False
        else:
            return True
