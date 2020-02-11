from InstagramAPI import InstagramAPI, os


class HashtagReader:
    """
    Hashtag Reader object storing items from json and hashtag counts as dictionary
    """
    def __init__(self):
        self.items = []
        self.hashDict = dict()

    def checkBannedTags(self):
        """
        Check for banned hashtags using included dictionary dict.txt
        :return:
        """
        # Reads dictionary file
        with open("dict.txt") as dictFile:
            dictionary = dictFile.readlines()
            dictionary = filter(None, [word.rstrip("\n") for word in dictionary])   # Remove empty strings
        dictSet = set(dictionary)

        # Reads each post and output if found banned hashtags
        for item in self.items:
            try:
                text = item['caption']['text']
                hashtags = {tag.strip("#") for tag in text.split() if tag.startswith("#")}
                result = hashtags.intersection(dictSet)
                if len(result) != 0:
                    print("===========Post code: " + item['code'] + "=============")
                    print(hashtags)
                    print("Found banned hashtags:")
                    print(result)
            except TypeError:
                pass   # Do Nothing
            self.countHashtags(hashtags)
        print("========All posts successfully checked========")

    def countHashtags(self, hashtags):
        """
        Adding/updating hashtags to the hashtag dictionary
        :param hashtags: set of hashtags of a post
        :return:
        """
        for hashtag in hashtags:
            if hashtag not in self.hashDict.keys():
                self.hashDict.update({hashtag: 1})
            else:
                self.hashDict.update({hashtag: self.hashDict[hashtag] + 1})

    def printAll(self):
        """
        prints captions of all posts
        :return:
        """
        for item in self.items:
            try:
                print("=========Post code: " + item['code'] + "=============")
                print(item['caption']['text'])
            except TypeError:
                print("(Empty caption text)")

    def printHashtagsDict(self):
        """
        Prints top 10 hashtags of user
        :return:
        """
        print("========Top 10 Hashtags=========")
        hashtagList = sorted(self.hashDict, key=self.hashDict.get, reverse=True)
        count = 0
        for hashtag in hashtagList:
            print(hashtag, self.hashDict[hashtag])
            count += 1
            if count >= 10:
                return


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


def readHashtags():
    """
    Get all posts by user then run the instance methods of reader
    :return:
    """
    next_max_id = True
    reader = HashtagReader()
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''
        _ = api.getUserFeed(usernameId=userId, maxid=next_max_id)
        reader.items.extend(api.LastJson.get('items', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    reader.checkBannedTags()
    reader.printHashtagsDict()


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
    # TODO: Input IG account username and password
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
    readHashtags()
