from poo.topic10final.typingfinal import Config


def main():
    print(Config.VERSION)
    # Si intentas cambiarlo, Python lo permite en ejecución,
    # pero el type checker (mypy/pyright) marcará error.
    # c.VERSION = "2.0.0"  # Error de tipado

if __name__ == "__main__":
    main()
