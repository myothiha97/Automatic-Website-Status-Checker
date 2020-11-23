from DashBoardTester import DashBoardTester
from HomePageTester import HomePageTester

from decouple import config

if __name__ == "__main__": 
    
    DashBoardTester.test_requests()
    HomePageTester.test_requests()
    
