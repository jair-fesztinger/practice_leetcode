import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    student_subject_pairs = students[['student_id', 'student_name']].merge(subjects, how = 'cross')
    exams_count = examinations.groupby(['student_id', 'subject_name'], as_index=False).agg(
        attended_exams = ('subject_name', 'count')
    )
    grouped_1 = pd.merge(student_subject_pairs, exams_count, how = 'left', on = ['student_id', 'subject_name'])
    grouped_1['attended_exams'] = grouped_1['attended_exams'].fillna(0).astype(int)

    grouped_1 = grouped_1.sort_values(by = ['student_id', 'subject_name']).reset_index(drop=True)

    return grouped_1