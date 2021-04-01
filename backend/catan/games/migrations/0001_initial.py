# Generated by Django 2.2.7 on 2019-11-19 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winner', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('dice_1', models.IntegerField(default=0)),
                ('dice_2', models.IntegerField(default=0)),
                ('turn_number', models.IntegerField(default=1)),
                ('has_finished', models.BooleanField(default=False)),
                ('robber_has_moved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Hex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.IntegerField(default=0)),
                ('has_robber', models.BooleanField(default=False)),
                ('resource', models.CharField(choices=[('brick', 'brick'), ('lumber', 'lumber'), ('wool', 'wool'), ('grain', 'grain'), ('ore', 'ore')], default=None, max_length=10)),
                ('board', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='games.Board')),
            ],
            options={
                'verbose_name_plural': 'hexes',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('colour', models.CharField(max_length=20)),
                ('development_cards', models.IntegerField(default=0)),
                ('resources_cards', models.IntegerField(default=0)),
                ('victory_points', models.IntegerField(default=0)),
                ('game', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='games.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Vertex_Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('index', models.IntegerField()),
                ('is_available_for_road', models.BooleanField(default=False)),
                ('is_available_for_building', models.BooleanField(default=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('road_building', models.PositiveIntegerField(default=0)),
                ('year_of_plenty', models.PositiveIntegerField(default=0)),
                ('monopoly', models.PositiveIntegerField(default=0)),
                ('victory_point', models.PositiveIntegerField(default=0)),
                ('knight', models.PositiveIntegerField(default=0)),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='games.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('lumber', models.PositiveIntegerField(default=0)),
                ('wool', models.PositiveIntegerField(default=0)),
                ('grain', models.PositiveIntegerField(default=0)),
                ('brick', models.PositiveIntegerField(default=0)),
                ('ore', models.PositiveIntegerField(default=0)),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='games.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Turns3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_turn', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='first3', to='games.Player')),
                ('game', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='games.Game')),
                ('second_turn', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='second3', to='games.Player')),
                ('third_turn', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='third3', to='games.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Turns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_turn', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='first4', to='games.Player')),
                ('fourth_turn', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='fourth4', to='games.Player')),
                ('game', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='games.Game')),
                ('second_turn', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='second4', to='games.Player')),
                ('third_turn', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='third4', to='games.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Hex_Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('index', models.IntegerField()),
                ('hex', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='position', to='games.Hex')),
            ],
        ),
        migrations.CreateModel(
            name='Hex_Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('index', models.IntegerField()),
                ('token', models.IntegerField(default=0)),
                ('has_robber', models.BooleanField(default=False)),
                ('resource', models.CharField(choices=[('brick', 'brick'), ('lumber', 'lumber'), ('wool', 'wool'), ('grain', 'grain'), ('ore', 'ore'), ('desert', 'desert')], default=None, max_length=10)),
                ('game', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='games.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Road',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='road', to='games.Player')),
                ('position1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position1', to='games.Vertex_Game')),
                ('position2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position2', to='games.Vertex_Game')),
            ],
            options={
                'unique_together': {('player', 'position1', 'position2')},
            },
        ),
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('position', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='games.Vertex_Game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='settlements', to='games.Player')),
            ],
            options={
                'unique_together': {('player', 'position')},
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('position', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='games.Vertex_Game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='games.Player')),
            ],
            options={
                'unique_together': {('player', 'position')},
            },
        ),
    ]
