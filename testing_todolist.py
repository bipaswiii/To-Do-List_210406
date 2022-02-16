import pytest
import random


@pytest.fixture
def tester():
    list_1 = "Take doggos out for walk"
    list_2= "Make breakfast"
    list_3 = "Work and meetups"
    list_4 = "Gym"
    return (list_1, list_2, list_3, list_4)


def test1(tester):
    list_1 = "Take doggos out for walk"
    assert tester[0] == list_1

def test_2(tester):
    list_2 = "Make lunch"
    assert tester[1] == list_2

def test_3(tester):
    list_3 = "Work and meetups4"
    assert tester[2] == list_3


def test_4(tester):
    list_4 = "Gym"
    assert tester[3] ==list_4