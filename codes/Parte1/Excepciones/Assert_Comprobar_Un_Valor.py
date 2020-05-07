try:
    assert 1 > 10 # false, entonces da error y va al except
except AssertionError:
    print("error de assert")