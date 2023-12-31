import os
from json import load
from os.path import join

from pytest import fixture
from yaml import safe_load


def load_test_data_from_file(filepath: str) -> tuple[any, any]:
    with open(filepath) as fp:
        if filepath.endswith(".json"):
            test_data = load(fp)
        elif filepath.endswith((".yaml", ".yml")):
            test_data = safe_load(fp)

        return test_data["input"], test_data["expected_result"]


def pytest_generate_tests(metafunc):

    # load up files in test_data dir
    # check file names against test names
    # parameterize against list of names if match
    test_name = metafunc.definition.name.removeprefix("test_")

    fixture_data_list = []
    for root, dirs, files in os.walk(os.getcwd()):
        # remove dirs that start with .
        for one_dir in dirs:
            if one_dir.startswith("."):
                dirs.remove(one_dir)

        if root.endswith("test_data"):
            test_data_filenames = [
                one_filename
                for one_filename in files
                if one_filename.startswith(test_name)
            ]

            for one_data_file in test_data_filenames:
                input, expected_result = load_test_data_from_file(
                    join(root, one_data_file)
                )
                fixture_data_list.append([input, expected_result])

    if len(fixture_data_list) > 0:
        metafunc.parametrize(
            ("input", "expected_result"),
            fixture_data_list,
            scope="function"
        )


@fixture
def other_fixture():
    return "blah blah blah"
