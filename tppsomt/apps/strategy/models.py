from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Constant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    dt = models.DecimalField(max_digits=10, decimal_places=2)  # forward integration time step.
    v0 = models.DecimalField(max_digits=10, decimal_places=2)  # initial velocity. Non-zero is necessary to initiate but is also physical as riders practice to throw out of the gate as the start signal is sounded.
    hl_length = models.DecimalField(max_digits=10, decimal_places=2)   # half-lap length i.e. 250m /2
    rho = models.DecimalField(max_digits=10, decimal_places=2) # air density
    bike_length = models.DecimalField(max_digits=10, decimal_places=2) # distance from front of front tyre to rear of rear tyre
    spacing = models.DecimalField(max_digits=10, decimal_places=2) # distance between rear tyre of lead rider and front tyre of following rider
    weight = models.DecimalField("weight distribution frt-rr", max_digits=10, decimal_places=2)
    crr_front = models.DecimalField(max_digits=10, decimal_places=2)   # Tyre rolling resistance coefficient
    crr_rear = models.DecimalField(max_digits=10, decimal_places=2)    # Tyre rolling resistance coefficient
    mu_scrub = models.DecimalField(max_digits=10, decimal_places=2)    # empirical tyre scrubbing coefficient (to account for when tyre is not @ 90 degrees to the track surface)
    efficiency = models.DecimalField(max_digits=10, decimal_places=2)  # % input power lost to mechanical friction (chain, bearings etc)
    front_mol = models.DecimalField(max_digits=10, decimal_places=2)   # Moment of Inertia of front, rear wheels
    rear_mol = models.DecimalField(max_digits=10, decimal_places=2)    # Moment of Inertia of front, rear wheels
    wheel_radius = models.DecimalField(max_digits=10, decimal_places=2)    # Distance from axle to tyre contact point with the track 
    time_standing = models.IntegerField()   # How long after leaving the start does the lead rider remain in the standing position. Determines which CDA value (seated/standing) is used.
    track_geo = models.CharField(max_length=3, choices=[("BRI", "BRI")]) # Legacy field enabling selection of different track geometries. For simplification only Brisbane ‘BRI’ is used in this model.
    distance = models.DecimalField("Distance from black line", max_digits=10, decimal_places=2)    # How far from the black line the rider is in the middle of the bend. Drives a calculation that scales lap distance travelled using perimeter of ellipse. Missing apex of the bend (further from black) is assumed to be slower.
    lap1_profile = models.CharField(max_length=1, choices=[("M", "Male"), ("F", "Female")])   #  Selects one of two VBA poly functions that define the lap 1 power profile.
    reaction = models.DecimalField("reaction time", max_digits=10, decimal_places=2)    # Time delay between start signal and movement out of the gate.
    team_2nd = models.BooleanField("2nd team")    # Selects one of two empirical relative wind speed profiles. TP competitions are 2 or 3 rounds. Qualifying is always one team only. Round 1 and/or the Final have two teams on the track. Relative wind speed due to greater air swirl in the velodrome is greater with two teams. Assumes teams remain equi-distant.
    p1_cda = models.DecimalField(max_digits=10, decimal_places=2)  # empirical value. Scales the lead rider’s CDA to account for favourable aerodynamic interaction from following rider

    class Meta:
        indexes = [
            models.Index(fields=["owner", "name"]),
        ]
    
    def __str__(self):
        return self.name
