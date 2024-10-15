"""
For obtaining a list of keys for controlling eufy devices.

This is only needed once, to get teh initial key.

See https://github.com/markbajaj/eufy-device-id-python/blob/main/eufy_local_id_grabber/crypto.py
"""

import json
from typing import Final
import aiohttp
import logging

_LOGGER = logging.getLogger(__name__)

EUFY_HEADERS: Final[dict[str, str]] = {
    "User-Agent": "EufyHome-Android-2.4.0",
    "timezone": "Europe/London",
    "category": "Home",
    "token": "",
    "uid": "",
    "openudid": "sdk_gphone64_arm64",
    "clientType": "2",
    "language": "en",
    "country": "US",
    "Accept-Encoding": "gzip",
}


async def get_eufy_vacuums(session: aiohttp.ClientSession, username: str, password: str):
    """Login to Eufy and get the vacuum details"""

    user_info_resp = await session.post(
        "https://home-api.eufylife.com/v1/user/email/login",
        headers=EUFY_HEADERS,
        json={
            "client_Secret": "GQCpr9dSp3uQpsOMgJ4xQ",
            "client_id": "eufyhome-app",
            "email": username,
            "password": password,
        },
    )

    if user_info_resp.status != 200:
        raise ApiFailed

    user_info = user_info_resp.json()

    if user_info["res_code"] != 1:
        raise AuthFailed

    id = user_info["user_info"]["id"]
    host = user_info["user_info"]["request_host"]
    access_token = user_info["access_token"]

    device_info_resp = await session.get(
        host + "/v1/device/list/devices-and-groups",
        headers={**EUFY_HEADERS, "token": access_token, "id": id},
    )
    device_info = device_info_resp.json()

    user_settings_resp = await session.get(
        host + "/v1/user/setting",
        headers={**EUFY_HEADERS, "token": access_token, "id": id},
    )
    user_settings = user_settings_resp.json()

    if (
        "tuya_home" in user_settings["setting"]["home_setting"]
        and "tuya_region_code" in user_settings["setting"]["home_setting"]["tuya_home"]
    ):
        region = user_settings["setting"]["home_setting"]["tuya_home"]["tuya_region_code"]
        if user_info["user_info"]["phone_code"]:
            country_code = user_info["user_info"]["phone_code"]
        else:
            country_code = get_phone_code_by_region(region)
    elif user_info["user_info"]["phone_code"]:
        region = get_region_by_phone_code(user_info["user_info"]["phone_code"])
        country_code = user_info["user_info"]["phone_code"]
    elif user_info["user_info"]["country"]:
        region = get_region_by_country_code(user_info["user_info"]["country"])
        country_code = get_phone_code_by_country_code(user_info["user_info"]["country"])
    else:
        region = "EU"
        country_code = "44"

    time_zone = user_info["user_info"]["timezone"]

    tuya_client = TuyaAPISession(
        username="eh-" + id,
        region=region,
        timezone=time_zone,
        phone_code=country_code,
    )

    vacs = {}
    for item in device_info["items"]:
        if item["device"]["product"]["appliance"] == "Cleaning":
            try:
                device = tuya_client.get_device(item["device"]["id"])

                vac_details = {
                    CONF_ID: item["device"]["id"],
                    CONF_MODEL: item["device"]["product"]["product_code"],
                    CONF_NAME: item["device"]["alias_name"],
                    CONF_DESCRIPTION: item["device"]["name"],
                    CONF_MAC: item["device"]["wifi"]["mac"],
                    CONF_IP_ADDRESS: "",
                    CONF_AUTODISCOVERY: True,
                    CONF_ACCESS_TOKEN: device["localKey"],
                }
                vacs[item["device"]["id"]] = vac_details
            except:
                _LOGGER.debug(
                    "Skipping vacuum {}: found on Eufy but not on Tuya. Eufy details:".format(
                        item["device"]["id"]
                    )
                )
                _LOGGER.debug(json.dumps(item["device"], indent=2))

    return vacs
