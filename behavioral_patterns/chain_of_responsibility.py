class ContentFilter(object):
    def __init__(self, filters=None):
        self._filters = list()
        if filters is not None:
            self._filters += filters

    def filter(self, content):
        for filter in self._filters:
            content = filter(content)
        return content


if __name__ == '__main__':
    filter = ContentFilter()
    filtered_content = filter.filter('some content.')
