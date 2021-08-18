from django.db import models


class Cause(models.Model):
    cause_id = models.IntegerField(primary_key=True)
    description = models.TextField(blank=True, null=True)       
    initial_frequency = models.FloatField(blank=True, null=True)
    event_id = models.IntegerField(blank=True, null=True)
    target_frequency = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cause'


class CauseBarrier(models.Model):
    cause_barrier_id = models.FloatField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    pfd = models.FloatField(blank=True, null=True)
    cause_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cause_barrier'


class Consequence(models.Model):
    consequence_id = models.IntegerField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    initial_frequency = models.FloatField(blank=True, null=True)
    target_frequency = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consequence'


class ConsequenceBarrier(models.Model):
    consequence_barrier_id = models.IntegerField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    pfd = models.FloatField(blank=True, null=True)
    consequence_id = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'consequence_barrier'


class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    cause_id = models.IntegerField(blank=True, null=True)
    consequence_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'
