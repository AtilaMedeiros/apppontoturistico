def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)
