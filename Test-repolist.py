import unittest
from datetime import date

from repolist import repolist

class TestRepoList(unittest.TestCase):
    def testRepoInvissy(self):
        self.assertEqual(repolist("invissy"), "Repo: GitHubApi567 Number of commits: 1\n" +
            "Repo: SSW-345-Abstract-Pizza-Factory Number of commits: 6\n" +
            "Repo: SSW-345-Singleton-and-Visitor-Pattern Number of commits: 3\n"
            "Repo: SSW-345-To-Do-List-Bot Number of commits: 5\n"
            "Repo: Triangle567 Number of commits: 13")
        
    def testRepoLogan630(self):
        self.assertEqual(repolist("logan630"), "Repo: cs-546-final-project-flashcard-app Number of commits: 30\n" +
            "Repo: gamejam_4_23 Number of commits: 30\n" +
            "Repo: Robot-Simulation Number of commits: 9\n")
        
    def testRepoColleenQue(self):
        self.assertEqual(repolist("ColleenQue"), "Repo: 396Assignment3b Number of commits: 7\n" + 
            "Repo: Algorithms Number of commits: 4\n" +
            "Repo: Colleen-Website Number of commits: 30\n" +
            "Repo: ColleenQue Number of commits: 6\n" +
            "Repo: data-structures Number of commits: 2\n" +
            "Repo: git-workshop-cq Number of commits: 11\n" +
            "Repo: Hack-it-together Number of commits: 30\n" +
            "Repo: IoT4Ag Number of commits: 12\n" +
            "Repo: PLaF Number of commits: 30\n" +
            "Repo: SAT-Words Number of commits: 7\n" +
            "Repo: statistics Number of commits: 5\n" +
            "Repo: Systems-Programming Number of commits: 5\n" +
            "Repo: wikipop Number of commits: 30\n" +
            "Repo: Word-Boss Number of commits: 30")

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