"""
LeetCode Problem #355: Design Twitter
Difficulty: Medium
Link: https://leetcode.com/problems/design-twitter/

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, 
and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:
- Twitter() Initializes your twitter object.
- void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId.
- List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. 
  Each item in the news feed must be posted by users who the user followed or by the user themself.
- void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
- void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

Algorithm: Hash Map + Min Heap
Time Complexity: 
    - postTweet: O(1)
    - follow/unfollow: O(1)
    - getNewsFeed: O(N log 10) where N is total tweets from user + followees
Space Complexity: O(U + T) where U is users and T is tweets
"""

import heapq
from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        """
        Initialize the Twitter data structure.
        
        Data structures:
        - tweets: userId -> list of (timestamp, tweetId) tuples
        - following: userId -> set of followeeIds
        - timestamp: global counter for tweet ordering (newer = higher)
        """
        self.tweets = defaultdict(list)  # userId -> [(timestamp, tweetId), ...]
        self.following = defaultdict(set)  # userId -> {followeeId, ...}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Post a new tweet.
        
        Args:
            userId: ID of user posting the tweet
            tweetId: ID of the tweet
        """
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet IDs in user's news feed.
        
        Strategy: Use a min heap to keep track of 10 most recent tweets.
        Collect tweets from user and all followees, then return top 10.
        
        Args:
            userId: ID of user requesting news feed
        
        Returns:
            List of up to 10 most recent tweet IDs
        """
        # Min heap to store (timestamp, tweetId) - keep only 10 largest timestamps
        minHeap = []
        
        # Get all relevant users (self + followees)
        relevantUsers = self.following[userId].copy()
        relevantUsers.add(userId)  # Include user's own tweets
        
        # Collect tweets from all relevant users
        for user in relevantUsers:
            for timestamp, tweetId in self.tweets[user]:
                if len(minHeap) < 10:
                    heapq.heappush(minHeap, (timestamp, tweetId))
                elif timestamp > minHeap[0][0]:
                    heapq.heapreplace(minHeap, (timestamp, tweetId))
        
        # Extract tweets and sort by timestamp (descending)
        result = sorted(minHeap, reverse=True)
        return [tweetId for _, tweetId in result]

    def getNewsFeedMaxHeap(self, userId: int) -> List[int]:
        """
        Alternative implementation using max heap - simpler but less efficient.
        
        Collects all tweets and uses heap to get top 10.
        Time: O(N log N) where N is total tweets
        
        Args:
            userId: ID of user requesting news feed
        
        Returns:
            List of up to 10 most recent tweet IDs
        """
        # Max heap (use negative timestamp)
        maxHeap = []
        
        # Get all relevant users
        relevantUsers = self.following[userId].copy()
        relevantUsers.add(userId)
        
        # Add all tweets to max heap
        for user in relevantUsers:
            for timestamp, tweetId in self.tweets[user]:
                heapq.heappush(maxHeap, (-timestamp, tweetId))
        
        # Pop up to 10 most recent
        result = []
        for _ in range(min(10, len(maxHeap))):
            _, tweetId = heapq.heappop(maxHeap)
            result.append(tweetId)
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        User starts following another user.
        
        Note: A user cannot follow themselves (though some implementations allow it).
        
        Args:
            followerId: ID of user who is following
            followeeId: ID of user being followed
        """
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        User stops following another user.
        
        Args:
            followerId: ID of user who is unfollowing
            followeeId: ID of user being unfollowed
        """
        self.following[followerId].discard(followeeId)


# Test cases
if __name__ == "__main__":
    # Test case 1: Basic operations
    print("Test Case 1: Basic operations")
    twitter = Twitter()
    twitter.postTweet(1, 5)  # User 1 posts tweet 5
    print(f"getNewsFeed(1): {twitter.getNewsFeed(1)}")  # Expected: [5]
    
    twitter.follow(1, 2)  # User 1 follows user 2
    twitter.postTweet(2, 6)  # User 2 posts tweet 6
    print(f"getNewsFeed(1): {twitter.getNewsFeed(1)}")  # Expected: [6, 5]
    
    twitter.unfollow(1, 2)  # User 1 unfollows user 2
    print(f"getNewsFeed(1): {twitter.getNewsFeed(1)}")  # Expected: [5]
    print()
    
    # Test case 2: Multiple users and tweets
    print("Test Case 2: Multiple users and tweets")
    twitter2 = Twitter()
    twitter2.postTweet(1, 1)
    twitter2.postTweet(1, 2)
    twitter2.postTweet(2, 3)
    twitter2.postTweet(2, 4)
    twitter2.postTweet(3, 5)
    
    twitter2.follow(1, 2)
    twitter2.follow(1, 3)
    
    feed = twitter2.getNewsFeed(1)
    print(f"getNewsFeed(1): {feed}")  # Expected: [5, 4, 3, 2, 1] (most recent first)
    print()
    
    # Test case 3: More than 10 tweets
    print("Test Case 3: More than 10 tweets")
    twitter3 = Twitter()
    for i in range(15):
        twitter3.postTweet(1, i)
    
    feed = twitter3.getNewsFeed(1)
    print(f"getNewsFeed(1): {feed}")  # Expected: [14, 13, 12, 11, 10, 9, 8, 7, 6, 5]
    print(f"Length: {len(feed)}")  # Expected: 10
    print()
    
    # Test case 4: Following and unfollowing
    print("Test Case 4: Following and unfollowing")
    twitter4 = Twitter()
    twitter4.postTweet(1, 10)
    twitter4.postTweet(2, 20)
    twitter4.postTweet(3, 30)
    
    twitter4.follow(1, 2)
    twitter4.follow(1, 3)
    print(f"getNewsFeed(1) after following 2,3: {twitter4.getNewsFeed(1)}")
    
    twitter4.unfollow(1, 2)
    print(f"getNewsFeed(1) after unfollowing 2: {twitter4.getNewsFeed(1)}")
    print()
    
    # Test case 5: User with no tweets or follows
    print("Test Case 5: Empty news feed")
    twitter5 = Twitter()
    print(f"getNewsFeed(1) for user with no activity: {twitter5.getNewsFeed(1)}")
    print()
    
    # Test case 6: Self-follow attempt
    print("Test Case 6: Self-follow attempt")
    twitter6 = Twitter()
    twitter6.postTweet(1, 100)
    twitter6.follow(1, 1)  # Should not add (implementation prevents this)
    print(f"Following after self-follow: {twitter6.following[1]}")
    print(f"getNewsFeed(1): {twitter6.getNewsFeed(1)}")  # Should still show own tweet
