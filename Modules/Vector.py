class Vector:
    def __init__(self, transponder, path, wavelength):
        self.transponder = transponder
        self.path = path
        self.wavelength = wavelength

    def __str__(self):
        return f'transponder:{self.transponder}G; ' \
               f'path:{self.path.id}; ' \
               f'wavelength:S{self.wavelength}'
