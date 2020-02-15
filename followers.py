from InstagramAPI import InstagramAPI, os
import json


class FollowerReader:
    """
    Class for reading followers/following
    """
    def __init__(self):
        self.followers = []
        self.followings = []

    def readFollowers(self):
        """
        Reads followers and save list to self.followers
        :return:
        """
        next_max_id = True
        while next_max_id:
            if next_max_id is True:
                next_max_id = ''
            _ = api.getUserFollowers(usernameId=userId, maxid=next_max_id)
            entries = api.LastJson.get('users')
            for entry in entries:
                self.followers.append(entry['username'])
            next_max_id = api.LastJson.get('next_max_id', '')

    def readFollowings(self):
        """
        Reads followings and save list to self.followings
        :return:
        """
        next_max_id = True
        while next_max_id:
            if next_max_id is True:
                next_max_id = ''
            _ = api.getUserFollowings(usernameId=userId, maxid=next_max_id)
            entries = api.LastJson.get('users')
            for entry in entries:
                self.followings.append(entry['username'])
            next_max_id = api.LastJson.get('next_max_id', '')


def readFollow():
    """
    Read followers/followings
    :return: List of followers/followings
    """
    freader = FollowerReader()
    freader.readFollowers()
    freader.readFollowings()
    with open('followers.json', 'r') as infile:
        prevFollowers = json.load(infile)
    with open('followers.json', 'w') as outfile:
        json.dump(freader.followers, outfile)
    return freader.followers, freader.followings, prevFollowers


def findNonFollowers(followers, followings):
    """
    Find non followers by set difference
    :param followers: List of followers
    :param followings: List of followings
    :return: Set of non followers
    """
    followerset = set(followers)
    followingset = set(followings)
    return followingset.difference(followerset)


def findUnfollowed(followers, prevFollowers):
    """
    Find who unfollowed you since last check, as well as new followers
    :param followers:
    :param prevFollowers:
    :return: Set of un-followers, then new followers
    """
    followerset = set(followers)
    prevFollowerset = set(prevFollowers)
    return prevFollowerset.difference(followerset), followerset.difference(prevFollowerset)


if __name__ == "__main__":
    # Login with test account
    # TODO : Fill in username/password
    api = InstagramAPI("USERNAME", "PASSWORD", False, os.path.dirname(os.path.abspath(__file__)))
    api.login()

    # Input username and searches for user ID
    valid = False
    while not valid:
        userName = input("Enter Instagram username: ")
        api.searchUsername(userName)
        try:
            userId = api.LastJson.get('user')['pk']
            valid = True
        except TypeError:
            print('User not Found')

    # Main functions
    followers, followings, prevFollowers = readFollow()
    nonfollowers = findNonFollowers(followers, followings)
    unfollowers, newfollowers = findUnfollowed(followers, prevFollowers)
    print("Number of followers: " + str(len(followers)))
    print("Number of followings: " + str(len(followings)))
    print("Number of un-followers (People unfollowed you since last check): " + str(len(unfollowers)))
    print(unfollowers)
    print("Number of new followers: " + str(len(newfollowers)))
    print(newfollowers)
    print("Number of non-followers (People who are not following back): " + str(len(nonfollowers)))
    print(nonfollowers)
