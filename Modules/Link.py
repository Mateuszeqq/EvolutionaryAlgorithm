class Link:
    def __init__(self, id, source, target):
        self.id = id
        self.source = source
        self.target = target
        self.wavelen_used = []

    def __str__(self):
        return f"id:{self.id}, source:{self.source}, target:{self.target}"
