from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Constant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    dt = models.CharField(max_length=16, default="0.00")  # forward integration time step.
    v0 = models.CharField(max_length=16, default="0.00")  # initial velocity. Non-zero is necessary to initiate but is also physical as riders practice to throw out of the gate as the start signal is sounded.
    hl_length = models.CharField(max_length=16, default="0.00")   # half-lap length i.e. 250m /2
    rho = models.CharField(max_length=16, default="0.00") # air density
    bike_length = models.CharField(max_length=16, default="0.00") # distance from front of front tyre to rear of rear tyre
    spacing = models.CharField(max_length=16, default="0.00") # distance between rear tyre of lead rider and front tyre of following rider
    weight = models.CharField("weight distribution frt-rr", max_length=16, default="0.00")
    crr_front = models.CharField(max_length=16, default="0.00")   # Tyre rolling resistance coefficient
    crr_rear = models.CharField(max_length=16, default="0.00")    # Tyre rolling resistance coefficient
    mu_scrub = models.CharField(max_length=16, default="0.00")    # empirical tyre scrubbing coefficient (to account for when tyre is not @ 90 degrees to the track surface)
    efficiency = models.CharField(max_length=16, default="0.00")  # % input power lost to mechanical friction (chain, bearings etc)
    front_mol = models.CharField(max_length=16, default="0.00")   # Moment of Inertia of front, rear wheels
    rear_mol = models.CharField(max_length=16, default="0.00")    # Moment of Inertia of front, rear wheels
    wheel_radius = models.CharField(max_length=16, default="0.00")    # Distance from axle to tyre contact point with the track 
    time_standing = models.CharField(max_length=16, default="0.00")   # How long after leaving the start does the lead rider remain in the standing position. Determines which CDA value (seated/standing) is used.
    track_geo = models.CharField(max_length=16, default="BRI") # Legacy field enabling selection of different track geometries. For simplification only Brisbane ‘BRI’ is used in this model.
    distance = models.CharField(max_length=16, default="0.00")    # How far from the black line the rider is in the middle of the bend. Drives a calculation that scales lap distance travelled using perimeter of ellipse. Missing apex of the bend (further from black) is assumed to be slower.
    lap1_profile =  models.CharField(max_length=16, default="Male")   #  Selects one of two VBA poly functions that define the lap 1 power profile.
    reaction = models.CharField(max_length=16, default="0.00")   # Time delay between start signal and movement out of the gate.
    team_2nd = models.CharField("2nd team", max_length=16, default="0.00")   # Selects one of two empirical relative wind speed profiles. TP competitions are 2 or 3 rounds. Qualifying is always one team only. Round 1 and/or the Final have two teams on the track. Relative wind speed due to greater air swirl in the velodrome is greater with two teams. Assumes teams remain equi-distant.
    p1_cda = models.CharField(max_length=16, default="0.00")  # empirical value. Scales the lead rider’s CDA to account for favourable aerodynamic interaction from following rider

    class Meta:
        indexes = [
            models.Index(fields=["owner", "name"]),
        ]
    
    def __str__(self):
        return self.name


class Rider(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.CharField("Rider Profile", max_length=16)
    cda_seated = models.CharField("CDA Seated", max_length=16, default="0.000")
    seat_height = models.CharField("Seat Height from groud", max_length=16, default="0.00")
    trun1_power = models.CharField("Turn 1 power", max_length=16, default="0.00")
    trun2_power = models.CharField("Turn 2 power", max_length=16, default="0.00")

    class Meta:
        indexes = [
            models.Index(fields=["owner", "profile"]),
        ]
    
    def __str__(self):
        return self.profile

class Strategy(models.Model):
    foreign_fields = {"rider1":Rider, "rider2":Rider, "rider3":Rider, "rider4":Rider, "rider5":Rider, "constant":Constant}
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    constant = models.ForeignKey(Constant, on_delete=models.SET_NULL, blank=True, null=True)

    rider1 = models.ForeignKey(Rider, related_name="rider1", on_delete=models.SET_NULL, blank=True, null=True)
    rider2 = models.ForeignKey(Rider, related_name="rider2", on_delete=models.SET_NULL, blank=True, null=True)
    rider3 = models.ForeignKey(Rider, related_name="rider3", on_delete=models.SET_NULL, blank=True, null=True)
    rider4 = models.ForeignKey(Rider, related_name="rider4", on_delete=models.SET_NULL, blank=True, null=True)
    rider5 = models.ForeignKey(Rider, related_name="rider5", on_delete=models.SET_NULL, blank=True, null=True)

    turn1_1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn1_2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn1_3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn1_4 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn1_5 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    turn2_1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn2_2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn2_3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn2_4 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn2_5 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    turn3_1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn3_2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn3_3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn3_4 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn3_5 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    turn4_1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn4_2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn4_3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn4_4 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn4_5 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    turn5_1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn5_2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn5_3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn5_4 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn5_5 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)


    class Meta:
        indexes = [
            models.Index(fields=["owner", "name"]),
        ]
    
    def __str__(self):
        return self.name

    def calculate(self):
        # some calculate ...
        # save the result to a model
        # return the result model
        return Result.objects.get(strategy__pk=self.pk)


class Result(models.Model):
    strategy = models.OneToOneField(Strategy, on_delete=models.DO_NOTHING)
    total_time = models.CharField(max_length=16, default="00:00.00")
    time_chart = models.JSONField()

    def __str__(self):
        return f"{self.strategy.name}#{str(self.id)}"
