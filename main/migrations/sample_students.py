from django.db import migrations

STUDENTS = [
    ('Juan', 'Dela Cruz', 20, 'BS Information Technology', 'juan@example.com'),
    ('Maria', 'Santos', 19, 'BS Computer Science', 'maria@example.com'),
    ('Jose', 'Reyes', 21, 'BS Information Systems', 'jose@example.com'),
    ('Maria', 'Santos', 20, 'BS Information Technology', 'maria@example.com'),
    ('Carlos', 'Dela Cruz', 22, 'BS Accountancy', 'carlos@example.com'),
    ('Angela', 'Garcia', 19, 'BS Entrepreneurship', 'angela@example.com'),
    ('Mark', 'Villanueva', 21, 'BS Social Work', 'mark@example.com'),
    ('Sofia', 'Mendoza', 20, 'BS Public Administration', 'sofia@example.com'),
    ('Daniel', 'Bautista', 23, 'BS Information Systems', 'daniel@example.com'),
    ('Andrea', 'Navarro', 21, 'BA English Language Studies', 'andrea@example.com'),
    ('Joshua', 'Fernandez', 22, 'BS Accounting Information System', 'joshua@example.com'),
    ('Patricia', 'Ramos', 19, 'Bachelor of Technical Vocational Teachers Education', 'patricia@example.com'),
]


def add_students(apps, schema_editor):
    Student = apps.get_model('main', 'Student')
    Student.objects.bulk_create([
        Student(first_name=f, last_name=l, age=a, course=c, email=e)
        for f, l, a, c, e in STUDENTS
    ])


def remove_students(apps, schema_editor):
    Student = apps.get_model('main', 'Student')
    Student.objects.filter(email__in=[s[4] for s in STUDENTS]).delete()


class Migration(migrations.Migration):

    dependencies = [('main', 'initial')]

    operations = [migrations.RunPython(add_students, remove_students)]
