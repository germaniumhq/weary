import unittest

import weary


@weary.model
class DataStore:
    def __init__(self, data):
        self.data = data

    @weary.property
    def data_count(self) -> str:
        ...

    @weary.property
    def not_implemented(self) -> None:
        ...


@weary.implementation(DataStore, "data_count")
def data_store_data_count_implementation(self, context):
    return len(self.data)


class WutTest(unittest.TestCase):
    def test_custom_constructor(self):
        ds = DataStore(data=[1, 2, 3, 4])
        self.assertEquals(4, ds.data_count)

    @unittest.expectedFailure
    def test_not_implemented_methdo(self):
        ds = DataStore(data="")
        ds.not_implemented


if __name__ == "__main__":
    unittest.main()
