import xmltodict


class XMLNetworkParser:
    def __init__(self, path):
        self.path = path
        self.document = self.parse_to_dict()

    def parse_to_dict(self):
        with open(self.path, "rb") as f:
            return xmltodict.parse(f, dict_constructor=dict)

    def nodes(self):
        dict_nodes = self.document['network']['networkStructure']['nodes']['node']
        net_nodes = []
        for net_node in dict_nodes:
            net_nodes.append((net_node['@id'], net_node['coordinates']['x'], net_node['coordinates']['y']))

        return net_nodes

    def links(self):
        dict_links = self.document['network']['networkStructure']['links']['link']
        net_links = []
        for net_link in dict_links:
            net_links.append((net_link['@id'], net_link['source'], net_link['target']))

        return net_links

    def demands(self):
        dict_demands = self.document['network']['demands']['demand']
        net_demands = []
        for net_demand in dict_demands:
            net_demands.append((net_demand['@id'],
                                (net_demand['source'], net_demand['target']),
                                float(net_demand['demandValue'])))

        return net_demands

    def paths(self):
        dict_demands = self.document['network']['demands']['demand']
        net_paths = []
        for net_demand in dict_demands:
            dem_paths = []
            demand_paths = net_demand['admissiblePaths']['admissiblePath']
            for path in demand_paths:
                dem_paths.append((path['@id'], path['linkId']))
            net_paths.append(dem_paths)

        return net_paths


if __name__ == '__main__':
    parsed = XMLNetworkParser('data/polska.xml')
    demands = parsed.links()
