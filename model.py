#!/usr/bin/python3

from ariadne import QueryType
import homematicip
from homematicip.home import Home
from homematicip.device import Device, ShutterContact, TemperatureHumiditySensorDisplay
from typing import List

# load homematic config
config = homematicip.find_and_load_config_file()

# authenticate and init connection
home = Home()
home.set_auth_token(config.auth_token)
home.init(config.access_point)

# do a first initial request
home.get_current_state()

# does the updating automatically
home.enable_events()

# RESOLVERS

query = QueryType()

@query.field("genericdevices")
def resolve_Device(_, info) -> List[Device]:
    return [d for d in home.devices]

@query.field("shuttercontacts") 
def resolve_ShutterContact(_, info) -> List[ShutterContact]:
    return [d for d in home.devices if isinstance(d, ShutterContact)]

@query.field("shuttercontacts_filtered")
def resolve_ShutterContact_Filtered(*_, label_filter="") -> List[ShutterContact]:
    return [d for d in home.devices if isinstance(d, ShutterContact) if label_filter in d.label ]

@query.field("ths_displays")
def resolve_TemperatureHumiditySensorDisplay(_, info) -> List[TemperatureHumiditySensorDisplay]:
    return [d for d in home.devices if isinstance(d, TemperatureHumiditySensorDisplay)]

@query.field("ths_displays_filtered")
def resolve_TemperatureHumiditySensorDisplay(*_, label_filter="") -> List[TemperatureHumiditySensorDisplay]:
    return [d for d in home.devices if isinstance(d, TemperatureHumiditySensorDisplay) if label_filter in d.label ]


