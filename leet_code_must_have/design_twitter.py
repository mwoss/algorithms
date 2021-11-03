"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
* void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId.
Each call to this function will be made with a unique tweetId.
* List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed.
Each item in the news feed must be posted by users who the user followed or by the user themself.
Tweets must be ordered from most recent to least recent.
* void follow(int followerId, int followeeId) The user with ID followerId
started following the user with ID followeeId.
* void unfollow(int followerId, int followeeId) The user with ID followerId
    started unfollowing the user with ID followeeId.
"""
import heapq
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import List, Deque, Optional


@dataclass
class TwitterUser:
    followees: List[int] = field(default_factory=list)
    posts: List[int] = field(default_factory=list)


class Twitter:

    def __init__(self):
        # user_id: [posts]
        self._users = defaultdict(TwitterUser)
        self._news_feed_size = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._users[userId].posts.append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        all_posts = []

        for followee_user_id in self._users[userId].followees:
            for post in self._users[followee_user_id].posts:
                self._insert_post(all_posts, post)

        for self_posts in self._users[userId].posts:
            self._insert_post(all_posts, self_posts)

        return all_posts[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self._users[followerId].followees.append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._users[followerId].followees.remove(followeeId)

    def _insert_post(self, collection: List[int], post: int) -> None:
        heapq.heappush(collection, post)
        if len(collection) > self._news_feed_size:
            heapq.heappop(collection)


@dataclass
class Tweet:
    tweet_id: int
    next_tweet: Optional["Tweet"]


@dataclass
class TwitterUser2:
    head_post: Tweet = None
    followees: List[int] = field(default_factory=list)


class Twitter2:

    def __init__(self):
        self._users = defaultdict(TwitterUser2)
        self._news_feed_size = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        if self._users[userId].head_post is None:
            self._users[userId].head_post = Tweet(tweetId, None)
        else:
            tweet = Tweet(tweetId, self._users[userId].head_post)
            # TODO

    def getNewsFeed(self, userId: int) -> List[int]:
        pass

    def follow(self, followerId: int, followeeId: int) -> None:
        self._users[followerId].followees.append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass

    def _insert_post(self, collection: List[int], post: int) -> None:
        pass


if __name__ == '__main__':
    t = Twitter()
    actions = ["postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
    arguments = [[1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
    for action, args in zip(actions, arguments):
        attr = getattr(t, action)
        output = attr(*args)
        print(output)
