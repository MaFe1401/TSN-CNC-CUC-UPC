from colorlog import info
from typing import List, Dict, Union, Any

from yangson.instance import InstanceRoute
from jetconf.data import BaseDatastore, DataChange
from jetconf.helpers import ErrorHelpers, LogHelpers
from jetconf.handler_base import ConfDataListHandler

JsonNodeT = Union[Dict[str, Any], List]
epretty = ErrorHelpers.epretty
debug_confh = LogHelpers.create_module_dbg_logger(__name__)


# ---------- User-defined handlers follow ----------


class JukeboxExampleConfHandler(ConfDataListHandler):
    def create_item(self, ii: InstanceRoute, ch: "DataChange"):
        debug_confh(self.__class__.__name__ + " replace triggered")
        info("Creating item '/ieee802-dot1q-tsn-types:group-interface-id' in app configuration")

    def create_list(self, ii: InstanceRoute, ch: "DataChange"):
        debug_confh(self.__class__.__name__ + " replace triggered")
        info("Creating list '/ieee802-dot1q-tsn-types:group-interface-id' in app configuration")

    def replace_item(self, ii: InstanceRoute, ch: "DataChange"):
        debug_confh(self.__class__.__name__ + " replace triggered")
        info("Replacing item '/ieee802-dot1q-tsn-types:group-interface-id' in app configuration")

    def replace_list(self, ii: InstanceRoute, ch: "DataChange"):
        debug_confh(self.__class__.__name__ + " replace triggered")
        info("Replacing list '/ieee802-dot1q-tsn-types:group-interface-id' in app configuration")

    def delete_item(self, ii: InstanceRoute, ch: "DataChange"):
        debug_confh(self.__class__.__name__ + " delete triggered")
        info("Deleting item '/ieee802-dot1q-tsn-types:group-interface-id' from app configuration")

    def delete_list(self, ii: InstanceRoute, ch: "DataChange"):
        debug_confh(self.__class__.__name__ + " delete triggered")
        info("Deleting list '/ieee802-dot1q-tsn-types:group-interface-id' from app configuration")


def register_conf_handlers(ds: BaseDatastore):
    ds.handlers.conf.register(JukeboxExampleConfHandler(ds, "/ieee802-dot1q-tsn-types:group-interface-id"))
