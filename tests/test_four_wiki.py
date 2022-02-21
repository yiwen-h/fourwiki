from fourwiki.lib import try_me

def test_try_me():
    result = try_me()
    assert type(result) == str
