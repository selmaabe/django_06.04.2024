from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myCV', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GeneralSettings',
            new_name='GeneralSetting',
        ),
    ]