import yaml
from oslo_config import cfg


class DmTopologyLoader(object):

    @classmethod
    def load(cls):
        # TODO(kamman): Topology file should be validate
        if cfg.CONF.APISERVER.topology:
            return cls._load_yaml_file(cfg.CONF.APISERVER.topology)
        else:
            return {}

    @classmethod
    def _load_yaml_file(cls, topology_file):
        with open(topology_file, "r") as topology:
            return yaml.load(topology)
