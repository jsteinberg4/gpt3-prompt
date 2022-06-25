import logging
from typing import Dict, Optional, Union

import openai


class ChatBot:
    """ A wrapper around the OpenAI GPT-3 API to speak with users 
    """
    LOGGER = logging.getLogger(__name__)

    def __init__(self,
                 secret_key: str,
                 query_params: Optional[Dict[str, Union[str, float, int]]] = None):
        """
        Creates a chatbot with the OpenAI API.

        :param secret_key: OpenAI API secret key
        :param query_params: default query parameters like temperature, max_tokens, etc.
        """
        ChatBot.LOGGER.info("Creating chatbot")
        self._key = secret_key
        self._default_params = query_params or dict(model='text-davinci-002',
                                                    temperature=0.7,
                                                    max_tokens=256,
                                                    top_p=1,
                                                    frequency_penalty=0,
                                                    presence_penalty=0)

    def prompt(self, prompt: str):
        openai.api_key = self._key
        self.LOGGER.info("Prompting GPT-3 with: %s" % prompt)
        return openai.Completion.create(prompt=prompt, **self._default_params)

