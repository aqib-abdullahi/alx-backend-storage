#!/usr/bin/env python3
"""lists top students
"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """returns the top students by average score
    """
    students = mongo_collection.find()
    top_students = []

    for student in students:
        topics = student.get('topics', [])
        total_score = 0
        topic_count = 0

        for topic in topics:
            total_score += topic.get('score', 0)
            topic_count += 1

        if topic_count > 0:
            average_score = total_score / topic_count
            student['averageScore'] = average_score
            top_students.append(student)

    top_students = sorted(top_students,
                          key=lambda x: x['averageScore'],
                          reverse=True)
    return top_students
