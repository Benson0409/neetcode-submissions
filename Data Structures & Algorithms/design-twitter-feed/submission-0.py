class Twitter:

    def __init__(self):
    
        self.time = 0 
        
        self.following = defaultdict(set) 
        
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1 
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        
        users_to_check = self.following[userId].copy()
        users_to_check.add(userId)
        
        for user in users_to_check:
            recent_tweets = self.tweets[user][-10:]
            
            for time, tweetId in recent_tweets:
                if len(min_heap) < 10:
                    heapq.heappush(min_heap, (time, tweetId))
                elif time > min_heap[0][0]:
                    heapq.heappushpop(min_heap, (time, tweetId))
                    
        min_heap.sort(reverse=True)
        return [tweetId for time, tweetId in min_heap]
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
