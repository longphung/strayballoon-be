# Generated by Django 3.2.15 on 2022-10-21 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20221021_1212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classroomstudents',
            old_name='class_room_ids',
            new_name='class_room_id',
        ),
        migrations.RenameField(
            model_name='classroomstudents',
            old_name='student_ids',
            new_name='student_id',
        ),
        migrations.RemoveField(
            model_name='session',
            name='questions',
        ),
        migrations.AddField(
            model_name='sessionprogress',
            name='student_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='classroomstudents',
            unique_together={('student_id', 'class_room_id')},
        ),
        migrations.AlterUniqueTogether(
            name='sessionprogress',
            unique_together={('student_id', 'session_id')},
        ),
        migrations.RemoveField(
            model_name='sessionprogress',
            name='student_ids',
        ),
        migrations.CreateModel(
            name='SessionsQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.question')),
                ('session_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.session')),
            ],
            options={
                'unique_together': {('session_id', 'question_id')},
            },
        ),
    ]
