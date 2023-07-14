import instaloader
import datetime

global followerList
global followeeList
global profileFollowers
global profileFollowees

def loadInsta():
    L = instaloader.Instaloader()

    L.login("username","password")
    #this doesnt have to be your target acc, but if your target acc is private, this acc  mus t follow your target acc

    profile = instaloader.Profile.from_username(L.context,'targetacc')


    profileFollowees = profile.get_followees()
    profileFollowers = profile.get_followers()

    followerList = []
    followeeList = []


def addToLists():
    for follower in profileFollowers:
        followerList.append(follower.username)

    for followee in profileFollowees:
        followeeList.append(followee.username)

def compareLists():
    for followee in followeeList:
        if followee not in followerList:
            print(followee +" doesnt follow back")

def createFollowersLog():
    f = open(f"{datetime.datetime.now().day}" +"-" + f"{datetime.datetime.now().month}"+"-" + f"{datetime.datetime.now().year}followers.txt","a")
    for follower in followerList:
        f.write(follower + '\n')

def createFolloweesLog():
    f = open(f"{datetime.datetime.now().day}" +"-" + f"{datetime.datetime.now().month}"+"-" + f"{datetime.datetime.now().year}followee.txt","a")
    for followee in followeeList:
        f.write(followee + '\n')


def compareLogs():
    firstFollowerTxt = open("C:\\Users\\agkam\\OneDrive\\Desktop\\code2\\python\\InstagramWhoUnfollowed\\12-7-2023followers.txt")
    secondFollowerTxt = open("C:\\Users\\agkam\\OneDrive\\Desktop\\code2\\python\\InstagramWhoUnfollowed\\14-7-2023followers.txt")

    firstFollowerList = firstFollowerTxt.readlines()
    secondFollowerList = secondFollowerTxt.readlines()
    
    for follower in firstFollowerList:
        if follower not in secondFollowerList:
            print(follower + " has recently unfollowed")
    

compareLogs()
