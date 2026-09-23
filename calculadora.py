from mi_paquete.operaciones import sumar, restar, multiplicar, dividir
from mi_paquete.utils import formatear_resultado

print("=== CALCULADORA ===")
res_suma = sumar(10, 5)
print(formatear_resultado("10 + 5", res_suma))

res_mult = multiplicar(4, 3)
print(formatear_resultado("4 * 3", res_mult))