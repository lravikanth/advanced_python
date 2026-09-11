from tracemalloc import Traceback


class open_file1:
    def __init__(self, path: str, mode: str):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.path, mode=self.mode)
        return self.file

    # return false so that the exception get thrown to app
    # return true if not expception and app dont want the app to know about it
    def __exit__(self, exc_type, exc, tb: Traceback) -> bool:
        if self.file is not None:
            self.file.close()

        if exc is not None:
            print(f"exc_type: {exc_type}")
            print(f"exc: {exc}")
            print(f"trace back tb: {tb}")
            return True

        return True


with open_file1("sample.txt", "w") as f:
    f.write("TEst Data")
    raise ValueError


print(f.closed)
