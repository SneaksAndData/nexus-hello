from dataclasses import dataclass
from typing import final

from nexus_client_sdk.nexus.input.payload_reader import AlgorithmPayload


@final
@dataclass
class HelloData(AlgorithmPayload):
    """
    Configuration for saying hello
    """

    hello_text: str
    hello_author: str
