from django.contrib import admin
import models



class CompetitionAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Competition, CompetitionAdmin)

class CompetitionPhaseAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.CompetitionPhase, CompetitionPhaseAdmin)

class ParticipantStatusAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.ParticipantStatus, ParticipantStatusAdmin)

class ExternalFileTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.ExternalFileType, ExternalFileTypeAdmin)

class ContentContainerTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.ContentContainerType, ContentContainerTypeAdmin)

class ContentContainerAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.ContentContainer, ContentContainerAdmin)

class ContentVisibilityAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.ContentVisibility, ContentVisibilityAdmin)

class ContentEntityAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.ContentEntity, ContentEntityAdmin)
