from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def test_object_init(self):
        student = Student("George")
        self.assertEqual("George", student.name)
        self.assertEqual({}, student.courses)

    def test_enroll_and_add_notes_to_existing_course(self):
        student = Student("George", {"math": ["notes"]})

        result = student.enroll("math", ["added_notes"])
        self.assertEqual({"math": ["notes", "added_notes"]}, student.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_add_notes_and_course(self):
        student = Student("George")

        self.assertEqual({}, student.courses)

        result = student.enroll("math", ["added_notes"])
        self.assertEqual({"math": ["added_notes"]}, student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_add_notes_and_course_with_Y(self):
        student = Student("George")

        self.assertEqual({}, student.courses)

        result = student.enroll("math", ["added_notes"],"Y")
        self.assertEqual({"math": ["added_notes"]}, student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_add_course_no_notes(self):
        student = Student("George")

        self.assertEqual({}, student.courses)

        result = student.enroll("math", ["added_notes"], "N")
        self.assertEqual({"math": []}, student.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes(self):
        student = Student("George", {"math": ["notes"]})

        self.assertEqual({"math": ["notes"]}, student.courses)
        result = student.add_notes("math", "new_note")

        self.assertEqual({"math": ["notes", "new_note"]}, student.courses)
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_error(self):
        student = Student("George")

        with self.assertRaises(Exception) as ex:
            student.add_notes("math", "new_note")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertEqual({}, student.courses)

    def test_leave_course(self):
        student = Student("George", {"math": ["notes"]})

        result = student.leave_course("math")
        self.assertEqual({}, student.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_error(self):
        student = Student("George")

        with self.assertRaises(Exception) as ex:
            student.leave_course("math")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

