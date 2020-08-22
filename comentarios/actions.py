def reprova_comentarios(modeladmin, request, queryset):
    queryset.update(aprovador=False)


def aprova_comentarios(modeladmin, request, queryset):
    queryset.update(aprovador=True)


reprova_comentarios.short_description = 'Reprovar comentarios'
aprova_comentarios.short_description = 'Aprovar comentarios'
