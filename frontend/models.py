from django.db import models

# Create your models here.

class menuKopi(models.Model):
    gambar = models.CharField(max_length=30)
    nama_kopi = models.CharField(max_length=30)
    harga = models.IntegerField()

class customer(models.Model):
    nama_customer = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    nomor_hp = models.CharField(max_length=30)

class pesanan(models.Model):
    no_pesanan = models.IntegerField()
    id_customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    jumlah_pesanan = models.IntegerField()
    pesanan = models.ForeignKey(menuKopi, on_delete=models.CASCADE)
    total_harga = models.IntegerField()
    sudah_bayar = models.BooleanField()
