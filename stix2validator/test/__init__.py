import unittest
import os
from .. import validate_string
from ..validators import ValidationOptions

SCHEMA_DIR = os.path.abspath(os.path.dirname(__file__) + "../../schemas")


class ValidatorTest(unittest.TestCase):
    options = ValidationOptions(schema_dir=SCHEMA_DIR)

    def check_ignore(self, instance, code):
        """Test that the given instance is valid if the given check is ignored.

        Args:
            instance: The JSON string to be validated.
            error: The numerical code of the check to be ignored.
        """
        self.assertTrueWithOptions(instance, ignored=code)

    def assertTrueWithOptions(self, instance, **kwargs):
        """Test that the given instance is valid when using the validation
        options provided by kwargs.

        Args:
            instance: The JSON string to be validated.
            kwargs: Any number of keyword arguments to be passed to the
                    ValidationOptions constructor.
        """
        options = ValidationOptions(schema_dir=SCHEMA_DIR, **kwargs)
        results = validate_string(instance, options)
        self.assertTrue(results.is_valid)

    def assertFalseWithOptions(self, instance, **kwargs):
        """Test that the given instance is NOT valid when using the validation
        options provided by kwargs.

        Args:
            instance: The JSON string to be validated.
            kwargs: Any number of keyword arguments to be passed to the
                    ValidationOptions constructor.
        """
        options = ValidationOptions(schema_dir=SCHEMA_DIR, **kwargs)
        results = validate_string(instance, options)
        self.assertEqual(results.is_valid, False)
