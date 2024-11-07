from django.db import models
#manytomany
class Categoria(models.Model):
    Nombre = models.CharField(max_length=50,verbose_name='Nombre :',unique=True,blank=False,help_text='Ingresa solo texto')
    
    def __str__(self):
        return self.Nombre
    class Meta:
        db_table = 'Categoria'
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categoria'

class Producto(models.Model):
   # Codigo = 
   
    Nombre = models.CharField(max_length=50,verbose_name='Nombre :',unique=True,blank=False)
    precio = models.DecimalField(max_digits=4,decimal_places=2,verbose_name='Precio :',blank=False)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria,on_delete= models.RESTRICT)
    
    def __str__(self):
        return self.Nombre
    class Meta:
        db_table = 'Producto'
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Producto'

class Cliente(models.Model):
    Cedula = models.CharField(max_length=10,verbose_name='Cedula: ',null=False)
    Nombre = models.CharField(max_length=50,verbose_name='Nombre :',unique=True,blank=False)
    Apellido = models.CharField(max_length=50,verbose_name='Apellido :',unique=True,blank=False)
    Edad = models.IntegerField()
    correo = models.EmailField()
    domicilio= models.TextField(max_length=200,help_text='Escribe tu referencia: ')
    
    def __str__(self):
        return f'{self.Nombre}{self.apellido}'
    class Meta:
        db_table = 'Cliente'
        managed = True
        verbose_name = 'Cliente'
        verbose_name_plural = 'Cliente'

class Orden(models.Model):
    fecha = models.DateField( auto_now_add = True)
    total = models.DecimalField(max_digits=4,decimal_places=2)
    Cliente = models.ForeignKey(Cliente,on_delete=models.RESTRICT)
    Producto = models.ManyToManyField(Producto)
    
    def __str__(self):
        return f'Orden de {self.id} - Cliente: {self.Cliente.Nombre}'
    class Meta:
        db_table = 'Orden'
        managed = True
        verbose_name = 'Orden'
        verbose_name_plural = 'Orden'