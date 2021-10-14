import sys
import pytest
from src import *
from unittest import mock
from unittest.mock import patch
from io import StringIO

doc_numbers = [
    ("2207 876234", True),
    ("11-2", True),
    ("10006", True),
    ("876234", False),
    ("245 43645", False),
    ("11-110", False),
    ("", False)
]

class Test_check_document_existance:

    @classmethod
    def setup_class(cls):
        print("setup_class")

    def setup(self):
        print("setup")

    @pytest.mark.parametrize('user_doc_numbers, existance', doc_numbers)
    def test_check_document_existance_true(self, user_doc_numbers, existance):
        assert check_document_existance(user_doc_numbers) == existance

    def tearDown(self):
        print("teardown")

    @classmethod
    def tearDown_class(cls):
        print("tearDown_class")

class Test_get_doc_owner_name:

    @classmethod
    def setup_class(cls):
        print("setup_class")

    def setup(self):
        print("setup")

    @patch("builtins.input", return_value="11-2")
    def test_get_doc_owner_name_one(self, author):
        assert get_doc_owner_name() == "Геннадий Покемонов"

    @patch("builtins.input", return_value="2207 876234")
    def test_get_doc_owner_name_two(self, author):
        assert get_doc_owner_name() == "Василий Гупкин"

    @patch("builtins.input", return_value="10006")
    def test_get_doc_owner_name_three(self, author):
        assert get_doc_owner_name() == "Аристарх Павлов"

    @patch("builtins.input", return_value="1006")
    def test_get_doc_owner_name_four(self, author):
        assert get_doc_owner_name() == None

    @patch("builtins.input", return_value="")
    def test_get_doc_owner_name_five(self, author):
        assert get_doc_owner_name() == None

    def tearDown(self):
        print("teardown")

    @classmethod
    def tearDown_class(cls):
        print("tearDown_class")

docs = [("2207 876234", None),
    ("11-2", None),
    ("10006", None)]

class Test_remove_doc_from_shelf:

    @classmethod
    def setup_class(cls):
        print("setup_class")

    def setup(self):
        print("setup")

    @pytest.mark.parametrize('user_doc_numbers, existance', docs)
    def test_remove_doc_from_shelf(self, user_doc_numbers, existance):
        assert remove_doc_from_shelf(user_doc_numbers) == existance

    def tearDown(self):
        print("teardown")

    @classmethod
    def tearDown_class(cls):
        print("tearDown_class")

class Test_delete_doc:

    @classmethod
    def setup_class(cls):
        print("setup_class")

    def setup(self):
        print("setup")

    @patch("builtins.input", return_value="11-2")
    def test_delete_doc_first(self, datas):
        assert add_new_shelf() == ("11-2", True)

    @patch("builtins.input", return_value="10006")
    def test_delete_doc_second(self, datas):
        assert add_new_shelf() == ("10006", True)

    @patch("builtins.input", return_value="106")
    def test_delete_doc_second_third(self, datas):
        assert check_document_existance("106") == (False)

    def tearDown(self):
        print("teardown")

    @classmethod
    def tearDown_class(cls):
        print("tearDown_class")

class Test_get_doc_shelf:

    @classmethod
    def setup_class(cls):
        print("setup_class")

    def setup(self):
        print("setup")

    @patch("builtins.input", return_value="10006")
    def test_get_doc_shelf_one(self, datas):
        assert get_doc_shelf() == ("2")

    @patch("builtins.input", return_value="11-2")
    def test_get_doc_shelf_two(self, datas):
        assert get_doc_shelf() == ("1")

    def tearDown(self):
        print("teardown")

    @classmethod
    def tearDown_class(cls):
        print("tearDown_class")

class Test_move_doc_to_shelf:

    @classmethod
    def setup_class(cls):
        print("setup_class")

    def setup(self):
        print("setup")

    def test_move_doc_to_shelf_one(self):
        with mock.patch("builtins.input", side_effect=["11-2", "2"]):
            assert move_doc_to_shelf() == ('Документ номер "11-2" был перемещен на полку номер "2"')

    def test_move_doc_to_shelf_two(self):
        with mock.patch("builtins.input", side_effect=["10006", "3"]):
            assert move_doc_to_shelf() == ('Документ номер "10006" был перемещен на полку номер "3"')

    def test_move_doc_to_shelf_three(self):
        with mock.patch("builtins.input", side_effect=["2207 876234", "3"]):
            assert move_doc_to_shelf() == ('Документ номер "2207 876234" был перемещен на полку номер "3"')

    def tearDown(self):
        print("teardown")

    @classmethod
    def tearDown_class(cls):
        print("tearDown_class")


class Test_add_new_doc:

    @classmethod
    def setup_class(cls):
        print("setup_class")

    def setup(self):
        print("setup")

    def test_add_new_doc_one(self):
        with mock.patch("builtins.input", side_effect=["12424", "passport", "Nastya Filippova", "1"]):
            assert add_new_doc() == "1"

    def test_add_new_doc_one(self):
        with mock.patch("builtins.input", side_effect=["563", "passport", "Alex Petrov", "3"]):
            assert add_new_doc() == "3"

    def tearDown(self):
        print("teardown")

    @classmethod
    def tearDown_class(cls):
        print("tearDown_class")