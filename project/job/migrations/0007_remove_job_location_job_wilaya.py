# Generated by Django 5.0.2 on 2024-03-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_category_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='location',
        ),
        migrations.AddField(
            model_name='job',
            name='Wilaya',
            field=models.CharField(blank=True, choices=[('Adrar', 'Adrar'), ('Chlef', 'Chlef'), ('Laghouat', 'Laghouat'), ('Oum El Bouaghi', 'Oum El Bouaghi'), ('Batna', 'Batna'), ('Béjaïa', 'Béjaïa'), ('Biskra', 'Biskra'), ('Béchar', 'Béchar'), ('Blida', 'Blida'), ('Bouira', 'Bouira'), ('Tamanrasset', 'Tamanrasset'), ('Tébessa', 'Tébessa'), ('Tlemcen', 'Tlemcen'), ('Tiaret', 'Tiaret'), ('Tizi Ouzou', 'Tizi Ouzou'), ('Alger', 'Alger'), ('Djelfa', 'Djelfa'), ('Jijel', 'Jijel'), ('Sétif', 'Sétif'), ('Saïda', 'Saïda'), ('Skikda', 'Skikda'), ('Sidi Bel Abbès', 'Sidi Bel Abbès'), ('Annaba', 'Annaba'), ('Guelma', 'Guelma'), ('Constantine', 'Constantine'), ('Médéa', 'Médéa'), ('Mostaganem', 'Mostaganem'), ("M'Sila", "M'Sila"), ('Mascara', 'Mascara'), ('Ouargla', 'Ouargla'), ('Oran', 'Oran'), ('El Bayadh', 'El Bayadh'), ('Illizi', 'Illizi'), ('Bordj Bou Arréridj', 'Bordj Bou Arréridj'), ('Boumerdès', 'Boumerdès'), ('El Tarf', 'El Tarf'), ('Tindouf', 'Tindouf'), ('Tissemsilt', 'Tissemsilt'), ('El Oued', 'El Oued'), ('Khenchela', 'Khenchela'), ('Souk Ahras', 'Souk Ahras'), ('Tipaza', 'Tipaza'), ('Mila', 'Mila'), ('Aïn Defla', 'Aïn Defla'), ('Naâma', 'Naâma'), ('Aïn Témouchent', 'Aïn Témouchent'), ('Ghardaïa', 'Ghardaïa'), ('Relizane', 'Relizane')], max_length=100, null=True),
        ),
    ]