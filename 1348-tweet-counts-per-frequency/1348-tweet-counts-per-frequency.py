class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == "minute":
            frequency = 60
        elif freq == "hour":
            frequency = 3600
        else:
            frequency = 86400

        chunks = (endTime - startTime) // frequency + 1
        res = [0] * chunks
        
        for time in self.tweets[tweetName]:
            if startTime <= time <= endTime:
                chunk = (time - startTime) // frequency
                res[chunk] += 1
        return res
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)