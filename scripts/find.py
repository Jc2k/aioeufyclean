#! python

import asyncio
import contextlib
import logging

import aioeufyclean


async def main() -> None:
    async with contextlib.aclosing(aioeufyclean.discover()) as discoveries:
        async for discovery in discoveries:
            print(discovery)  # noqa: T201


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())
