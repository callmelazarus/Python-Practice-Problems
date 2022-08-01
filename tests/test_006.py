from unittest import TestCase
from problems.problem_006 import can_skydive


class ProblemTests(TestCase):
    def test_can_skydive_because_old_enough(self):
        value = can_skydive(20, False)
        self.assertTrue(value is True)

    def test_can_skydive_because_has_consent_form(self):
        value = can_skydive(16, True)
        self.assertTrue(value is True)

    def test_cannot_skydive_because_they_are_too_young_and_have_no_consent(
        self,
    ):
        value = can_skydive(16, False)
        self.assertTrue(value is False)
