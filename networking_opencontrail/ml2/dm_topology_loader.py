import yaml
from oslo_config import cfg
from jsonschema import validate, ValidationError


class DmTopologyLoader(object):

    def validate(self, config):

        """
        e.g.
        nodes:
          - name: b1s19-node3
            type: baremetal
            ports:
              - name: ens1f1
                #mac_address: 90:e2:ba:e3:5a:a1
                switch_name: vqfx-10k-leaf2
                port_name: xe-0/0/1
                switch_id: 52:54:00:29:b1:a6
                fabric: fab01
        """

        schema = """
        type: object
        required:
        - nodes
        properties:
          nodes:
            type: array
            items:
              type: object
              required:
              - name
              - ports
              properties:
                name:
                  type: string
                ports:
                  type: array
                  items:
                    type: object
                    required:
                    - switch_name
                    - port_name
                    - switch_id
                    - fabric
                    properties:
                      name:
                        type: string
                      switch_name:
                        type: string
                      port_name:
                        type: string
                      switch_id:
                        type: string
                      fabric:
                        type: string
                """

        try:
            validate(config, yaml.load(schema))
        except ValidationError, e:
            raise ConfigInvalidFormat(e)

    def load(self):
        if cfg.CONF.APISERVER.topology:
            yaml_file = self._load_yaml_file(cfg.CONF.APISERVER.topology)
            self.validate(yaml_file)
            return yaml_file
        else:
            return {}

    def _load_yaml_file(self, topology_file):
        with open(topology_file, "r") as topology:
            return yaml.load(topology)


class ConfigInvalidFormat(Exception):
    pass
