#! python

import asyncio
import contextlib
import logging
import sys

import aioeufyclean


async def main() -> None:
    if not (discovery := await aioeufyclean.find(sys.argv[1])):
        print("Device id not found")  # noqa: T201
        return

    print(discovery)  # noqa: T201


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())
