from django.db import models

class problem(models.Model):
    name=models.CharField(max_length=1000,null='true')
    statement=models.TextField(null='true')
    inputs=models.TextField(null='true')
    outputs=models.TextField(null='true')
    examples=models.TextField(null='true')
    constraints=models.TextField(null='true')
    code=models.TextField(null='true')

    def __str__(self):
        return self.name

class solutions(models.Model):
    prob=models.ForeignKey("problem", on_delete=models.CASCADE)
    verdict=models.IntegerField(null='true')
    def __str__(self):
        return self.prob.name

class test(models.Model):
    index=models.IntegerField(null='true')  
    inp=models.TextField(null='true')
    oup=models.TextField(null='true')
    prob=models.ForeignKey("problem", on_delete=models.CASCADE)
    def __str__(self):
        return self.prob.name