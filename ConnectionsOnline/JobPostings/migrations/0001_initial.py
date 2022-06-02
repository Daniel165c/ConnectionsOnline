from django.db import migrations, models


class Migrations(migrations.Migration):

    initial: True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=))
            ]
        )

    ]