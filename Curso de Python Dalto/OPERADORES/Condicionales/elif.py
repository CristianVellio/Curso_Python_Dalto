ingreso_mensual = 81000
gasto_mensual = 80000

#if anidado y else if (elif)
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas em Deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Bien pa, estas bien")
    else:
        print("Y pa, estas gastando una banda, hay que ver si te alcanza")
        
elif ingreso_mensual > 1000:
    print("Estas bien en latinoamerica")
    
elif ingreso_mensual > 500:
    print("Estas bien en Argentina")
    
elif ingreso_mensual > 200:
    print("Estas bien en Venezuela")
    
else:
    print("Sos pobre")