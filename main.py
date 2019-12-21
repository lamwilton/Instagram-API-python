from InstagramAPI import InstagramAPI, os
import json


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
            dictionary = [word.rstrip("\n") for word in dictionary]
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
                _   # Do Nothing
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

    def getFirstComment(self) -> str:
        # TODO Complete this method, struggling
        """
        Get First comment of the post
        :return: First comment text
        """
        media_id = self.item['id']
        has_more_comments = True
        max_id = ''
        comments = []
        while has_more_comments:
            _ = api.getMediaComments(media_id, max_id=max_id)
            for c in reversed(api.LastJson['comments']):
                comments.append(c)
            has_more_comments = api.LastJson.get('has_more_comments', False)

            if has_more_comments:
                max_id = json.loads(api.LastJson.get('next_max_id', ''))['server_cursor']
            if len(comments) >= self.item['comment_count']:
                has_more_comments = False
        return ""

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
        hashtagList = sorted(reader.hashDict, key=reader.hashDict.get, reverse=True)
        count = 0
        for hashtag in hashtagList:
            print(hashtag, self.hashDict[hashtag])
            count += 1
            if count >= 10:
                return


if __name__ == "__main__":
    # Login with test account
    api = InstagramAPI("YOUR_LOGIN", "YOUR_PASSWORD", False, os.path.dirname(os.path.abspath(__file__)))
    api.login()
    next_max_id = True

    # Input user ID
    userId = input("Enter Instagram user ID (leave blank for tombrady): ")
    if userId == "":
        userId = 1665557140
    # Get all posts by user
    reader = HashtagReader()
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''
        _ = api.getUserFeed(usernameId=userId, maxid=next_max_id)
        reader.items.extend(api.LastJson.get('items', []))
        next_max_id = api.LastJson.get('next_max_id', '')

    reader.checkBannedTags()
    reader.printHashtagsDict()
