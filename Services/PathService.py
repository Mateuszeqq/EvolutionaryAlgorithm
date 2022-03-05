from Modules.Path import Path
from Services.LinkService import LinkService


class PathService:
    def __init__(self):
        pass

    def create_path(self, xml_path, links):
        link_serv = LinkService()
        path = Path(xml_path[0])
        for link in xml_path[1]:
            link_ = link_serv.find_link_by_id(links, link)
            if link_ is not None:
                path.add_link(link_)

        return path

    def create_admiss_paths(self, paths, links):
        return [self.create_path(path, links) for path in paths]

    def create_paths(self, paths, links):
        return [self.create_admiss_paths(demand_paths, links) for demand_paths in paths]
