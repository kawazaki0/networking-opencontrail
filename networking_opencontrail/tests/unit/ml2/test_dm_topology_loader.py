

import mock
# import oslo_config

from networking_opencontrail.ml2 import dm_integrator
from networking_opencontrail.tests import base

class TestDmTopologyLoader(base.TestCase):


    @mock.patch("oslo_config.cfg.CONF",
                APISERVER=mock.MagicMock(topology=None))
    def setUp(self, conf):
        super(TestDmTopologyLoader, self).setUp()
        # dm_integrator.directory.get_plugin = mock.Mock()
        # dm_integrator.ContrailRestApiDriver = mock.Mock()
        # self.dm_integrator = dm_integrator.DeviceManagerIntegrator()
        # self.core_plugin = self.dm_integrator._core_plugin
        # self.tf_rest_driver = self.dm_integrator.tf_rest_driver

    @mock.patch("oslo_config.cfg.CONF")
    def test_load_topology(self, config):
        # dm_integrator._load_yaml_file = mock.MagicMock(
        #     return_value=self._get_topology())
        pass


        # config.APISERVER = mock.MagicMock(topology=)
        # oslo_config.cfg.CONF = mock.MagicMock()
        # topology = '/tmp'
        # oslo_config.cfg.CONF.APISERVER = mock.MagicMock(topology=topology)

    # def _load_topology_definition(self):
    #     return {}

    def test_load_invalid_topology(self):
        pass

    def test_empty_topology_file(self):
        pass

    def test_topology_file_does_not_exist(self):
        pass