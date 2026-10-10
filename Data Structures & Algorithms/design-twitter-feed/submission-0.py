import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.following[userId].add(userId)

        self.tweets[userId].append((-self.time, tweetId))

        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = []

        for followee in self.following[userId]:
            for tweet in self.tweets[followee]:
                heapq.heappush(minheap, tweet)
        
        res = []
        for i in range(min(10, len(minheap))):
            time, Id = heapq.heappop(minheap)
            res.append(Id)
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId)
        
