from nexus_client_sdk.nexus.configurations.configuration_model import NexusConfigurationModel
from pydantic.dataclasses import dataclass


@dataclass
class HelloSettings:
    """
    Hello settings group
    """

    hello_str: str
    hello_num: int


class HelloConfig(NexusConfigurationModel):
    """
    Hello configuration.
    """

    hello_settings: HelloSettings
