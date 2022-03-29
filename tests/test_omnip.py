import unittest
import decoupler as dc
import pandas as pd


class TestOmnipath(unittest.TestCase):

    def test_showresources(self):
        lst = dc.show_resources()
        self.assertTrue(type(lst) is list)
        self.assertTrue(len(lst) > 0)

    def test_getresource(self):
        res = dc.get_resource('TFcensus')
        self.assertTrue(type(res) is pd.DataFrame)
        self.assertTrue(res.shape[0] > 0)

    def test_getprogeny_human(self):
        n = 100
        df = dc.get_progeny(organism='human', top=n)
        n_paths = len(df['source'].unique())
        n_rows = (n_paths * 100)
        self.assertTrue(type(df) is pd.DataFrame)
        self.assertTrue(df.shape[0] == n_rows)

    def test_getprogeny_mouse(self):
        n = 100
        df = dc.get_progeny(organism='mouse', top=n)
        n_paths = len(df['source'].unique())
        n_rows = (n_paths * 100)
        self.assertTrue(type(df) is pd.DataFrame)
        self.assertTrue(df.shape[0] == n_rows)

    def test_getdorothea_human(self):
        df = dc.get_dorothea(organism='human')
        self.assertTrue(type(df) is pd.DataFrame)
        self.assertTrue(df.shape[0] > 0)

    def test_getdorothea_mouse(self):
        df = dc.get_dorothea(organism='mouse')
        self.assertTrue(type(df) is pd.DataFrame)
        self.assertTrue(df.shape[0] > 0)
