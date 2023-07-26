class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class TestList(TestCase):

    def test_object_constructor(self):
        integer_list = IntegerList(2, 3, 4, "6", [3, 2], {2: "asd"}, 2.34, (2, 3))
        self.assertEqual([2, 3, 4], integer_list.get_data())

    def test_add_element_integer(self):
        integer_list = IntegerList(2, 3, 4)
        integer_list.add(5)
        self.assertEqual([2, 3, 4, 5], integer_list.get_data())

    def test_add_element_not_integer(self):
        integer_list = IntegerList(2, 3, 4)

        with self.assertRaises(ValueError) as valer:
            integer_list.add("5")

        self.assertEqual("Element is not Integer", str(valer.exception))

    def test_remove_index(self):
        integer_list = IntegerList(2, 3, 4)
        removed_index = integer_list.remove_index(1)
        self.assertEqual(3, removed_index)
        self.assertEqual([2, 4], integer_list.get_data())

    def test_remove_invalid_index(self):
        integer_list = IntegerList(2, 3, 4)

        with self.assertRaises(IndexError) as idxer:
            integer_list.remove_index(4)

        self.assertEqual("Index is out of range", str(idxer.exception))

    def test_get_element(self):
        integer_list = IntegerList(2, 3, 4)
        self.assertEqual(3, integer_list.get(1))

    def test_get_element_invalid_idx(self):
        integer_list = IntegerList(2, 3, 4)

        with self.assertRaises(IndexError) as idxer:
            integer_list.get(4)

        self.assertEqual("Index is out of range", str(idxer.exception))

    def test_insert_element(self):
        integer_list = IntegerList(2, 3, 4)
        integer_list.insert(1, 8)
        self.assertEqual([2, 8, 3, 4], integer_list.get_data())

    def test_insert_element_index_error(self):
        integer_list = IntegerList(2, 3, 4)

        with self.assertRaises(IndexError) as idxer:
            integer_list.insert(4, 6)

        self.assertEqual("Index is out of range", str(idxer.exception))

    def test_insert_element_not_integer(self):
        integer_list = IntegerList(2, 3, 4)

        with self.assertRaises(ValueError) as valer:
            integer_list.insert(1, "5")

        self.assertEqual("Element is not Integer", str(valer.exception))

    def test_bigger_value(self):
        integer_list = IntegerList(2, 3, 4)
        self.assertEqual(4, integer_list.get_biggest())

    def test_get_index(self):
        integer_list = IntegerList(2, 3, 4)
        self.assertEqual(1, integer_list.get_index(3))


if __name__ == "__main__":
    main()
