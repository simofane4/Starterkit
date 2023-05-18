# Generated by Django 4.1.7 on 2023-05-18 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('MR', 'Monsieur'), ('MISS', 'Mademoiselle'), ('MRS', 'Madame')], default='MR', max_length=4, verbose_name='Civilité')),
                ('first_name', models.CharField(max_length=50, verbose_name='Prénom')),
                ('last_name', models.CharField(max_length=50, verbose_name='Nom')),
                ('address', models.CharField(max_length=255, verbose_name='Adresse')),
                ('additional_address', models.CharField(blank=True, max_length=255, verbose_name="Complément d'adresse")),
                ('city', models.CharField(max_length=50, verbose_name='Ville')),
                ('phone', models.CharField(max_length=10, verbose_name='Téléphone')),
                ('mobilephone', models.CharField(blank=True, max_length=10, verbose_name='Téléphone portable')),
            ],
            options={
                'verbose_name': 'Adresse',
                'verbose_name_plural': 'Adresses',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nom de la catégorie')),
                ('short_desc', models.CharField(blank=True, max_length=150, verbose_name='Description courte')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.category', verbose_name='Catégorie parente')),
            ],
            options={
                'verbose_name': 'Catégorie de produits',
                'verbose_name_plural': 'Catégories de produits',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_invoicing_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_invoicing_address', to='core.address', verbose_name='Adresse de facturation par défaut')),
                ('default_shipping_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_shipping_address', to='core.address', verbose_name='Adresse de livraison par défaut')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur associé')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(auto_now=True, verbose_name='Date de la commande')),
                ('shipping_date', models.DateField(null=True, verbose_name="Date de l'expédition")),
                ('status', models.CharField(choices=[('W', 'En attente de validation'), ('P', 'Payée'), ('S', 'Expédiée'), ('C', 'Annulée')], default='W', max_length=1, verbose_name='Statut de la commande')),
                ('stripe_charge_id', models.CharField(blank=True, max_length=30, verbose_name='Identifiant de transaction Stripe')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client', verbose_name='Client ayant passé commande')),
                ('invoicing_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_invoicing_address', to='core.address', verbose_name='Adresse de facturation')),
                ('shipping_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_shipping_address', to='core.address', verbose_name='Adresse de livraison')),
            ],
            options={
                'verbose_name': 'Commande',
                'verbose_name_plural': 'Commandes',
            },
        ),
        migrations.CreateModel(
            name='TagDict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='VAT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.FloatField(verbose_name='Taux de TVA (décimal)')),
            ],
            options={
                'verbose_name': 'Taux de TVA',
                'verbose_name_plural': 'Taux de TVA',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, default='default.jpeg', null=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nom du produit')),
                ('short_desc', models.CharField(max_length=150, verbose_name='Description courte')),
                ('long_desc', models.TextField(verbose_name='Description longue')),
                ('price', models.FloatField(verbose_name='Prix HT du produit')),
                ('thumbnail', models.ImageField(null=True, upload_to='commerce/media', verbose_name='Miniature du produit')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category', verbose_name='Catégorie du produit')),
                ('vat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vat', verbose_name='Taux de TVA')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('read_count', models.IntegerField(default=0, editable=False)),
                ('read_time', models.IntegerField(default=0, editable=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='commerce/media')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(verbose_name='Quantité')),
                ('product_unit_price', models.FloatField(verbose_name='Prix unitaire du produit')),
                ('vat', models.FloatField(verbose_name='Taux de TVA')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order', verbose_name='Commande associée')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
            options={
                'verbose_name': "Ligne d'une commande",
                'verbose_name_plural': 'Lignes de commandes',
            },
        ),
        migrations.CreateModel(
            name='FavouritePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posts', models.ManyToManyField(to='core.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='core.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.post')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='CartLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
            options={
                'verbose_name': "Ligne d'un panier client",
                'verbose_name_plural': "Lignes d'un panier client",
            },
        ),
        migrations.AddField(
            model_name='address',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client'),
        ),
    ]