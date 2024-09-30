from django.db import models

# Create your models here.

u_typename = [
    ('1', 'user'),
    ('2', 'seller'),
    ('3', 'admin'),
]
status = [
    ('1', '0 ACTIVE'),
    ('2', '1 INACTIVE'),
]

end_month = [
    ('1', 'jan'),
    ('2', 'feb'),
    ('3', 'mar'),
    ('4', 'apr'),
    ('5', 'may'),
    ('6', 'jun'),
    ('7', 'jul'),
    ('8', 'aug'),
    ('9', 'oct'),
    ('10', 'sep'),
    ('11', 'nov'),
    ('12', 'dec'),

]
end_year = [
    ('1', '2022'),
    ('2', '2021'),
    ('3', '2022'),
    ('4', '2023'),
    ('5', '2024'),
    ('6', '2025'),
    ('7', '2026'),
    ('8', '2027'),
    ('9', '2028'),
    ('10', '2029'),
    ('11', '2030'),
]


class Role(models.Model):
    u_name = models.CharField(max_length=30, choices=u_typename)

    def __str__(self):
        return self.u_name


class user_details(models.Model):
    u_name = models.CharField(max_length=30)
    u_password = models.IntegerField()
    u_email = models.EmailField()
    u_phone_no = models.IntegerField()
    u_type = models.ForeignKey(Role, on_delete=models.CASCADE)
    u_status = models.CharField(max_length=30, choices=status)

    def __str__(self):
        return self.u_name


class bank_details(models.Model):
    u_id = models.ForeignKey(user_details, on_delete=models.CASCADE)
    b_name = models.CharField(max_length=30)
    digit_no = models.IntegerField()
    end_month = models.CharField(max_length=30, choices=end_month)
    end_year = models.CharField(max_length=30, choices=end_year)