import mine_dwarf.file as test_module

def test_read_file():
    ret = test_module.open_file('resources/example.txt')
    assert ret == 'Hello World'