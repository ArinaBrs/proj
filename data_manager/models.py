# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class IncomingFiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    filename = models.CharField(max_length=100)
    uploaded_date = models.DateTimeField()
    status = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'incoming_files'


class Indicators(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    xls_filename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicators'
        unique_together = (('code', 'xls_filename'),)


class MappingXlsPeriod(models.Model):
    id = models.BigIntegerField(primary_key=True)
    xls_filename = models.CharField(max_length=100)
    xls_value_year = models.CharField(max_length=32)
    xls_value = models.CharField(max_length=100)
    period = models.ForeignKey('Periods', models.DO_NOTHING, blank=True, null=True)
    date_value = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mapping_xls_period'
        unique_together = (('xls_filename', 'xls_value_year', 'xls_value'),)

class Logging(models.Model):
    created_at_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField()
    priority = models.TextField()

    class Meta:
        managed = False
        db_table = 'logging'

class MappingXlsRegion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    xls_filename = models.CharField(max_length=100)
    xls_value = models.CharField(max_length=100)
    region = models.ForeignKey('Regions', models.DO_NOTHING, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mapping_xls_region'
        unique_together = (('xls_filename', 'xls_value', 'region'),)


class Periods(models.Model):
    id = models.BigIntegerField(primary_key=True)
    value = models.DateField(unique=True)
    value_label = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'periods'


class RegionPeriodIndicators(models.Model):
    id = models.BigAutoField(primary_key=True)
    region = models.ForeignKey('Regions', models.DO_NOTHING)
    indicator = models.ForeignKey(Indicators, models.DO_NOTHING)
    period = models.ForeignKey(Periods, models.DO_NOTHING)
    value = models.FloatField(blank=True, null=True)
    file = models.ForeignKey(IncomingFiles, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'region_period_indicators'
        unique_together = (('region', 'indicator', 'period', 'file'),)

class Regions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    code = models.CharField(unique=True, max_length=32, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    par = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    region_type = models.CharField(max_length=32, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
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
    action_flag = models.SmallIntegerField()
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


class Rules(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    description_log = models.TextField()
    flag = models.BooleanField()
    code = models.TextField()

    class Meta:
        managed = False
        db_table = 'rules'


class RulesChecking(models.Model):
    rule = models.ForeignKey(Rules, models.DO_NOTHING)
    region = models.ForeignKey(Regions, models.DO_NOTHING)
    indicator = models.ForeignKey(Indicators, models.DO_NOTHING)
    period = models.ForeignKey(Periods, models.DO_NOTHING)
    status = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rules_checking'