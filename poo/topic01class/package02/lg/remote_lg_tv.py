from poo.topic01class.package02.remotetv import RemoteTv

class RemoteLgTv(RemoteTv):
    """Class RemoteLgTv"""

    def increase_volume(self) -> str:
        return "Lg Increase Volume +"

    def lower_volume(self) -> str:
        return "Lg lower Volume -"

    def upload_channel(self) -> str:
        return "LG Upload Channel ->"

    def down_channel(self) -> str:
        return "LG down Channel <-"
