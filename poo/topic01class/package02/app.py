from poo.topic01class.package02.lg.remote_lg_tv import RemoteLgTv
from poo.topic01class.package02.samsung.remote_samsung_tv import RemoteSamsungTv
from poo.topic01class.package02.remotetv import RemoteTv

def main():
    remote_lg_tv = RemoteLgTv()
    remote_samsung_tv = RemoteSamsungTv()
    print("======= LG =======")

    print("State of TV", remote_lg_tv.is_turned_on_tv)
    print(remote_lg_tv.power())
    print(remote_lg_tv.increase_volume())
    print(remote_lg_tv.upload_channel())

    # Validate value of the variable is_turned_on_tv
    print(RemoteTv.is_turned_on_tv)
    print(remote_lg_tv.power(), end='\n\n')

    print("======= Samsung =======")

    RemoteTv.is_turned_on_tv = True

    print("State of TV", remote_samsung_tv.is_turned_on_tv)
    print(remote_samsung_tv.power())
    print(remote_samsung_tv.increase_volume())
    print(remote_samsung_tv.upload_channel())

    # Validate value of the variable is_turned_on_tv
    print(RemoteTv.is_turned_on_tv)
    print(remote_samsung_tv.power(), end='\n\n')


if __name__ == "__main__":
    main()
