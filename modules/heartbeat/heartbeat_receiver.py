"""
Heartbeat receiving logic.
"""

from pymavlink import mavutil

from ..common.modules.logger import logger


# =================================================================================================
#                            ↓ BOOTCAMPERS MODIFY BELOW THIS COMMENT ↓
# =================================================================================================
class HeartbeatReceiver:
    """
    HeartbeatReceiver class to send a heartbeat
    """

    __private_key = object()

    @classmethod
    def create(
        cls,
        connection: mavutil.mavfile,
        local_logger: logger.Logger
    ) -> "tuple [True, HeartbeatReceiver] | tuple [False, None]":
        """
        Falliable create (instantiation) method to create a HeartbeatReceiver object.
        """
        return cls.__init__(cls.__private_key, connection, local_logger)

    def __init__(
        self,
        key: object,
        connection: mavutil.mavfile,
        local_logger: logger.Logger
    ) -> None:
        assert key is HeartbeatReceiver.__private_key, "Use create() method"

        # Do any intializiation here
        self.local_logger = local_logger

    def run(
        self,
        local_logger: logger.Logger
    ) -> "tuple[True, None]":
        """
        Attempt to recieve a heartbeat message.
        If disconnected for over a threshold number of periods,
        the connection is considered disconnected.
        """
        self.connection.recv_match(
            mavutil.mavlink.SYS_STATUS,
            mavutil.mavlink.
        )


        return True, None


# =================================================================================================
#                            ↑ BOOTCAMPERS MODIFY ABOVE THIS COMMENT ↑
# =================================================================================================
