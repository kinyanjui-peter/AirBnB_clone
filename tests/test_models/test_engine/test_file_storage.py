#!/usr/bin/python3

"""storage of file for testing"""

import unittest
import models
import os
import datetime

class FileStorage(unittest.TestCase):
    """  """
    def test_docstring(self):
        #checks the presence of doc string
        self.assertTrue(len(FileStorage.all.__doc__) > 1)

    def tearDown(self):
        """ remove json file """
        if os.path.exists(self.filepath):
            os.remove(self.linpath)

        if os.path.exists('test_storage'):
            os.rename('test_sotorage', self.filepathi)
    
    def reload(self):
        Storage = FileStorage()
        try:
            os.remove(file.json)
        except:
            pass
        with open("file.json","w") as FILE:
            FILE.write("{}")
        with open("file.json","r") as FILE:
            for item in FILE:
                self.assertEqual(item, "{}")
            self.assertIs(Storage.reload(), None)
     

