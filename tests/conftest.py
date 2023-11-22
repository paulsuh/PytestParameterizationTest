from pytest import fixture
from glob import glob
from json import load
from yaml import safe_load


def pytest_generate_tests(metafunc):

    # load up files in test_data dir
    # check file names against test names
    # parameterize against list of names if match
    test_name = metafunc.definition.name.removeprefix("test_")
    test_data_filenames = glob(f"./test_data/{test_name}*")

    fixture_data_list = []
    for one_data_file in test_data_filenames:
        with open(one_data_file) as fp:
            if one_data_file.endswith(".json"):
                test_data = load(fp)
            elif one_data_file.endswith((".yaml", ".yml")):
                test_data = safe_load(fp)

            fixture_data_list.append([test_data["input"], test_data["expected_result"]])

    metafunc.parametrize(
        ("input", "expected_result"),
        fixture_data_list,
        scope="function"
    )


@fixture
def other_fixture():
    return "blah blah blah"
