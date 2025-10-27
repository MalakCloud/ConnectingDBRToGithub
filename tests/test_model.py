# Simple test file
def test_example():
    """A simple test to verify testing works"""
    assert 1 + 1 == 2
    print("✅ Test passed!")

def test_data_loading():
    """Test that we can load data"""
    from sklearn.datasets import load_iris
    iris = load_iris()
    assert iris.data.shape[0] > 0
    print("✅ Data loading test passed!")
