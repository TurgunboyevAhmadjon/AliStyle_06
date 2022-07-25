from django.db import models

class Bolim(models.Model):
    nom = models.CharField(max_length=40)
    rasm = models.FileField(upload_to='bolimlar')
    def __str__(self):
        return self.nom

class Ichki(models.Model):
    nom = models.CharField(max_length=30)
    rasm = models.FileField(upload_to='ichkilar')
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True, related_name="bolim_ichkilari")

    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    narx = models.IntegerField()
    ishlab_ch = models.CharField(max_length=20)
    kafolat = models.CharField(max_length=30)
    yetkazish = models.CharField(max_length=50)
    mavjud = models.BooleanField(default=True)
    batafsil = models.CharField(max_length=500)
    ichki = models.ForeignKey(Ichki, on_delete=models.SET_NULL, null=True, related_name="ichki_mahsulot")

    def __str__(self):
        return self.nom

class Media(models.Model):
    rasm = models.FileField(upload_to='mahsulotlar')
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.rasm