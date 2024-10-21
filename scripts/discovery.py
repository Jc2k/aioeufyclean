import asyncio
import contextlib
import logging

from aioeufyclean import discover


async def main() -> None:
    async for discovery in discover():
        print(discovery)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())
