from django.db import models


class Answer(models.Model):
    id_answer = models.AutoField(primary_key=True)
    value = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'answer'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Question(models.Model):
    id_question = models.AutoField(primary_key=True)
    question = models.CharField(max_length=45)
    right_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, db_column='right_answer')

    class Meta:
        managed = False
        db_table = 'question'


class QuestionAnswer(models.Model):
    id_questionanswer = models.AutoField(primary_key=True)
    id_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, db_column='id_answer')
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE, db_column='id_question')

    class Meta:
        managed = False
        db_table = 'question_answer'
        unique_together = (('id_questionanswer', 'id_answer', 'id_question'),)


class Test(models.Model):
    id_test = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


class TestQuestion(models.Model):
    id_testquestion = models.AutoField(primary_key=True)
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE, db_column='id_question')
    id_test = models.ForeignKey(Test,on_delete=models.CASCADE, db_column='id_test')

    class Meta:
        managed = False
        db_table = 'test_question'
        unique_together = (('id_testquestion', 'id_question', 'id_test'),)


class TestResult(models.Model):
    id_test_result = models.AutoField(primary_key=True)
    id_user = models.ForeignKey('User', on_delete=models.CASCADE, db_column='id_user')
    id_test = models.ForeignKey(Test, on_delete=models.CASCADE, db_column='id_test')
    status = models.CharField(max_length=12)
    date_start = models.DateTimeField()
    right_answer = models.FloatField()
    result_comment = models.CharField(max_length=255, blank=True, null=True)
    date_complete = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'test_result'
        unique_together = (('id_test_result', 'id_user', 'id_test'),)


class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    patronymic = models.CharField(max_length=45, blank=True, null=True)
    login = models.CharField(unique=True, max_length=45)
    password = models.CharField(unique=True, max_length=45)
    date_registration = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user'
