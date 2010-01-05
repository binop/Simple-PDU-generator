from django.db import models


class SMSData(models.Model):
    RP = models.DecimalField(max_digits=1,decimal_places=0,default=0)
    UDHI = models.DecimalField(max_digits=1, decimal_places=0,default=0)
    SRR = models.DecimalField(max_digits=1, decimal_places=0,default=0)
    VPF1 = models.DecimalField(max_digits=1, decimal_places=0,default=0)
    VPF2 = models.DecimalField(max_digits=1, decimal_places=0,default=0)
    RD = models.DecimalField(max_digits=1, decimal_places=0,default=0)
    MTI1 = models.DecimalField(max_digits=1, decimal_places=0,default=0)
    MTI2 = models.DecimalField(max_digits=1, decimal_places=0,default=1)    
    MR = models.DecimalField(max_digits=3, decimal_places=0,default=0)   
    DA = models.DecimalField(max_digits=15, decimal_places=0,default=3584544180845)
    PID = models.DecimalField(max_digits=1, decimal_places=0,default=0)  
    HCDCS1 = models.DecimalField(max_digits=1, decimal_places=0,default=0)
    HCDCS2 = models.DecimalField(max_digits=1, decimal_places=0,default=0)
    TC = models.DecimalField(max_digits=1, decimal_places=0,default=0)
    CM = models.DecimalField(max_digits=1, decimal_places=0,default=0)
    ALPH1 = models.DecimalField(max_digits=1, decimal_places=0,default=0)
    ALPH2 = models.DecimalField(max_digits=1, decimal_places=0,default=0)
    CL1 = models.DecimalField(max_digits=1, decimal_places=0,default=0)
    CL2 = models.DecimalField(max_digits=1, decimal_places=0,default=0)
    SMSC = models.DecimalField(max_digits=15, decimal_places=0,default=353454400051)
    UDH = models.CharField(max_length=100,default='0')
    UD = models.CharField(max_length=160,default='Simple text')
    UD_FORMAT_CHOICES = (
        ('1','Option 1 - UDH in hex and UD in GSM7'),
        ('2','Option 2 - UDH and UD in hex'),
    )
    UDFormat = models.CharField(max_length=1, choices=UD_FORMAT_CHOICES, default = 1)
    DRAFT_NAME = models.CharField(max_length=20, default='Simple SMS', 
                                  unique=True, blank=True)


    @models.permalink
    def get_absolute_url(self):
        return ('details', (), { 'object_id' : self.id })
