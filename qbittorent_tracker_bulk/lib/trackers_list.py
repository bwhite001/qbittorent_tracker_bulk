from urllib.request import urlopen


class TrackersList:
    trackers = []

    def __init__(self, target_url):
        text = urlopen(target_url).read()
        self.trackers = text.decode('utf-8').split('\n\n')

        assert len(self.trackers) > 0, f'Unable to find Trackers with given URL ${trackers}'
