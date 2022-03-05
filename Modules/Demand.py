class Demand:
    def __init__(self, id, source, target, value, admiss_paths):
        self.id = id
        self.source = source
        self.target = target
        self.value = value
        self.admiss_paths = admiss_paths

    def __str__(self):
        return f"id:{self.id}\n" \
               f"source:{self.source}\n" \
               f"target:{self.target}\n" \
               f"value:{self.value}"
