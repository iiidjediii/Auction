from django.db import models
#from datetime import DateTimeField
from django.contrib.auth.models import User



class Auction(models.Model):
    lot_start_date = models.DateTimeField(auto_now_add=True)
    lot_title = models.CharField(max_length=100, blank=True, default='')
    lot_description = models.TextField(max_length=1000, help_text='Enter a brief description of the your lot')
    lot_author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='auctions', default='1')
    lot_start_price = models.CharField(max_length=100, default=100)
    lot_end_date = models.DateField()
    lot_last_bet_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='lot_last_bet_user', verbose_name="Who placed the bet", null=True, blank=True)
    lot_last_bet_price = models.IntegerField(null=True, blank=True)
    LOT_STATUS = (
        ('b', 'being traded'),
        ('c', 'completed'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOT_STATUS,
        blank=True,
        default='b',
        help_text='Lot is available for purchase',
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.lot_title

    class Meta:
        ordering = ['lot_end_date']
        db_table = 'auction'

    def save(self, *args, **kwargs):
        super(Auction, self).save(*args, **kwargs)