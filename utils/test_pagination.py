from unittest import TestCase
from utils.pagination import make_pagination_range

class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range = list(range(1, 21)),
            qty_pages = 4,
            current_page = 1,
        )['pagination']
        self.assertEqual([1,2,3,4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):
        pagination = make_pagination_range(
            page_range = list(range(1, 21)),
            qty_pages = 4,
            current_page = 1,
        )['pagination']
        self.assertEqual([1,2,3,4], pagination)

        pagination = make_pagination_range(
            page_range = list(range(1, 21)),
            qty_pages = 4,
            current_page = 2,
        )['pagination']
        self.assertEqual([1,2,3,4], pagination)

        pagination = make_pagination_range(
            page_range = list(range(1, 21)),
            qty_pages = 4,
            current_page = 3,
        )['pagination']
        self.assertEqual([2,3,4,5], pagination)

    def test_make_sure_middle_ranges_are_correct(self):
        pagination = make_pagination_range(
            page_range = list(range(1, 21)),
            qty_pages = 4,
            current_page = 10,
        )['pagination']
        self.assertEqual([9,10,11,12], pagination)

    def test_last_range_is_static_if_the_last_page_range_is_the_last_page(self):
        pagination = make_pagination_range(
            page_range = list(range(1, 21)),
            qty_pages = 4,
            current_page = 18,
        )['pagination']
        self.assertEqual([17,18,19,20], pagination)