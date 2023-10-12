import unittest
import re
from datetime import date

from repolist import repolist

class TestRepoList(unittest.TestCase):
    def testRepoInvissy(self):
        id = "invissy"
        match = re.findall(r'Repo: \w+ Number of commits: \d+', repolist(id))
        self.assertTrue(match, "Output is not in the correct format")

    def testRepoLogan630(self):
        id = "logan630"
        match = re.findall(r'Repo: \w+ Number of commits: \d+', repolist(id))
        self.assertTrue(match, "Output is not in the correct format")
    
    def testRepoColleenQue(self):
        id = "ColleenQue"
        match = re.findall(r'Repo: \w+ Number of commits: \d+', repolist(id))
        self.assertTrue(match, "Output is not in the correct format")

    def testRepoUnrealOG(self):
        id = "UnrealOG"
        match = re.findall(r'Repo: \w+ Number of commits: \d+', repolist(id))
        self.assertTrue(match, "Output is not in the correct format")

def my_brand():
    print("=*=*=*= Cindy Lee =*=*=*=")
    print("=*=*=*= Course 2023S-SSW567 =*=*=*=")
    print("=*=*=*= HW 04a - Develop with the Perspective of the Tester in mind =*=*=*=")
    print("=*=*=*=", date.today(), "=*=*=*=")
    print()

if __name__ == '__main__':
    my_brand()
    print('Running unit tests')
    unittest.main()