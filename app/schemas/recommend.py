from pydantic import BaseModel

class EmojiInput(BaseModel):
    emojis: str
