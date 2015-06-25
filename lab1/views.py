# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from random import randint

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': stat.generate_dict_list(),
                'subjects': [x.name for x in sbj_list],
                'average_subj': [stat.avg_subj(x) for x in stat.all_subj_id()],
                'excellent_students': ', '.join(stat.good_stud()) or 'нет отличников',
                'bad_students': ', '.join(stat.bad_stud()) or 'нет студентов на отчисление'
            }
        )
        return context


class Person(object):
    def __init__(self, fam, name, patr):
        self.fam = unicode(fam, 'UTF-8')  # фамилия
        self.name = unicode(name, 'UTF-8')  # имя
        self.patr = unicode(patr, 'UTF-8')  # отчество

    @property
    def short_name(self):
        return self.fam + ' ' + self.name + ' ' + self.patr

    @property
    def full_name(self):
        return ' '.join([self.fam, self.name, self.patr])


class Student(Person):
    def __init__(self, ID, fam, name, patr, group, age):
        super(Student, self).__init__(fam, name, patr)
        self.ID = ID
        self.group = group
        self.age = age


class Statistics:
    # student_id, [Subjects]
    def __init__(self, scores):
        self.scores = scores

    def name_of(self, student_id, short=False):
        f = lambda s: z.short_name if s else z.full_name
        return [f(short) for z in stud_list if z.ID == student_id].pop()

    def marks_of(self, student_id):
        return [z.value for z in self.scores if z.stud_id == student_id]

    # средняя оценка студента
    def avg_stud(self, student_id):
        l = self.marks_of(student_id)
        return float(sum(l))/len(l)

    # среднее значение оценок по данному предмету
    def avg_subj(self, subject_id):
        l = [z.value for z in self.scores if z.subj_id == subject_id]
        return float(sum(l))/len(l)

    # множество всех id студентов
    def all_id(self):
        return {z.stud_id for z in self.scores}

    # множество всех id предметов
    def all_subj_id(self):
        return {z.subj_id for z in self.scores}

    # список студентов к отчислению
    def bad_stud(self):
        return [self.name_of(z) for z in self.all_id() if self.avg_stud(z) < 3]

    # список успевающих студентов
    def good_stud(self):
        return [self.name_of(z) for z in self.all_id() if self.avg_stud(z) >= 4.7]

    # генерация списка словарей для генерации html-страницы
    def generate_dict_list(self):
        lst = [
            {
                'id': x,
                'fio': self.name_of(x, short=True),
                'marks': self.marks_of(x),
                'average': round(self.avg_stud(x)*100)/100.0
            }
            for x in self.all_id()
        ]
        return lst


class Subject:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = unicode(name, 'UTF-8')


class Score:
    # Subject,
    def __init__(self, stud_id, subj_id, value):
        self.stud_id = stud_id
        self.subj_id = subj_id
        self.value = value



p_list = [
    ('Ахвледиани', 'Николай', 'Филиппович'),
    ('Болдаев', 'Кир', 'Гордеевич'),
    ('Витвинина', 'Варвара', 'Афанасиевна'),
    ('Горностаев', 'Бронислав', 'Миронович'),
    ('Евсеев','Денис', 'Левович'),
    ('Кидина', 'Ольга', 'Тихоновна'),
    ('Лютенков', 'Егор', 'Эмилевич'),
    ('Мальцова', 'Фаина', 'Георгиевна'),
    ('Николаенко', 'Лилия', 'Феликсовна'),
    ('Носачёв', 'Артемий', 'Модестович'),
    ('Пишенин', 'Семён', 'Проклович'),
    ('Суходолина', 'Милена', 'Алексеевна'),
    ('Тамахин', 'Иван', 'Григориевич'),
    ('Ханинов', 'Денис', 'Серафимович'),
    ('Храмов', 'Павел', 'Юриевич'),
    ('Язов', 'Никита', 'Остапович'),
    ]
stud_list = []
for i in range(len(p_list)):
    stud_list.append(Student(i, p_list[i][0], p_list[i][1], p_list[i][2], '723', randint(19,23)))
sbj_list = [
    Subject(0, 'ТиМП'),
    Subject(1, 'ЭиС'),
    Subject(2, 'Философия'),
    Subject(3, 'Ин. язык'),
    Subject(4, 'Физ. культура'),
    Subject(5, 'ТВиМС')
    ]

# Генерация ранодомной хорошей оценки (в среднем)
def good_marks():
    r = randint(1,5)
    if r in [1, 2]: return 5
    elif r in [3, 4]: return 4
    else: return 3

def bad_marks():
    r = randint(1,10)
    if r in [1]: return 5
    elif r in [2]: return 4
    elif r in [3, 4, 5, 6, 7]: return 3
    else: return 2

rand_marks = lambda b: good_marks() if b else bad_marks()
scr_list = [Score(x, y, rand_marks(randint(0, 1))) for x in [a.ID for a in stud_list] for y in [b.ID for b in sbj_list]]
stat = Statistics(scr_list)