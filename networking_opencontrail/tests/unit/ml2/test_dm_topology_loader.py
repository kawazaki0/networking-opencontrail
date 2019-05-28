import mock

from networking_opencontrail.ml2 import dm_topology_loader
from networking_opencontrail.tests import base


# import oslo_config

class TestDmTopologyLoader(base.TestCase):

    # Tests to do:
    # - load topology file on start
    # - more definition in topology (if get correct)

    @mock.patch("oslo_config.cfg.CONF",
                APISERVER=mock.MagicMock(topology=None))
    def setUp(self, conf):
        super(TestDmTopologyLoader, self).setUp()
        self.dm_topology_loader = dm_topology_loader.DmTopologyLoader()

    @mock.patch("oslo_config.cfg.CONF")
    def test_correct_topology_should_return_dict(self, config):
        config.APISERVER = mock.MagicMock()
        topology_filename = mock.MagicMock()
        config.APISERVER.topology = topology_filename

        yaml_file = mock.MagicMock()

        self.dm_topology_loader._load_yaml_file = mock.MagicMock(return_value=yaml_file)

        self.dm_topology_loader._load_yaml_file.assert_called_with(topology_filename)


    def test_invalid_yaml_should_raise_exception(self):
        self.fail()

    def test_invalid_format_should_raise_exception(self):
        self.fail()

    def test_empty_topology_file_should_return_empty_dict(self):
        self.fail()

    def test_no_file_should_raise_exception(self):
        self.fail()
