# Generated by Django 2.2.7 on 2020-06-19 19:55

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import kpi.fields.kpi_uid


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0024_alter_jsonfield_to_jsonbfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100)),
            ],
            options={
                'unique_together': {('name',)},
            },
        ),
        migrations.AlterModelOptions(
            name='asset',
            options={'default_permissions': ('add', 'change', 'delete'), 'ordering': ('-date_modified',), 'permissions': (('view_asset', 'Can view asset'), ('share_asset', "Can change asset's sharing settings"), ('add_submissions', 'Can submit data to asset'), ('view_submissions', 'Can view submitted data for asset'), ('partial_submissions', 'Can make partial actions on submitted data for asset for specific users'), ('change_submissions', 'Can modify submitted data for asset'), ('delete_submissions', 'Can delete submitted data for asset'), ('share_submissions', "Can change sharing settings for asset's submitted data"), ('validate_submissions', 'Can validate submitted data asset'), ('from_kc_only', 'INTERNAL USE ONLY; DO NOT ASSIGN'))},
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'default_permissions': ('add', 'change', 'delete'), 'ordering': ('-date_modified',), 'permissions': (('view_collection', 'Can view collection'), ('share_collection', "Can change this collection's sharing settings"))},
        ),
        migrations.AlterField(
            model_name='asset',
            name='_deployment_data',
            field=jsonfield.fields.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_type',
            field=models.CharField(choices=[('text', 'text'), ('empty', 'empty'), ('question', 'question'), ('block', 'block'), ('survey', 'survey'), ('template', 'template')], default='survey', max_length=20),
        ),
        migrations.AlterField(
            model_name='asset',
            name='content',
            field=jsonfield.fields.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='asset',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='asset',
            name='summary',
            field=jsonfield.fields.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='asset',
            name='uid',
            field=kpi.fields.kpi_uid.KpiUidField(uid_prefix='a'),
        ),
        migrations.AlterField(
            model_name='assetfile',
            name='file_type',
            field=models.CharField(choices=[('map_layer', 'map_layer')], max_length=32),
        ),
        migrations.AlterField(
            model_name='assetfile',
            name='uid',
            field=kpi.fields.kpi_uid.KpiUidField(uid_prefix='af'),
        ),
        migrations.AlterField(
            model_name='assetsnapshot',
            name='details',
            field=jsonfield.fields.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='assetsnapshot',
            name='source',
            field=jsonfield.fields.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='assetsnapshot',
            name='uid',
            field=kpi.fields.kpi_uid.KpiUidField(uid_prefix='s'),
        ),
        migrations.AlterField(
            model_name='assetversion',
            name='uid',
            field=kpi.fields.kpi_uid.KpiUidField(uid_prefix='v'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='collection',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='collection',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='collection',
            name='uid',
            field=kpi.fields.kpi_uid.KpiUidField(uid_prefix='c'),
        ),
        migrations.AlterField(
            model_name='exporttask',
            name='data',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.AlterField(
            model_name='exporttask',
            name='messages',
            field=jsonfield.fields.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='exporttask',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('processing', 'processing'), ('error', 'error'), ('complete', 'complete')], default='created', max_length=32),
        ),
        migrations.AlterField(
            model_name='exporttask',
            name='uid',
            field=kpi.fields.kpi_uid.KpiUidField(uid_prefix='e'),
        ),
        migrations.AlterField(
            model_name='importtask',
            name='data',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.AlterField(
            model_name='importtask',
            name='messages',
            field=jsonfield.fields.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='importtask',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('processing', 'processing'), ('error', 'error'), ('complete', 'complete')], default='created', max_length=32),
        ),
        migrations.AlterField(
            model_name='importtask',
            name='uid',
            field=kpi.fields.kpi_uid.KpiUidField(uid_prefix='i'),
        ),
        migrations.AlterField(
            model_name='objectpermission',
            name='deny',
            field=models.BooleanField(default=False, help_text='Blocks inheritance of this permission when set to True'),
        ),
        migrations.AlterField(
            model_name='objectpermission',
            name='uid',
            field=kpi.fields.kpi_uid.KpiUidField(uid_prefix='p'),
        ),
        migrations.AlterField(
            model_name='taguid',
            name='uid',
            field=kpi.fields.kpi_uid.KpiUidField(uid_prefix='t'),
        ),
        migrations.AlterField(
            model_name='usercollectionsubscription',
            name='uid',
            field=kpi.fields.kpi_uid.KpiUidField(uid_prefix='b'),
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kpi.Region')),
            ],
            options={
                'unique_together': {('name', 'region')},
            },
        ),
        migrations.CreateModel(
            name='Woreda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kpi.Zone')),
            ],
            options={
                'unique_together': {('name', 'zone')},
            },
        ),
        migrations.CreateModel(
            name='Kebele',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100)),
                ('woreda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kpi.Woreda')),
            ],
            options={
                'unique_together': {('name', 'woreda')},
            },
        ),
    ]
