from fourwiki.lib import try_me

def test_try_me():
    result1, result2 = try_me()
    assert type(result1 + result2) == str
