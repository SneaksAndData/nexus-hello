import asyncio

from nexus_client_sdk.nexus.core.app_core import Nexus
from nexus_client_sdk.nexus.input.command_line import NexusDefaultArguments

from nexus_hello.models.payload import HelloData


def logger_tags_from_payload(
    payload: HelloData, _: NexusDefaultArguments
) -> dict[str, str]:
    """
    Extracts tags from payload used for logger
    """
    return {
        "author": payload.hello_author,
    }


def metric_tags_from_payload(
    payload: HelloData, run_args: NexusDefaultArguments
) -> dict[str, str]:
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
        .inject_payload(HelloData)
        .with_log_enricher(
            tagger=logger_tags_from_payload, enricher=enrich_logger_from_payload
        )
        .with_metric_tagger(tagger=metric_tags_from_payload)
    )

    await nexus.activate()


if __name__ == "__main__":
    asyncio.run(main())
