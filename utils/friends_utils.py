from typing import List

from .models import Blog, Comment, User


def find_first_level_friends(user: User) -> List[User]:
    """Find all users who have commented on the same blog as the given user"""
    friends = set()
    comments = Comment.objects.filter(user=user)
    for comment in comments:
        friends |= set(comment.blog.comments.exclude(user=user).values_list("user", flat=True))
    return list(friends)


def find_second_level_friends(user: User) -> List[User]:
    """Find all users who have commented on a blog where a first level friend has commented"""
    first_level_friends = find_first_level_friends(user)
    second_level_friends = set()
    for friend in first_level_friends:
        comments = Comment.objects.filter(user=friend)
        for comment in comments:
            friends = set(comment.blog.comments.exclude(user__in=[user, friend]).values_list("user", flat=True))
            second_level_friends |= friends
    return list(second_level_friends - set(first_level_friends))


def find_nth_level_friends(user: User, level: int) -> List[User]:
    """Find all users who are nth level friends of the given user"""
    if level == 1:
        return find_first_level_friends(user)
    elif level == 2:
        return find_second_level_friends(user)
    else:
        friends = set()
        for friend in find_first_level_friends(user):
            friends |= set(find_nth_level_friends(friend, level - 1))
        return list(friends - set(find_first_level_friends(user)) - set([user]))