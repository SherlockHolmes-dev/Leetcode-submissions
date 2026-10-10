import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0  # Global timestamp
        self.tweets = defaultdict(list)  # userId -> list of (time, tweetId)
        self.following = defaultdict(set)  # userId -> set of followees
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Auto-follow self if not already following
        self.following[userId].add(userId)
        # Add tweet with current timestamp
        self.tweets[userId].append( (-self.time, tweetId) )  # Negative time for max-heap
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        
        # Collect tweets from self and followees
        for followee in self.following[userId]:
            for tweet in self.tweets[followee]:
                heapq.heappush(heap, tweet)
        
        # Get top 10 most recent tweets
        res = []
        for _ in range(min(10, len(heap))):
            time, tweetId = heapq.heappop(heap)
            res.append(tweetId)
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Prevent unfollowing self
        if followeeId != followerId:
            self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)