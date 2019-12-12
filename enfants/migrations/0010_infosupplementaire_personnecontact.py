# Generated by Django 3.0 on 2019-12-12 10:21

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('enfants', '0009_auto_20191212_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonneContact',
            fields=[
                ('personne_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('email', models.EmailField(max_length=250, null=True)),
                ('relation', models.CharField(choices=[('P', 'Père'), ('M', 'Mère'), ('T', 'Tuteur'), ('F', 'Frère'), ('S', 'Soeur'), ('A', 'Autre')], max_length=20)),
                ('autre_relation', models.CharField(max_length=50, null=True)),
                ('enfant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='enfant', to='enfants.Enfant')),
            ],
        ),
        migrations.CreateModel(
            name='InfoSupplementaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_naissance', models.DateTimeField(auto_now_add=True)),
                ('langue', models.CharField(max_length=255, null=True)),
                ('scolarite', models.CharField(choices=[('EO', 'Enseignement ordinaire'), ('ES', 'Enseignement spécialisé'), ('EI', 'Enseignement en intégration')], max_length=50, null=True)),
                ('niveau_scolaire', models.CharField(max_length=255)),
                ('type_enseignement', models.CharField(max_length=255, null=True)),
                ('dominance', models.CharField(choices=[('D', 'Droitier'), ('G', 'Gaucher'), ('AB', 'Ambidextre'), ('AD', 'Adominant')], max_length=10, null=True)),
                ('besoin_particulier', models.CharField(choices=[('DV', 'présente difficultés visuelles'), ('VP', 'ne voit pas'), ('DA', 'présente des difficultés auditives'), ('EP', 'n’entend pas'), ('DCD', 'présente des difficultés pour contrôler avec précision les mouvements de ses bras et mains à droite'), ('DCG', 'présente des difficultés pour contrôler avec précision les mouvements de ses bras et mains à gauche'), ('DCB', 'présente des difficultés pour contrôler avec précision les mouvements de ses bras et mains bilatéral'), ('MD', 'ne peut pas mouvoir ses bras et mains à droite'), ('MG', 'ne peut pas mouvoir ses bras et mains à gauche'), ('MB', 'ne peut pas mouvoir ses bras et mains bilateral'), ('DO', 'présente des difficultés pour s’exprimer oralement'), ('PP', 'ne peut pas parler'), ('DCA', 'présente des difficultés pour comprendre les consignes verbales de l’adulte'), ('DEI', 'présente des difficultés pour comprendre les étapes et/ou les images du jeu'), ('DOE', 'présente des difficultés pour s’orienter dans l’espace du jeu'), ('AU', 'Autre')], max_length=100, null=True)),
                ('autre_besoin_particulier', models.CharField(max_length=255, null=True)),
                ('enfant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='info_enfant', to='enfants.Enfant')),
            ],
        ),
        migrations.RemoveField(
            model_name='InfoSupplementaire',
            name='id',
        ),
    ]
