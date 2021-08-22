from django.db import models

# Create your models here.
class Countrie(models.Model):
    '''
    This class will represent a country with all citys and poblation
    '''

    ''' Columns '''
    name_countrie = models.CharField('Name', max_length=60)
    state = models.CharField('State', max_length=60)
    city = models.CharField('Cities', max_length=60)
    population = models.IntegerField('Population')


    class Meta():
        '''
        Options for configuration of web side
        '''

        ''' Options '''
        verbose_name = 'Countrie'
        verbose_name_plural = 'Countries'
        unique_together = ('name_countrie', 'city', 'state', 'population')
        ordering = ['name_countrie', 'city', 'state', 'population']
    

    def __str__(self) -> str:
        '''
        This method will represent own model
        '''
        return f'{self.name_countrie} - {self.city}, {self.state} - {self.population}'