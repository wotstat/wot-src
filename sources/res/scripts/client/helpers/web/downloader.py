class IDownloader(object):

    @property
    def stopped(self):
        raise NotImplementedError
        return

    def close(self):
        raise NotImplementedError
        return

    def downloadLowPriority(self, url, callback):
        raise NotImplementedError
        return

    def download(self, url, callback):
        raise NotImplementedError
        return
