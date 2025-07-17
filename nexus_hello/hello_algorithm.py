from typing import final

from adapta.metrics import MetricsProvider
from injector import inject
from nexus_client_sdk.nexus.abstractions.algrorithm_cache import InputCache
from nexus_client_sdk.nexus.abstractions.logger_factory import LoggerFactory
from nexus_client_sdk.nexus.abstractions.nexus_object import AlgorithmResult
from nexus_client_sdk.nexus.algorithms import MinimalisticAlgorithm

from nexus_hello.models.hello_result import HelloResult
from nexus_hello.models.payload import HelloData


@final
class HelloAlgorithm(MinimalisticAlgorithm):

    @inject
    def __init__(self, metrics_provider: MetricsProvider, logger_factory: LoggerFactory, payload: HelloData, cache: InputCache):
        super().__init__(metrics_provider, logger_factory, cache=cache)

        self._payload = payload

    async def _run(self, **kwargs) -> AlgorithmResult:
        return HelloResult(
            response_text="",
            response_codes=[]
        )

    async def _context_open(self):
        pass

    async def _context_close(self):
        pass