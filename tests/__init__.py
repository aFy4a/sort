from sort.sort.__init__ import sort

def test_empty():
    assert(sort([]), [])

def test_more_than_5():
    assert(sort([6, 7, 8, 6, 10, 6]), [])

def test_less_than_5():
    assert(sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

def test():
    assert(sort([1, 5, 6, 4, 9, 2, 8]), [1, 5, 4, 2])