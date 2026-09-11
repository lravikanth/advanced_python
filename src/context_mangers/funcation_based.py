from contextlib import contextmanager


@contextmanager
def open_file(path: str, mode: str):
    file = open(path, mode)  # noqa: SIM115
    try:
        yield file
    except Exception as e:
        print("Exceptiion: ", e)
    finally:
        file.close()


with open_file("sample2.txt", "w") as f:
    f.write("another sample")
    raise FileNotFoundError('File not found')

print(f.closed)


# In funcation based context manager exceptions happen 'yeild f' file
# this line is the whole with block.
# so wrap yeild line in try catch block
