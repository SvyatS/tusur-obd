from django.db import models


class Teacher(models.Model):
    """модель преподавателя"""

    fio = models.CharField(max_length=256)
    adress = models.CharField(max_length=256)
    phone = models.CharField(max_length=64)
    #department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.fio)
  
    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class Department(models.Model):
    """модель кафедры"""

    name_department = models.CharField(max_length=256)
    manager = models.OneToOneField(Teacher, on_delete = models.CASCADE, primary_key = True)
    #faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name_department)
    
    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"



class Faculty(models.Model):
    """модель факультета"""

    name_faculty = models.CharField(max_length=256)
    dekan = models.OneToOneField(Teacher, on_delete = models.CASCADE, primary_key = True)
    num_of_learners = models.IntegerField('количество обучающихся')

    def __str__(self):
        return str(self.name_faculty)
    
    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"


class Group(models.Model):
    """модель группы"""

    name_group = models.CharField(max_length=32)
    num_of_learners = models.IntegerField('количество учащихся')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name_group)
    
    class Meta:
        verbose_name = "Группы"
        verbose_name_plural = "Группы"

        
class Student(models.Model):
    """модель студента"""

    fio = models.CharField(max_length=256)
    record_book = models.IntegerField('номер зачетной книжки')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}: {1}".format(self.fio, self.group.name_group[:10])
    
    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class Lesson(models.Model):
    """модель расписания/урок"""

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name_of_lesson = models.CharField(max_length=64)
    room = models.CharField(max_length=32)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{0}: {1}".format(self.name_of_lesson, self.room)
    
    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"


class Rating(models.Model):
    """модель оценки за урок"""

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    rating = models.IntegerField('оценка')

    def __str__(self):
        return "{0}: {1}".format(self.student.fio, self.rating)
    
    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"






