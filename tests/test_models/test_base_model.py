#!/usr/bin/python3
""" Module for testing base model"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Testing BaseModel functionality """

    def setUp(self):
        """Set up for testing"""
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def tearDown(self):
        """Tear down/clean up after testing"""
        del self.bm1
        del self.bm2

    def test_id(self):
        """Test id"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_at(self):
        """Test created_at"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_updated_at(self):
        """Test updated_at"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)

    def test_str(self):
        """Test str"""
        bm1 = BaseModel()
        str_output = str(bm1)
        self.assertIn(f"[BaseModel] ({bm1.id})", str_output)
        self.assertIn("'id':", str_output)
        self.assertIn("'created_at':", str_output)
        self.assertIn("'updated_at':", str_output)

    def test_save(self):
        """Test save"""
        bm1 = BaseModel()
        bm1.save()
        self.assertNotEqual(bm1.created_at, bm1.updated_at)

    def test_to_dict(self):
        """Test to_dict"""
        bm1 = BaseModel()
        bm1_dict = bm1.to_dict()
        self.assertEqual(bm1_dict['__class__'], 'BaseModel')
        self.assertEqual(bm1_dict['created_at'],
                         bm1.created_at.isoformat())
        self.assertEqual(bm1_dict['updated_at'],
                         bm1.updated_at.isoformat())

    def test_kwargs(self):
        """Test kwargs"""
        bm1 = BaseModel()
        bm1.save()
        bm1_dict = bm1.to_dict()
        bm2 = BaseModel(**bm1_dict)
        self.assertEqual(bm1.id, bm2.id)
        self.assertEqual(bm1.created_at, bm2.created_at)
        self.assertEqual(bm1.updated_at, bm2.updated_at)
        self.assertEqual(bm1.__dict__, bm2.__dict__)


if __name__ == '__main__':
    unittest.main()
