from pydantic import BaseModel, Field, field_validator
import re

class Feedback(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    message: str = Field(min_length=5, max_length=200)

    @field_validator('message')
    @classmethod
    def check_bad_words(cls, v: str) -> str:
        bad_words = ['редиска', 'редиски', 'редиску', 'редиской', 'редиске',
                     'бяка', 'бяки', 'бяку', 'бякой', 'бяке',
                     'козявка', 'козявки', 'козявку', 'козявкой', 'козявке']
        
        message_lower = v.lower()
        for word in bad_words:
            if word in message_lower:
                raise ValueError('Использование недопустимых слов')
        
        return v