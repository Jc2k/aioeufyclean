#! python

import asyncio
import contextlib
import logging
import os

import aioeufyclean


def _availability_callback(availability: bool) -> None:
    print(f"availability: {availability}")  # noqa: T201


def _state_callback(state: aioeufyclean.VacuumState) -> None:
    print(f"state: {state}")  # noqa: T201


async def main():
    device_id = os.environ["DEVICE_ID"]
    ip_addresss = os.environ["IP_ADDRESS"]
    local_key = os.environ["LOCAL_KEY"]

    vd = aioeufyclean.VacuumDevice(device_id, ip_addresss, local_key)
    vd.async_add_availability_callback(_availability_callback)
    vd.async_add_state_callback(_state_callback)

    task = asyncio.create_task(vd.async_process_messages())

    # await vd.async_set_switch(aioeufyclean.Switch.BOOST_IQ, False)

    await task


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())
