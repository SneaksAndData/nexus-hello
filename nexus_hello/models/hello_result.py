from dataclasses import dataclass
from datetime import datetime
from typing import final, Any

import pandas
import polars

from nexus_client_sdk.nexus.abstractions.nexus_object import AlgorithmResult


@final
@dataclass
class HelloResult(AlgorithmResult):
    """
    Algorithm run result
    """

    response_text: str
    response_codes: list[int]

    def result(self) -> pandas.DataFrame | polars.DataFrame | dict:
        return {
            "hello_response": self.response_text,
            "hello_time": datetime.now().isoformat(),
            "hello_values": self.response_codes,
        }

    def to_kwargs(self) -> dict[str, Any]:
        pass
