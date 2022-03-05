class Path:
    def __init__(self, id):
        self.id = id
        self.links = []

    def add_link(self, link):
        self.links.append(link)

    def __str__(self):
        return f'{self.id}'
