from skynetapi.requests.http_request import HTTPRequest


class DownloadRequest(HTTPRequest):
    def __init__(self, token: str):
        super().__init__(token)

    def get_png(self, **kwargs):
        """ Downloads the request PNG file. Optionally, saves the file
        to the provided `out_dir`.

        :param kwargs:
            - out_dir: The directory to save the PNG file.
            - See https://astrodyl.gitbook.io/astrodyl-docs/skynet-docs/api-endpoints/download
        """
        return self.download('png', kwargs.pop('out_dir', None), **kwargs)

    def get_jpg(self, **kwargs):
        """ Downloads the request PNG file. Optionally, saves the file
        to the provided `out_dir`.

        :param kwargs:
            - out_dir: The directory to save the JPG file.
            - See https://astrodyl.gitbook.io/astrodyl-docs/skynet-docs/api-endpoints/download
        """
        return self.download('jpg', kwargs.pop('out_dir', None), **kwargs)

    def get_fits(self, **kwargs):
        """ Downloads the request PNG file. Optionally, saves the file
        to the provided `out_dir`.

        :param kwargs:
            - out_dir: The directory to save the FITS file.
            - See https://astrodyl.gitbook.io/astrodyl-docs/skynet-docs/api-endpoints/download
        """
        return self.download('fits', kwargs.pop('out_dir', None), **kwargs)

    def get_header(self, **kwargs):
        """ Downloads the request PNG file. Optionally, saves the file
        to the provided `out_dir`.

        :param kwargs:
            - See https://astrodyl.gitbook.io/astrodyl-docs/skynet-docs/api-endpoints/download
        """
        return self.download('header', None, **kwargs)
