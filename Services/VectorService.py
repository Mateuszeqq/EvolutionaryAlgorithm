import copy
import random
from Modules.Vector import Vector


class VectorService:
    def __init__(self):
        pass

    def create_vector(self, transponders, paths, wavelenghts):
        transponder = random.choice(transponders)
        path, wavelength = self.get_path(paths, wavelenghts)
        for link in path.links:
            link.wavelen_used.append(wavelength)
        return Vector(transponder, path, wavelength)

    def get_path(self, paths, wavelenghts):
        path = random.choice(paths)
        wls = self.wavelengths_avaible_in_path(path, wavelenghts)
        if len(wls) > 0:
            wl = random.choice(wls)
            return path, wl
        else:
            while not len(wls) > 0:
                path = random.choice(paths)
                wls = self.wavelengths_avaible_in_path(path, wavelenghts)
            wl = random.choice(wls)
            return path, wl

    def wavelengths_avaible_in_path(self, path, wavelenghts):
        l = []
        for wl in wavelenghts:
            wl_taken = False
            for link in path.links:
                if wl in link.wavelen_used:
                    wl_taken = True
            if not wl_taken:
                l.append(wl)
        return l



