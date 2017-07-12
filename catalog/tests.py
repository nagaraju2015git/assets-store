from django.test import TestCase
from .models import Asset, AssetClass

# Create your tests here.
class AssetsTestCase(TestCase):
    def setUp(self):
        self.asset_name = "TestCase_2"
        self.asset_type = "S"
        self.asset_class = AssetClass.objects.get(acclass="rapideye")
        self.assets = Asset(self.asset_name, self.asset_type, self.asset_class)

    def test_model_can_create_a_asset(self):
        old_count = Asset.objects.count()
        self.assets.save()
        new_count = Asset.objects.count()
        self.assertNotEqual(old_count, new_count)
