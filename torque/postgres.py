# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""TODO"""

from torque import v1


class V1ClusterInterface(v1.bond.Interface):
    """TODO"""

    def uri(self, database: str, user: str) -> v1.utils.Future[str]:
        """TODO"""


class V1ServiceInterface(v1.component.SourceInterface):
    """TODO"""

    def uri(self, database: str, user: str) -> v1.utils.Future[str]:
        """TODO"""


class V1Component(v1.component.Component):
    """TODO"""

    @classmethod
    def on_requirements(cls) -> dict[str, object]:
        """TODO"""

        return {
            "cluster": {
                "interface": V1ClusterInterface,
                "required": True
            }
        }

    def on_interfaces(self) -> [v1.component.Interface]:
        """TODO"""

        return [
            V1ServiceInterface(uri=self._uri)
        ]

    def _uri(self, database: str, user: str) -> v1.utils.Future[str]:
        """TODO"""

        return self.interfaces.cluster.uri(database, user)


repository = {
    "v1": {
        "components": [
            V1Component
        ]
    }
}
