import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertIsNotNone(obj1.id)
        self.assertIsNotNone(obj2.id)
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertIsInstance(obj1.created_at, datetime.datetime)
        self.assertIsInstance(obj1.updated_at, datetime.datetime)
        self.assertNotEqual(obj1.created_at, obj1.updated_at)

    def test_str(self):
        obj = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected_str)

    def test_save(self):
        obj = BaseModel()
        created_at_before_save = obj.created_at
        updated_at_before_save = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, updated_at_before_save)
        self.assertEqual(obj.created_at, created_at_before_save)

    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
