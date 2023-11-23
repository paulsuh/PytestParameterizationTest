from src.main import three_times, five_times, _main

def test_func_one(input, expected_result):
    assert expected_result == three_times(input)


def test_func_two(other_fixture, input, expected_result):
    # logging.error(f"other_fixture={other_fixture}")
    # print(f"other_fixture={other_fixture}")
    assert expected_result == five_times(input)


def test_main(capsys):
    _main()
    captured = capsys.readouterr()
    assert captured.out == "PyCharmPyCharmPyCharm\nPyCharmPyCharmPyCharmPyCharmPyCharm\n"
