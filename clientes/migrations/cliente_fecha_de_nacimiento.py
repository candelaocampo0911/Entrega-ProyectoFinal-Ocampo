
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='fechaNacimiento',
            field=models.DateField(null=True),
        ),
    ]