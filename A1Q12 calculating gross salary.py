#input basic salary
basic=float(input("enter basic salary"))
if basic<=10000:
            hra_percent=20
            da_percent=80
else:
    if basic <= 20000:
        hra_percent=25
        dra_percent=90
    else:
        if basic > 20000:
            hra_percent=30
            da_percent=95
hra = (hra_percent/100) * basic
da = (da_percent/100) * basic
gross_sallary = hra + da + basic
print(gross_sallary)
