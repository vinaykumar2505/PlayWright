import pytest
def test_firstmethod():
    print("test_firstmethod")
@pytest.mark.firstmethod
def test_secondmethod():
    print("test_secondmethod")
def test_thirdmethod():
    print("test_secondmethod")