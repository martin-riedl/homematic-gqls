#!/usr/bin/python3

from ariadne import QueryType
import homematicip
from homematicip.home import Home
from homematicip.device import ShutterContact, TemperatureHumiditySensorDisplay
from apscheduler.schedulers.background import BackgroundScheduler

# load homematic config
config = homematicip.find_and_load_config_file()

# authenticate and init connection
home = Home()
home.set_auth_token(config.auth_token)
home.init(config.access_point)

# do a first initial request
home.get_current_state()

# schedule a task at a given interval to update status
sched = BackgroundScheduler(daemon=True)
sched.add_job(lambda : home.get_current_state(),'interval',seconds=600)
sched.start()


# RESOLVERS

query = QueryType()

@query.field("shuttercontacts")
def resolve_ShutterContact(_, info):
    return [d for d in home.devices if isinstance(d, ShutterContact)]

@query.field("shuttercontacts_filtered")
def resolve_ShutterContact_Filtered(*_, label_filter=""):
    return [d for d in home.devices if isinstance(d, ShutterContact) if label_filter in d.label ]

@query.field("ths_displays")
def resolve_TemperatureHumiditySensorDisplay(_, info):
    return [d for d in home.devices if isinstance(d, TemperatureHumiditySensorDisplay)]

@query.field("ths_displays_filtered")
def resolve_TemperatureHumiditySensorDisplay(*_, label_filter=""):
    return [d for d in home.devices if isinstance(d, TemperatureHumiditySensorDisplay) if label_filter in d.label ]


