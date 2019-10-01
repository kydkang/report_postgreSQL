from django.contrib import admin
from .models import Event, Informe, SatImage, Area, Location


admin.site.register(Event)
admin.site.register(Informe)  
admin.site.register(Area)
admin.site.register(Location)

class SatImageAdmin(admin.ModelAdmin):
    list_display = ['event', 'fuente', 'banda', 'fecha', 'image']
admin.site.register(SatImage, SatImageAdmin)


