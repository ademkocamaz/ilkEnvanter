# Generated by Django 5.1.3 on 2024-12-04 09:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edited', models.DateTimeField(auto_now=True, null=True, verbose_name='Değiştirilme Tarih/Saat')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Oluşturulma Tarih/Saat')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Düzenleyen Kullanıcı')),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entity.base')),
                ('tag', models.CharField(blank=True, max_length=500, null=True, verbose_name='Etiket')),
                ('name', models.CharField(max_length=500, verbose_name='Adı')),
                ('location', models.CharField(blank=True, max_length=500, null=True, verbose_name='Konum')),
                ('manufacturer', models.CharField(blank=True, max_length=500, null=True, verbose_name='Üretici')),
                ('brand', models.CharField(blank=True, max_length=500, null=True, verbose_name='Marka')),
                ('model', models.CharField(blank=True, max_length=500, null=True, verbose_name='Model')),
                ('serial_number', models.CharField(blank=True, max_length=500, null=True, verbose_name='Seri Numarası')),
                ('product_number', models.CharField(blank=True, max_length=500, null=True, verbose_name='Ürün Numarası')),
                ('inventory_number', models.CharField(blank=True, max_length=500, null=True, verbose_name='Stok Numarası')),
                ('used_by', models.CharField(blank=True, max_length=500, null=True, verbose_name='Kullanan Birim / Kullanıcı')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Not')),
            ],
            bases=('entity.base',),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entity.base')),
                ('tag', models.CharField(blank=True, max_length=500, null=True, verbose_name='Etiket')),
                ('name', models.CharField(max_length=500, verbose_name='Adı')),
                ('user_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Kullanıcı Adı')),
                ('password', models.CharField(blank=True, max_length=500, null=True, verbose_name='Şifre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Not')),
            ],
            options={
                'verbose_name': 'Oturum/Giriş Bilgisi',
                'verbose_name_plural': 'Oturum/Giriş Bilgileri',
            },
            bases=('entity.base',),
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Port Adı')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name='Değiştirilme Tarih/Saat')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarih/Saat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Düzenleyen Kullanıcı')),
            ],
            options={
                'verbose_name': 'Port',
                'verbose_name_plural': 'Portlar',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Durum Adı')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name='Değiştirilme Tarih/Saat')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarih/Saat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Düzenleyen Kullanıcı')),
            ],
            options={
                'verbose_name': 'Durum',
                'verbose_name_plural': 'Durumlar',
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entity.entity')),
                ('license_key', models.TextField(blank=True, null=True, verbose_name='Lisans Anahtarı')),
                ('license_start_date', models.DateTimeField(blank=True, null=True, verbose_name='Lisans Başlangıç Tarih / Saat')),
                ('license_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Lisans Bitiş Tarih / Saat')),
            ],
            options={
                'verbose_name': 'Yazılım',
                'verbose_name_plural': 'Yazılımlar',
            },
            bases=('entity.entity',),
        ),
        migrations.AddField(
            model_name='entity',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='entity.status', verbose_name='Durum'),
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entity.entity')),
                ('ports', models.ManyToManyField(to='entity.port', verbose_name='Portlar')),
            ],
            options={
                'verbose_name': 'Bilgisayar',
                'verbose_name_plural': 'Bilgisayarlar',
            },
            bases=('entity.entity',),
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entity.entity')),
                ('ports', models.ManyToManyField(to='entity.port', verbose_name='Portlar')),
            ],
            options={
                'verbose_name': 'Aygıt',
                'verbose_name_plural': 'Aygıtlar',
            },
            bases=('entity.entity',),
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entity.entity')),
                ('size', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Boyut')),
                ('ports', models.ManyToManyField(to='entity.port', verbose_name='Portlar')),
            ],
            options={
                'verbose_name': 'Monitör',
                'verbose_name_plural': 'Monitörler',
            },
            bases=('entity.entity',),
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entity.entity')),
                ('ip_address', models.CharField(blank=True, max_length=500, null=True, verbose_name='IP Adresi')),
                ('ports', models.ManyToManyField(to='entity.port', verbose_name='Portlar')),
            ],
            options={
                'verbose_name': 'Ağ Cihazı',
                'verbose_name_plural': 'Ağ Cihazları',
            },
            bases=('entity.entity',),
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entity.entity')),
                ('ports', models.ManyToManyField(to='entity.port', verbose_name='Portlar')),
            ],
            options={
                'verbose_name': 'Yazıcı',
                'verbose_name_plural': 'Yazıcılar',
            },
            bases=('entity.entity',),
        ),
        migrations.CreateModel(
            name='ComputerSession',
            fields=[
                ('session_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entity.session')),
                ('computer_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity.computer', verbose_name='Bilgisayar')),
            ],
            options={
                'verbose_name': 'Bilgisayar Oturum/Giriş Bilgisi',
                'verbose_name_plural': 'Bilgisayar Oturum/Giriş Bilgileri',
            },
            bases=('entity.session',),
        ),
        migrations.CreateModel(
            name='DeviceSession',
            fields=[
                ('session_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entity.session')),
                ('device_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity.device', verbose_name='Aygıt')),
            ],
            options={
                'verbose_name': 'Aygıt Oturum/Giriş Bilgisi',
                'verbose_name_plural': 'Aygıt Oturum/Giriş Bilgileri',
            },
            bases=('entity.session',),
        ),
        migrations.CreateModel(
            name='NetworkSession',
            fields=[
                ('session_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entity.session')),
                ('network_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity.network', verbose_name='Ağ Cihazı')),
            ],
            options={
                'verbose_name': 'Ağ Cihazı Oturum/Giriş Bilgisi',
                'verbose_name_plural': 'Ağ Cihazı Oturum/Giriş Bilgileri',
            },
            bases=('entity.session',),
        ),
        migrations.CreateModel(
            name='PrinterSession',
            fields=[
                ('session_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entity.session')),
                ('printer_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity.printer', verbose_name='Yazıcı')),
            ],
            options={
                'verbose_name': 'Yazıcı Oturum/Giriş Bilgisi',
                'verbose_name_plural': 'Yazıcı Oturum/Giriş Bilgileri',
            },
            bases=('entity.session',),
        ),
        migrations.CreateModel(
            name='SoftwareSession',
            fields=[
                ('session_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entity.session')),
                ('software_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity.software', verbose_name='Yazılım')),
            ],
            options={
                'verbose_name': 'Yazılım Oturum/Giriş Bilgisi',
                'verbose_name_plural': 'Yazılım Oturum/Giriş Bilgileri',
            },
            bases=('entity.session',),
        ),
    ]
