import mock

from networking_opencontrail.ml2 import dm_topology_loader
from networking_opencontrail.ml2.dm_topology_loader import ConfigInvalidFormat
from networking_opencontrail.tests import base


def _get_topology():
    switch_port = {'name': 'ens1f1',
                   'switch_name': 'leaf1',
                   'port_name': 'xe-0/0/1',
                   'switch_id': 'mac-address',
                   'fabric': 'fab01'}
    return {'nodes': [{'name': 'compute1', 'ports': [switch_port]}]}


class TestDmTopologyLoader(base.TestCase):

    @mock.patch("oslo_config.cfg.CONF",
                APISERVER=mock.MagicMock(topology=None))
    def setUp(self, conf):
        super(TestDmTopologyLoader, self).setUp()
        self.dm_topology_loader = dm_topology_loader.DmTopologyLoader()

    @mock.patch("oslo_config.cfg.CONF")
    def test_correct_topology_should_return_dict(self, _):
        yaml_file = _get_topology()
        self.dm_topology_loader._load_yaml_file = mock.Mock(
            return_value=yaml_file)

        actual = self.dm_topology_loader.load()

        self.assertEqual(yaml_file, actual)

    @mock.patch("oslo_config.cfg.CONF")
    def test_invalid_schema_should_raise_exception(self, _):
        yaml_file = _get_topology()
        del yaml_file['nodes'][0]['name']

        self.dm_topology_loader._load_yaml_file = mock.Mock(
            return_value=yaml_file)

        self.assertRaises(ConfigInvalidFormat, self.dm_topology_loader.load)

    @mock.patch("oslo_config.cfg.CONF")
    def test_empty_topology_file_should_return_empty_dict(self, _):
        self.dm_topology_loader._load_yaml_file = mock.Mock(return_value={})

        self.assertRaises(ConfigInvalidFormat, self.dm_topology_loader.load)

    @mock.patch("oslo_config.cfg.CONF")
    def test_no_file_should_raise_exception(self, config):
        config.APISERVER = mock.Mock()
        config.APISERVER.topology = '/file_does_not_exist'

        self.assertRaises(IOError, self.dm_topology_loader.load)
