from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0002_writings_is_liked'),
    ]

    operations = [
        migrations.RunSQL(
            ('CREATE FULLTEXT INDEX content_fulltext_index ON writings_writings (content)',),
            ('DROP INDEX content_fulltext_index on writings_writings',)
        )
    ]