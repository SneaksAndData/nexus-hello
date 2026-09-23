from typing import final

from adapta.metrics import MetricsProvider
from injector import inject
from nexus_client_sdk.nexus.abstractions.algorithm_cache import InputCache
from nexus_client_sdk.nexus.abstractions.logger_factory import LoggerFactory
from nexus_client_sdk.nexus.abstractions.nexus_object import AlgorithmResult
from nexus_client_sdk.nexus.algorithms import MinimalisticAlgorithm

from nexus_hello.models.hello_config import HelloConfig
from nexus_hello.models.hello_result import HelloResult
from nexus_hello.models.payload import HelloData


@final
class HelloAlgorithm(MinimalisticAlgorithm[HelloData, HelloConfig]):
    """
    A greeting algorithm
    """

    @inject
    def __init__(
        self,
        config: HelloConfig,
        metrics_provider: MetricsProvider,
        logger_factory: LoggerFactory,
        payload: HelloData,
        cache: InputCache,
    ):
        super().__init__(metrics_provider, logger_factory, cache=cache, configuration=config)

        self._payload = payload

    async def _run(self, **kwargs) -> AlgorithmResult:
        return HelloResult(
            response_text=f"Hello to you, {self._payload.hello_author}! I am configured with {self._configuration.hello_str} and {self._configuration.hello_num} Guess what I have encoded for you :)",
            response_codes=list(b"Nexus is your true friend!"),
        )

    async def _context_open(self):
        pass

    async def _context_close(self):
        pass
