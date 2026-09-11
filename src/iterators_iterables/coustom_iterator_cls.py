from dataclasses import dataclass, field

# Most business/domain classes should not implement __next__.
# In most real-world classes, use existing iterable collections internally and expose them through __iter__.

# OOTB Iterators/Iterables
# list
# tuple
# set
# dict
# str
# range
# generator


@dataclass
class Eligibility:
    member_id: int
    start_date: str
    end_date: str


@dataclass
class Member:
    name: str
    id: int
    eligibilityList: list[Eligibility] = field(default_factory=list)


member = Member(
    "Ravi", 1, [Eligibility(1, "st date", "end Date"), Eligibility(1, "date1", "date2")]
)

for e in member.eligibilityList:
    print(e)

print(dir(member.eligibilityList))
