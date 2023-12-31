import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Testing File Storage functionality """

    def setUp(self):
        self.fs = FileStorage()
        self.fs1 = FileStorage()
        self.obj = BaseModel()

    def tearDown(self):
        """Reset FileStorage and delete the file.json after each test"""
        FileStorage._FileStorage__objects = {}  # Reset objects
        if os.path.exists("file.json"):
            os.remove("file.json")  # Delete the file.json

    def test_all(self):
        """Test all"""
        fs2 = FileStorage()
        self.assertEqual(self.fs.all(), self.fs1.all(), fs2.all())

    def test_new(self):
        """Test new"""
        bm1 = BaseModel()
        self.fs.new(bm1)
        key = self.obj.__class__.__name__ + "." + self.obj.id
        self.assertIn(f'BaseModel.{bm1.id}', self.fs.all())
        self.assertIn(key, self.fs1.all())

    def test_save(self):
        """Test save"""
        bm2 = BaseModel()
        self.fs.new(bm2)  # Add object to storage
        self.fs.save()  # Save the object
        with open('file.json', 'r') as f:
            self.assertIn(f'BaseModel.{bm2.id}', f.read())

    def test_reload(self):
        """Test reload method"""
        self.fs1.new(self.obj)
        self.fs1.save()
        self.fs1._FileStorage__objects = {}
        self.fs1.reload()
        key = self.obj.__class__.__name__ + "." + self.obj.id
        self.assertIn(key, self.fs1.all())


if __name__ == '__main__':
    unittest.main()
