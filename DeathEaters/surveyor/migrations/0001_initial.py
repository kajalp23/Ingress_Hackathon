# Generated by Django 3.1.5 on 2021-02-13 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BuildingNo', models.CharField(max_length=10)),
                ('CensusHouseNo', models.CharField(max_length=4)),
                ('FloorMaterial', models.CharField(choices=[('1', 'Mud'), ('2', 'Wood/bamboo'), ('3', 'Burnt brick'), ('4', 'Stone'), ('5', 'Cement'), ('6', 'Mosaic/floor tiles'), ('7', 'Any other')], max_length=1)),
                ('WallMaterial', models.CharField(choices=[('1', 'Grass/thatch/bamboo'), ('2', 'Plastic/polythene'), ('3', 'Mud/unburnt brick'), ('4', 'Wood'), ('5', 'Stone not packed with mortar'), ('6', 'Stone packed with mortar'), ('7', 'G.I./metal/asbestos sheets'), ('8', 'Burnt brick'), ('9', 'Concrete'), ('0', 'Any other')], max_length=1)),
                ('RoofMaterial', models.CharField(choices=[('1', 'Grass/ thatch/ bamboo/ wood/ mud'), ('2', 'Plastic/ polythene'), ('3', 'Hand made tiles'), ('4', 'Machine made tiles'), ('5', 'Burnt brick'), ('6', 'Stone'), ('7', 'Slate'), ('8', 'G.I./metal/asbestos sheets'), ('9', 'Concrete'), ('0', 'Any other')], max_length=1)),
                ('UseOfHouse', models.CharField(choices=[('1', 'Residence'), ('2', 'Residence-cum-other use'), ('3', 'Shop/ office'), ('4', 'School/ college'), ('5', 'Hotel/ lodge/ guest house'), ('6', 'Hospital/ dispensary'), ('7', 'Factory/ workshop/ workshed'), ('8', 'Place of worship'), ('9', 'Other non-residential use'), ('0', 'Any other')], max_length=1)),
                ('TotalResidents', models.IntegerField()),
                ('HeadName', models.CharField(max_length=200)),
                ('HeadSex', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=1)),
                ('HeadCaste', models.CharField(choices=[('1', 'SC'), ('2', 'ST'), ('3', 'Other')], max_length=1)),
                ('Ownership', models.CharField(choices=[('1', 'Owned'), ('2', 'Rented but has own house elsewhere'), ('3', 'Rented and does not own any house'), ('4', 'Any other')], max_length=1)),
                ('DwellingRooms', models.IntegerField()),
                ('MarriedCouples', models.IntegerField()),
                ('DrinkingWaterSource', models.CharField(choices=[('1', 'Tap water from source'), ('2', 'Tap water from un-treated source'), ('3', 'Well'), ('4', 'Hand Pump'), ('5', 'Tubewell/ borehole'), ('6', 'Spring'), ('7', 'River/canal'), ('8', 'Tank/pond/lake'), ('9', 'Packaged/bottled water'), ('0', 'Other sources')], max_length=1)),
                ('DrinkingWaterAvail', models.CharField(choices=[('1', 'Within premises'), ('2', 'Near the premises'), ('3', 'Away')], max_length=1)),
                ('LightingSource', models.CharField(choices=[('1', 'Electricity'), ('2', 'Kerosene'), ('3', 'Solar'), ('4', 'Other oil'), ('5', 'Any other'), ('6', 'No lighting')], max_length=1)),
                ('LatrineAccess', models.CharField(choices=[('1', 'YES, Exclusively for household use only'), ('2', 'YES, Shared with other household'), ('3', 'YES, Public latrine'), ('4', 'NO, Open')], max_length=1)),
                ('LatrineType', models.CharField(choices=[('1', 'Flush/pour flush latrine connected to Piped sewer system'), ('2', 'Flush/pour flush latrine connected to Septic tack'), ('3', 'Flush/pour flush latrine connected to Other system'), ('4', 'Twin Pit latrine With slab/ventilated improved pit'), ('5', 'Twin Pit latrine Without slab/open pit'), ('6', 'Single Pit latrine With slab/ventilated improved pit'), ('7', 'Single Pit latrine Without slab/open pit'), ('8', 'Service latrine Night soil removed by human'), ('9', 'Service latrine Night soil serviced by animals'), ('0', 'Night soil disposed into open drain')], max_length=1)),
                ('WasteWaterOutlet', models.CharField(choices=[('1', 'Closed drainage'), ('2', 'Open drainage'), ('3', 'No drainage')], max_length=1)),
                ('BathingFacility', models.CharField(choices=[('1', 'YES, Bathroom'), ('2', 'YES, Enclosure without roof'), ('3', 'NO')], max_length=1)),
                ('Kitchen', models.CharField(choices=[('1', 'Cooking in kitchen, has LPG/PNG Connection'), ('2', 'Cooking in kitchen, Does not have LPG/PNG Connection'), ('3', 'Cooking inside house, but not in kitchen, Has LPG/PNG Connection'), ('4', 'Cooking inside house, but not in kitchen, does not have LPG/PNG Connection'), ('5', 'Cooking in open/ outside house, Has LPG/PNG Connection'), ('6', 'Cooking in open/ outside house, does not have LPG/PNG Connection'), ('7', 'No cooking')], max_length=1)),
                ('KitchenFuel', models.CharField(choices=[('1', 'Firewood'), ('2', 'Crop residue'), ('3', 'Cowding cake'), ('4', 'Coal/lignite/charcoal'), ('5', 'Kerosene'), ('6', 'LPG/PNG'), ('7', 'Electricity'), ('8', 'Bio-gas'), ('9', 'Solar'), ('0', 'Any other')], max_length=1)),
                ('Radio', models.CharField(choices=[('1', 'YES, Traditional radio set'), ('2', 'YES, on mobile/smartphone'), ('3', 'YES, On any other device'), ('4', 'NO')], max_length=1)),
                ('Television', models.CharField(choices=[('1', 'YES, Doordarshan free dish'), ('2', 'YES, DTH/Dish'), ('3', 'YES, Cable connection'), ('4', 'Any other'), ('5', 'NO')], max_length=1)),
                ('Internet', models.CharField(choices=[('1', 'YES, On laptop/computer'), ('2', 'YES, On mobile/smartphone'), ('3', 'YES, On any other device'), ('4', 'NO')], max_length=1)),
                ('ComputingDevice', models.CharField(choices=[('1', 'YES'), ('2', 'NO')], max_length=1)),
                ('Phone', models.CharField(choices=[('1', 'YES, Landline only'), ('2', 'YES, Mobile only, Smartphone'), ('3', 'YES, Mobile only, Other basic mobile'), ('4', 'YES, Both'), ('5', 'No')], max_length=1)),
                ('TwoWheeler', models.CharField(choices=[('1', 'Bicycle'), ('2', 'Scooter/ Motorcycle/ Moped'), ('3', 'Both'), ('4', 'None')], max_length=1)),
                ('FourWheeler', models.CharField(choices=[('1', 'YES'), ('2', 'NO')], max_length=1)),
                ('Cereal', models.CharField(choices=[('1', 'Rice'), ('2', 'Wheat'), ('3', 'Jowar'), ('4', 'Bajra'), ('5', 'Maize'), ('6', 'Any other')], max_length=1)),
                ('ContactNo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='HouseHolds',
            fields=[
                ('fname', models.CharField(default='AMAR', max_length=50)),
                ('mname', models.CharField(default='AKBAR', max_length=50)),
                ('lname', models.CharField(default='ANTHONY', max_length=50)),
                ('state', models.CharField(default='UP', max_length=100)),
                ('district', models.CharField(default='Pune', max_length=100)),
                ('subDistrict', models.CharField(default='chincwad', max_length=100)),
                ('village', models.CharField(default='chincwad', max_length=100)),
                ('wardNo', models.IntegerField(default=0)),
                ('adhar', models.BigIntegerField(primary_key=True, serialize=False)),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=1)),
                ('dob', models.DateField(max_length=30)),
                ('age', models.IntegerField()),
                ('religion', models.CharField(choices=[('H', 'Hindu'), ('M', 'Muslim'), ('C', 'Christian'), ('S', 'Sikh'), ('B', 'Buddhist'), ('J', 'Jain')], max_length=1)),
                ('scst', models.CharField(choices=[('SC', 'Scheduled-Caste'), ('ST', 'Scheduled-Tribe'), ('NA', 'None')], max_length=2)),
                ('scstType', models.CharField(default='KALA', max_length=50)),
                ('martialStatus', models.CharField(choices=[('1', 'Never-Married'), ('2', 'Currently-Married'), ('3', 'Widowed'), ('4', 'Separated'), ('5', 'Divorced')], max_length=1)),
                ('disability', models.CharField(choices=[('1', 'Seeing'), ('2', 'Hearing'), ('3', 'Speech'), ('4', 'Movement'), ('5', 'Mental-Retardness'), ('6', 'Mental-Illness'), ('7', 'Multiple-Disability'), ('8', 'Other')], max_length=1)),
                ('motherTongue', models.CharField(default='Hindi', max_length=50)),
                ('literate', models.BooleanField(default=True)),
                ('statusOfAttendance', models.BooleanField(default=False)),
                ('highestEDUAttained', models.CharField(choices=[('1', 'School'), ('2', 'College'), ('3', 'Vocational'), ('4', 'Special Institution For Disabled'), ('5', 'Literacy-Centre'), ('6', 'Other-Institution'), ('7', 'None')], max_length=1)),
                ('workedLike', models.CharField(choices=[('1', 'Main-Worker'), ('2', 'Marginal-Worker'), ('3', 'Non-Worker')], max_length=1)),
                ('workedAs', models.CharField(choices=[('1', 'Employer'), ('2', 'Employee'), ('3', 'Single-Worker'), ('4', 'Family-Worker')], max_length=1)),
                ('describeWork', models.CharField(max_length=250)),
                ('industryType', models.CharField(max_length=250)),
                ('workerClass', models.CharField(choices=[('1', 'Employer'), ('2', 'Employee'), ('3', 'Single-Worker'), ('4', 'Family-Worker')], max_length=1)),
                ('nonWorkerType', models.CharField(choices=[('1', 'Student'), ('2', 'Household-Duties'), ('3', 'Dependent'), ('4', 'Pensioner'), ('5', 'Rentier'), ('6', 'Beggar'), ('7', 'Other')], max_length=1)),
                ('findingWork', models.BooleanField(default=False)),
                ('disOfTravelInKm', models.FloatField(default=0.0)),
                ('modeOfTravel', models.CharField(choices=[('1', 'On Foot'), ('2', 'Bicycle'), ('3', 'Moped/Scooter/Motor-Cycle'), ('4', 'Car/Jeep/VAN  '), ('5', 'Literacy Centre'), ('6', 'Other Institution'), ('7', 'None')], max_length=1)),
                ('birthPlace', models.CharField(max_length=500)),
                ('birthPlaceBool', models.BooleanField(default=True)),
                ('placeOfLastResidence', models.CharField(max_length=500)),
                ('placeOfLastResidenceBool', models.BooleanField(default=True)),
                ('lastMigrated', models.BooleanField(default=False)),
                ('cameFrom', models.CharField(choices=[('1', 'Rural'), ('2', 'Urban')], max_length=1)),
                ('durOfStayAfterMigration', models.IntegerField(default=1)),
                ('curChildren', models.IntegerField(default=0)),
                ('totChildren', models.IntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
