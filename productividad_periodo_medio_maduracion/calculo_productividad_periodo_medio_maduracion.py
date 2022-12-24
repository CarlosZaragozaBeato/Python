import math
from builtins import map

def CalcularProductividad():
    materias_primas = ObtenerValorMateriasPrimas()
    capital = ObtenerValorCapital()
    trabajo = ObtenerValorFactorTrabajo()
    total_ingresos = int(input("Introduzca el total de ingresos: "))

    factor_materias_primas = CalcularFactorMateriasPrimas(total_ingresos, materias_primas)
    factor_capital = CalcularFactorCapital(total_ingresos, capital)
    factor_trabajo = CalcularFactorTrabajo(total_ingresos,trabajo)

    productividad_global = CalcularProductividadGlobal(total_ingresos, materias_primas, capital, trabajo)

    return f"El valor del factor de materias primas es {factor_materias_primas}\n" \
           f"El valor del factor del capital es {factor_capital}\n" \
           f"El valor del factor del trabajo es {factor_trabajo}\n" \
           f"La productividad global es {productividad_global}" \




def ObtenerValorMateriasPrimas():
    materias_primas = 0
    while True:
         valor = input("Introduce materias primas: ")
         if len(valor) == 0:break
         materias_primas += int(valor)
    return materias_primas

def ObtenerValorCapital():
    capital = 0
    while True:
         valor = input("Introduce capital: ")
         if len(valor) == 0:break
         capital += int(valor)
    return capital

def ObtenerValorFactorTrabajo():
    factor_trabajo = 0
    while True:
        valor = input("Introduce factor trabajo: ")
        if len(valor) == 0:break
        factor_trabajo += int(valor)
    return factor_trabajo

def CalcularFactorMateriasPrimas(ingresos, materias_primas):
    return ingresos/materias_primas

def CalcularFactorTrabajo(ingresos, factor_trabajo):
    return ingresos/factor_trabajo

def CalcularFactorCapital(ingresos, capital):
    return ingresos/capital

def CalcularProductividadGlobal(ingresos, materias_primas, factor_trabajo, capital):
    return ingresos/(materias_primas+factor_trabajo+capital)



print(CalcularProductividad())




def CalcularPeriodoMedioMaduracion():
    periodo_almacen = int(input("Introduce el tiempo medio en el almacen(días): "))
    periodo_venta = int(input("Introduce el tiempo medio de venta (días): "))
    periodo_cobro = int(input("Introduce el tiempo medio de cobro (días): "))
    periodo_fabricacion = int(input("Introduce el tiempo medio de frabricacion (días): "))
    periodo_pago = int(input("Introduce el tiempo medio de pago (días): "))
    pmme = CalcularPeriodoMedioMaduracionEconomico(periodo_almacen, periodo_venta, periodo_cobro,periodo_fabricacion)
    pmmf = CalcularPeriodoMedioMaduracionFinanciero(pmme, periodo_pago)
    numero_ciclos = CalcularNumeroCiclos(pmme)
    return f'El Periodo medio de maduracion económico es {pmme}\n' \
           f'El Periodo medio de maduracion financiero es {pmmf}\n' \
           f'El numero de ciclos por año es {numero_ciclos}'

def CalcularPeriodoMedioMaduracionEconomico(pa, pv, pc, pf):
    return pa+pv+pc+pf
def CalcularPeriodoMedioMaduracionFinanciero(pmme, pp):
    return pmme - pp
def CalcularNumeroCiclos(pmme):
    return 365/pmme

#print(CalcularPeriodoMedioMaduracion())
