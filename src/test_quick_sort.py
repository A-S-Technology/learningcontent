import pytest
from quick_sort import quick_sort

@pytest.fixture
def setup_environment():
    """
    Setup the test environment.
    """
    # Example setup
    data = [5, 3, 1, 2, 4]
    return data

def test_quick(setup_environment):
    """
    Test quick sort.
    """
    data = setup_environment
    assert quick_sort(data) == [1, 2, 3, 4, 5]

@pytest.mark.parametrize(
    "input_array, expected_output",
    [
        ([], []),  # Test empty array
        ([1], [1]),  # Test single element
        ([3, 2, 1], [1, 2, 3]),  # Test unsorted array
        ([5, 1, 5, 3, 5], [1, 3, 5, 5, 5]),  # Test array with duplicates
        ([10, 8, 6, 4, 2], [2, 4, 6, 8, 10]),  # Test reverse sorted array
        ([2, -1, 4, 3, 0], [-1, 0, 2, 3, 4]),  # Test array with negative numbers
    ],
)
def test_quick_sort(input_array, expected_output):
    """
    Test quick sort.
    """
    result = quick_sort(input_array)
    assert result == expected_output, f"Expected: {expected_output}, Got: {result}"