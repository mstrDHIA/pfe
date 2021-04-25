from django.contrib import admin
from .models import FeedBack,Order,Profile

# Register your models here.


admin.site.site_header = 'Admin Management'
admin.site.site_title = 'Admin Management'

admin.site.site_url = '**Empty**'
admin.site.index_title = 'Admin Management'
#admin.empty_value_display = '**Empty**'

@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ("id_user", "object","date","verified")
    list_filter = ("date","verified")
    search_fields = ("object",)



    pass



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "id_buyer","id_seller","id_user","state","order_time","delivery_time","stars")
    list_filter = ("order_time","state","stars","id_user","id_buyer","id_seller")
    search_fields = ("id",)

    pass



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id","id_user","sex","age","country","governorate","vehicle")
    list_filter = ("sex","age","country","governorate","vehicle")
#    search_fields = ("id_user",)

    pass

