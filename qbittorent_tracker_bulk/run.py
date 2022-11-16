#!/usr/bin/env python

"""Process open MRs and notify the team."""
import os
import sys
from urllib.parse import urlparse

import click
from dotenv import load_dotenv

from qbittorent_tracker_bulk.lib.loop_clients import LoopClients
from qbittorent_tracker_bulk.lib.trackers_list import TrackersList

load_dotenv()

HOSTS_STRING = os.environ.get("QTORRENT_URLS", "")
LIVE_TRACKERS_LIST_URL = os.environ.get(
    "TRACKER_URL",
    "https://cdn.staticaly.com/gh/XIU2/TrackersListCollection/master/best.txt",
)
assert (
    LIVE_TRACKERS_LIST_URL != ""
), "LIVE_TRACKERS_LIST_URL must be defined. and NOT EMPTY"


def parse_host(host_string):
    hosts = []
    for name in host_string.split(","):
        host = urlparse(name.strip())
        print(host)
        hosts.append(
            {
                "host": host.scheme + "://" + host.hostname,
                "port": host.port,
                "password": host.password,
                "username": host.username,
            }
        )

    assert (
        len(hosts) > 0
    ), "HOSTS_STRING urls seperated by ',' must be defined in the environment or .env file for eg http://admin:adminadmin@192.168.0.243:8080/"
    return hosts


@click.command()
@click.option("-h", "--hosts", default=None)
def cli(hosts=None):
    if hosts is None:
        hosts = HOSTS_STRING
    hosts_list = parse_host(hosts)
    trackers = TrackersList(LIVE_TRACKERS_LIST_URL)
    looper = LoopClients(trackers, hosts_list)
    looper.run("addAllTrackers", trackersArray=trackers.trackers)


if __name__ == "__main__":
    try:
        cli()
    except SystemExit:
        sys.exit(0)
