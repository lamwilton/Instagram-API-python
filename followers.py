from InstagramAPI import InstagramAPI, os


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
    return freader.followers, freader.followings


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


if __name__ == "__main__":
    # Login with test account
    # TODO: Input username and password
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
    followers, followings = readFollow()
    nonfollowers = findNonFollowers(followers, followings)
    print(nonfollowers)
