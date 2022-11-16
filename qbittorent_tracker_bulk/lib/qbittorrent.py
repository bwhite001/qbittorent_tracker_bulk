#!/usr/bin/python3

from qbittorrentapi import Client


class qBittorrentClient:
    ########## CONFIGURATIONS ##########
    # Access Information for qBittorrent
    client = None

    def __init__(self, host):
        self.params = host
        self.client = Client(**host)

    def addAllTrackers(self, trackersArray):
        torrents = self.client.torrents.info()
        for t in torrents:
            print(t['name'])
            for url in trackersArray:
                print(t['name'] + " - " + url)
                self.client.torrents_add_trackers(t['hash'], url)

    def removeByFilter(self, filter='completed'):
        data = self.client.torrents.info(filter=filter)
        print("Found " + str(len(data)) + " torrents with filter " + filter)

        if len(data) == 0:
            print('No completed torrents to clear')
            return
        for tor in data:
            print(tor['name'] + " " + tor['state'])
            stateRemove = ['missingFiles', 'error']
            if tor['state'] == 'queuedDL' or tor['state'] == 'stalledDL' or tor[
                'state'] == 'forcedDL':
                continue
            if tor['state'] in stateRemove:
                print('Clearing ' + tor['state'] + ' torrent: ' + tor['name'])
                self.client.torrents_delete(
                    delete_files=True, torrent_hashes=tor['hash'])

    def manageTorrents(self, trackersArray, md5):
        data = self.client.torrents.info()
        for t in data:
            if t['completion_on'] != 0 and t['state'] != "pausedUP":
                self.client.torrents_pause(t['hash'])
                print("Paused Completed Torrent: " + t['name'])
                continue
            if t['state'] in ['queuedDL', 'stalledDL']:
                self.client.torrents.set_force_start(
                    torrent_hashes=t['hash'], value=True)
            else:
                self.addAllTrackers(trackersArray, md5)
                self.client.torrents_reannounce(torrent_hashes=t['hash'])
