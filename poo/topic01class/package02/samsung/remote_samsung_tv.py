from poo.topic01class.package02.remotetv import RemoteTv

class RemoteSamsungTv(RemoteTv):
    """Class RemoteSamsungTv"""

    def increase_volume(self) -> str:
        return "Samsung Increase Volume +"

    def lower_volume(self) -> str:
        return "Samsung lower Volume -"

    def upload_channel(self) -> str:
        return "Samsung Upload Channel ->"

    def down_channel(self) -> str:
        return "Samsung down Channel <-"
