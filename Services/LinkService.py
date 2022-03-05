from Modules.Link import Link


class LinkService:
    def __init__(self):
        pass

    def create_link(self, id, source, target):
        return Link(id, source, target)

    def create_links(self, links):
        return [self.create_link(link[0], link[1], link[2]) for link in links]

    def find_link_by_id(self, links, id):
        for link in links:
            if link.id == id:
                return link
        return None

    def get_unique_links(self, links):
        result = []
        l = [result.append([link[0], link[1], link[2]]) for link in links if [link[0], link[1], link[2]] not in result]
        l = list(set(l))
        return l