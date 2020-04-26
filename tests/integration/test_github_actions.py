"""A test that is run only by Github Actions

This test makes real network requests, so environment variables
should be specified in Github Actions.
"""
import os

import pytest

from praw import Reddit
from praw.models import Submission


@pytest.mark.skipif(
    "true" not in os.environ.get("GITHUB_ACTIONS", "").lower(),
    reason="Not running on Github Actions",
)
def test_github_actions():
    reddit = Reddit(user_agent="Github Actions CI Testing")
    assert isinstance(next(reddit.subreddit("all").hot()), Submission)
