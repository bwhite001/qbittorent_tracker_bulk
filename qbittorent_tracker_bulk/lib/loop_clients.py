#!/usr/bin/python3
import requests
import os
import hashlib
from qbittorent_tracker_bulk.lib.qbittorrent import qBittorrentClient


class LoopClients:
    connected = 0
    qbittorrents = []
    trackers = []
    len_trackers = 0
    test_host = None

    def __init__(self, trackers, hosts):
        self.trackers = trackers.trackers
        for host in hosts:
            self.test_host = qBittorrentClient(host)
            self.qbittorrents.append(self.test_host)
        self.connected = len(self.qbittorrents)
        self.len_trackers= len(self.trackers)

    def run(self, function, **kwargs):
        print(f"## RUNNING {function} on {self.connected} Clients")
        if(hasattr(self.test_host, function)):
            for client in self.qbittorrents:
                print(f"Connected to ${client}")
                getattr(client, function)(**kwargs)
        else:
            print(f"{function} is not in")
