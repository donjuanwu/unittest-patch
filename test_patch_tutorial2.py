"""
Lesson 1: patch
Video: https://canvas.uw.edu/courses/1608479/pages/lesson-01-content-part-12-more-on-linting-mocks-and-patching?module_item_id=16955510

Notes:
    below commands must be executed in git bash terminal

install coverage
> pip install coverage

install pylint
> pip install pylint

create .pylintrc (in root directory)
> pylint --generate-rcfile > .pylintrc

create requirements.txt (in root directory)
> add coverage, pylint and mock

Run Unittest CLI:
> python -m unittest test_patch_tutorial2.py

Run test coverage and unittest CLI:
> python -m coverage run --include=patch_tutorial2.py -m unittest test_patch_tutorial2.py

Generate coverage report
> python -m coverage report

Generate coverage html report
> python -m coverage html    # a new folder called 'htmlcov' got created with an index.html
"""

from unittest import TestCase
import queue
from mock import patch
import patch_tutorial2 as PT2


class TestPatchTutorial2(TestCase):
    """
    test patch tutorial 2
    """

    def test_get_current_temperate_all(self):
        """
        use patch to override temperature_sensor.read_temperature
        use tuple to hold values and assigned it to side_effect
        :return:
        """
        expected_queue = queue.Queue()
        expected_queue.put("Nice weather, 75F!")
        expected_queue.put("Rough weather, 10F!")
        responses = (75, 10, -1)
        with patch('patch_tutorial2.temperature_sensor.read_temperature', side_effect=responses):
            self.assertEqual(PT2.get_current_temperature(), expected_queue.get())
            self.assertEqual(PT2.get_current_temperature(), expected_queue.get())
            with self.assertRaises(SystemError):
                PT2.get_current_temperature()
