from lxml import etree
import re
from pandas import DataFrame as df


class Study_RE(object):
    __slots__ = ['string', 'pat']

    def __init__(self, string, pat):
        self.string = string
        self.pat = pat

    def demo(self):
        r = re.search(self.pat, self.string)
        r1 = re.findall(self.pat, self.string)
        r2 = re.match(self.pat, self.string)

        print(r)
        print(r1)
        print(r2)


if __name__ == '__main__':
    character = 'pythonthonth'
    pa = 'th'
    sr = Study_RE(character, pa)
    sr.demo()
