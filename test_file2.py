import pytest
@pytest.mark.order(1)
def test_file2firstmethod(test_precondition):
    print("test_F2firstmethod")
@pytest.fixture(scope="session")
def test_precondition():
    print("test_Precondition")

@pytest.mark.tfiles
@pytest.mark.order(1)
def test_file2secondmethod(test_precondition):
    print("test_F2secondmethod")
@pytest.mark.skip
def test_file2thirdmethod(test_precondition):
    print("test_F2secondmethod")