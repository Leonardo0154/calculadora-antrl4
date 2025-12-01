from sympy import symbols, integrate, sin, cos, tan, exp, log, diff, simplify, factor, collect
from antlr4 import *
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from CalcVisitor import CalcVisitor
import sys
import os

class MyVisitor(CalcVisitor):
    def __init__(self):
        #  AÑADIDO: Configuración de optimización
        self.optimizar_resultados = True
        self.simplificar_expresiones = True
    
    def visitExprInt(self, ctx):
        return int(ctx.INT().getText())

    def visitExprFloat(self, ctx):
        return float(ctx.FLOAT().getText())

    def visitExprVar(self, ctx):
        return symbols(ctx.ID().getText())

    def visitExprAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        result = left + right if ctx.ADD() else left - right
        #  AÑADIDO: Aplicar optimización al resultado
        return self._optimizar_resultado(result)

    def visitExprMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        result = left * right if ctx.MUL() else left / right
        #  AÑADIDO: Aplicar optimización al resultado
        return self._optimizar_resultado(result)

    def visitExprPow(self, ctx):
        result = self.visit(ctx.expr(0)) ** self.visit(ctx.expr(1))
        #  AÑADIDO: Aplicar optimización al resultado
        return self._optimizar_resultado(result)

    def visitExprPar(self, ctx):
        return self.visit(ctx.expr())

    def visitExprIntegral(self, ctx):
        expr = self.visit(ctx.expr(0))
        var = symbols(ctx.ID().getText())
        if len(ctx.expr()) > 1:
            # Integral DEFINIDA
            lower = self.visit(ctx.expr(1))
            upper = self.visit(ctx.expr(2))
            result = integrate(expr, (var, lower, upper))
        else:
            # Integral INDEFINIDA - agregar + C al final
            from sympy import Symbol
            C = Symbol('C')
            resultado = integrate(expr, var)
            # Solo agregar +C si el resultado no es cero
            if resultado != 0:
                # Forzar que C aparezca al final
                result = resultado + C
            else:
                result = C
        
        #  AÑADIDO: Aplicar optimización al resultado
        return self._optimizar_resultado(result)

    def visitExprDerivada(self, ctx):
        expr = self.visit(ctx.expr())
        var = symbols(ctx.ID().getText())
        result = diff(expr, var)
        #  AÑADIDO: Aplicar optimización al resultado
        return self._optimizar_resultado(result)

    def visitExprSin(self, ctx):
        result = sin(self.visit(ctx.expr()))
        #  AÑADIDO: Aplicar optimización al resultado
        return self._optimizar_resultado(result)

    def visitExprCos(self, ctx):
        result = cos(self.visit(ctx.expr()))
        #  AÑADIDO: Aplicar optimización al resultado
        return self._optimizar_resultado(result)

    def visitExprTan(self, ctx):
        result = tan(self.visit(ctx.expr()))
        #  AÑADIDO: Aplicar optimización al resultado
        return self._optimizar_resultado(result)

    def visitExprExp(self, ctx):
        result = exp(self.visit(ctx.expr()))
        #  AÑADIDO: Aplicar optimización al resultado
        return self._optimizar_resultado(result)

    def visitExprLog(self, ctx):
        result = log(self.visit(ctx.expr()))
        #  AÑADIDO: Aplicar optimización al resultado
        return self._optimizar_resultado(result)
    
    #  AÑADIDO: Método de optimización
    def _optimizar_resultado(self, result):
        """Aplica optimizaciones al resultado sin afectar números simples"""
        if not self.optimizar_resultados:
            return result
            
        # No optimizar números simples
        if isinstance(result, (int, float)):
            return result
        
        try:
            # Simplificar expresión
            if self.simplificar_expresiones:
                result = simplify(result)
            
            # Intentar factorizar
            result = factor(result)
            
            # Colectar términos semejantes
            result = collect(result)
            
        except:
            # Si falla alguna optimización, mantener el resultado original
            pass
            
        return result

def calcular_expresion(expresion):
    """Calcula una expresión individual"""
    # Crear archivo temporal
    with open('temp.xyz', 'w') as f:
        f.write(expresion + '\n')
    
    try:
        lexer = CalcLexer(FileStream('temp.xyz'))
        tokens = CommonTokenStream(lexer)
        parser = CalcParser(tokens)
        tree = parser.prog()

        driver = MyVisitor()
        results = []
        for stat in tree.stat():
            result = driver.visit(stat.expr())
            results.append(result)
        
        # Limpiar archivo temporal
        if os.path.exists('temp.xyz'):
            os.remove('temp.xyz')
            
        return results[0] if results else None
        
    except Exception as e:
        # Limpiar archivo temporal en caso de error
        if os.path.exists('temp.xyz'):
            os.remove('temp.xyz')
        
        # Mensajes de error más específicos y útiles
        error_msg = str(e)
        if "extraneous input" in error_msg:
            if "expecting ','" in error_msg and "x" in expresion:
                return "ERROR: Falta el operador * en multiplicación. Usa: 5*x en lugar de 5x"
            return "ERROR de sintaxis: Revisa paréntesis, comas u operadores"
        elif "missing" in error_msg:
            if "ID" in error_msg:
                return "ERROR: Falta la variable de integración/derivación"
            return "ERROR: Faltan paréntesis, comas o argumentos"
        elif "no viable alternative" in error_msg:
            return "ERROR: Expresión no válida"
        elif "token recognition error" in error_msg:
            return "ERROR: Carácter no reconocido en la expresión"
        else:
            return f"ERROR: {error_msg}"

def modo_archivo(nombre_archivo):
    """Modo: procesar archivo .xyz"""
    lexer = CalcLexer(FileStream(nombre_archivo))
    tokens = CommonTokenStream(lexer)
    parser = CalcParser(tokens)
    tree = parser.prog()

    driver = MyVisitor()
    for i, stat in enumerate(tree.stat(), 1):
        result = driver.visit(stat.expr())
        print(f"Resultado {i}: {result}")

def modo_interactivo():
    """Modo: consola interactiva"""
    print("=" * 60)
    print("           CALCULADORA MATEMÁTICA COMPLETA")
    print("=" * 60)
    print("OPERACIONES BÁSICAS:")
    print("  Suma: 5 + 3")
    print("  Resta: 10 - 4")
    print("  Multiplicación: 6 * 2")
    print("  División: 15 / 3")
    print("  Potencia: 2 ** 3")
    print("  Con variables: x + 5, 2*x, x**2")
    print("\nCÁLCULO AVANZADO:")
    print("  Derivadas: derivada(x**2, x)")
    print("  Integrales: integral(sin(x), x)")
    print("  Integral def: integral(x**2, x, 0, 1)")
    print("\nFUNCIONES:")
    print("  sin(x), cos(x), tan(x), exp(x), log(x)")
    print("\nIMPORTANTE:")
    print("  Usar * para multiplicación: 5*x (NO 5x)")
    print("  Integrales indefinidas incluyen +C al final")
    print("\nCOMANDOS:")
    print("  salir - Terminar programa")
    print("  archivo <nombre> - Procesar archivo")
    print("  ayuda - Mostrar esta ayuda")
    print("=" * 60)
    
    while True:
        try:
            entrada = input("\n>>> ").strip()
            
            if not entrada:
                continue
                
            if entrada.lower() == 'salir':
                print("¡Hasta luego!")
                break
                
            if entrada.lower() == 'ayuda':
                modo_interactivo()
                continue
                
            if entrada.startswith('archivo '):
                nombre_archivo = entrada[8:].strip()
                if os.path.exists(nombre_archivo):
                    print(f" Procesando archivo: {nombre_archivo}")
                    modo_archivo(nombre_archivo)
                else:
                    print(f" Error: Archivo '{nombre_archivo}' no encontrado")
                continue
            
            #Permitir operaciones básicas y comandos especiales
            es_operacion_basica = any(op in entrada for op in ['+', '-', '*', '/', '**'])
            es_numero = entrada.replace('.', '').replace('-', '').isdigit()
            es_variable = entrada.isalpha()
            es_comando_especial = entrada.lower() in ['ayuda', 'salir'] or entrada.startswith('archivo ')

            if (not entrada.startswith('derivada(') and 
                not entrada.startswith('integral(') and
                not es_operacion_basica and
                not es_numero and
                not es_variable and
                not es_comando_especial):
                print("Comandos aceptados:")
                print("  Operaciones: 2+3, 5*4, x**2, etc.")
                print("  Derivadas: derivada(x**2, x)")
                print("  Integrales: integral(sin(x), x)")
                print("  Comandos: ayuda, salir, archivo <nombre>")
                continue
            
            # Calcular expresión individual
            resultado = calcular_expresion(entrada)
            print(f" Resultado: {resultado}")
            
        except Exception as e:
            print(f" Error: {e}")
            print(" Sugerencia: Revisa la sintaxis o escribe 'ayuda'")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Modo: python main.py archivo.xyz
        modo_archivo(sys.argv[1])
    else:
        # Modo interactivo por defecto
        modo_interactivo()