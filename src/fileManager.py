class FileManager:

    def __init__(self):
        self._file_url = None

    def change_file_url(self, file_url):
        self._file_url = file_url

    def get_file_url(self):
        return self._file_url
