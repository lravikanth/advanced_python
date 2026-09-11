from dataclasses import dataclass

sen = "This is a test to work on"
l1 = sen.split(" ")
for i in l1:
    print(i)


@dataclass
class Sentence:
    s: str

    def next_word(self):
        yield from self.s.split(" ")


s1 = Sentence("This is a sentafcen to work on")
for i in s1.next_word():
    print(i)
