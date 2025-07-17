import asyncio

from nexus_.nexus.core.app_core import Nexus
from nexus_client_sdk.nexus.input.command_line import NexusDefaultArguments

from nexus_hello.models.payload import HelloData


def logger_tags_from_payload(payload: HelloData, _: NexusDefaultArguments) -> dict[str, str]:
    """
    Extracts tags from payload used for logger
    """
    return {
        "author": payload.hello_author,
    }


def metric_tags_from_payload(payload: HelloData, run_args: NexusDefaultArguments) -> dict[str, str]:
    """
    Extracts tags from payload used for metrics
    """
    return {
        "author": payload.hello_author,
        "request_id": run_args.request_id,
        "algorithm_name": "nexus_hello",
    }


def enrich_logger_from_payload(
    _: HelloData, run_args: NexusDefaultArguments
) -> dict[str, dict[str, str]]:
    """
    Extracts tags from payload used for logging
    """
    return {
        "(request_id:{request_id})": {"request_id": run_args.request_id},
    }


async def main():
    """
    Main function to run the Omni Channel Nexus Solver
    """
    nexus = (
        Nexus.create()
        # .with_module(AstraClientModule)
        # .add_reader(SkuReader)
        # .add_reader(CustomerLocationReader)
        # .add_reader(StoresDcsReader)
        # .add_reader(LocationReader)
        # .add_reader(OnlineOrderDetailsReader)
        # .add_reader(PriceReader)
        # .add_reader(SkuLocationPriceReader)
        # .add_reader(CurrencyReader)
        # .add_reader(ExchangeRateReader)
        # .add_reader(OnlineOrderDetailsEnhancedReader)
        # .add_reader(DemandReader)
        # .add_reader(ParameterReader)
        # .add_reader(OrderUpToLevelsReader)
        # .add_reader(ShippingReader)
        # .add_reader(DeliveryNodeReader)
        # .add_reader(CityReader)
        # .add_reader(IterationInventorySnapshotReader)
        # .use_processor(BasketInfoProcessor)
        # .use_processor(BasketProcessor)
        # .use_processor(DemandProtectionTimeProcessor)
        # .use_processor(DemandEndOfSeasonProcessor)
        # .use_processor(DemandHorizonProcessor)
        # .use_processor(EdgeProcessor)
        # .use_processor(FixedPathProcessor)
        # .use_processor(NodeProcessor)
        # .use_processor(UpdateDemandHorizonProcessor)
        # .use_processor(UpdateProtectionTimeDemandProcessor)
        # .use_processor(NodeSkuProcessor)
        # .use_processor(SkuProcessor)
        # .use_processor(CoordinateProcessor)
        # .use_algorithm(OmniChannelSolver)
        # .on_complete(
        #     AggregatedSolutionTelemetry,
        #     LocationSolutionTelemetry,
        #     SkuLocationSolutionTelemetry,
        #     LineNumberSolutionTelemetry,
        #     BasketInfoOutputTelemetry,
        #     EdgeOutputTelemetry,
        #     EdgeLineOutputTelemetry,
        #     EdgeSkuOutputTelemetry,
        #     FixedPathOutputTelemetry,
        #     LineBasketOutputTelemetry,
        #     NodeOutputTelemetry,
        #     NodeExceededLineNumberOutputTelemetry,
        #     NodeExceededOrderOutputTelemetry,
        #     NodeLineOutputTelemetry,
        #     NodeSkuOutputTelemetry,
        #     EndOfSeasonOutputTelemetry,
        #     ProtectionTimeOutputTelemetry,
        #     SolutionOutputTelemetry,
        #     InventorySnapshotTelemetry,
        # )
        # .inject_configuration(SolverConfigCollection)
        .inject_payload(HelloData)
        .with_log_enricher(tagger=logger_tags_from_payload, enricher=enrich_logger_from_payload)
        .with_metric_tagger(tagger=metric_tags_from_payload)
    )

    await nexus.activate()


if __name__ == "__main__":
    asyncio.run(main())
