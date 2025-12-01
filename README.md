![LogoUPC](./logoupc.svg)
1ACC0218-2520-1733 - Teoría de Compiladores
Profesor: Peter Jonathan Montalvo Garcia

Integrantes:
| Nombres y Apellidos | Codigo | 
|------------|------------|
| Alvaro Jair Abanto Davila    | U202313540    |
| Daniel Jose Huapaya Vargas    | U202312230     | 
| Leonardo Gamboa Huilcaya 		| u202322950	|
# Problemática y motivación.

## Problemática

En el ámbito académico y profesional de matemáticas, ingeniería y ciencias, existe una necesidad constante de realizar cálculos de derivadas e integrales de manera precisa y eficiente. Aunque existen herramientas como SymPy, Mathematica y Maple, estas presentan varias limitaciones:

Falta de estandarización: No existe un lenguaje específico y ampliamente aceptado para expresar operaciones de cálculo diferencial e integral de forma declarativa.

Dependencia de entornos complejos: Las herramientas existentes requieren instalaciones complejas o licencias costosas.

Falta de portabilidad: Muchas soluciones no pueden ejecutarse fácilmente en diferentes sistemas operativos.

Curva de aprendizaje elevada: El uso de bibliotecas de programación requiere conocimientos técnicos avanzados.

Por qué es importante

Accesibilidad educativa: Los estudiantes de cálculo necesitan una herramienta sencilla para verificar sus ejercicios.

Reproducibilidad: Un DSL permite expresar definiciones matemáticas de manera concisa y versionable.

Verificación automática: Posibilidad de validar resultados y detectar errores en cálculos manuales.

Integración pedagógica: Herramienta que puede usarse en entornos educativos sin costos adicionales.

NUESTRRA SOLUCION

Desarrollamos un Lenguaje de Dominio Específico (DSL) para cálculo simbólico, implementado con:

ANTLR4 para la gramática y parsing

SymPy como motor matemático

Docker para empaquetado y portabilidad

Python como lenguaje de implementación

¿Existe y es un proceso largo?

Existen sistemas y bibliotecas consolidadas para manipulación simbólica y cálculo, pero no un estándar exclusivo para un DSL orientado a expresiones matemáticas simbólicas con enfoque en integración con herramientas de compilación y análisis estático. Diseñar e implementar un DSL completo es un proceso de varias fases: diseño del dominio y la gramática, implementación del parser (por ejemplo con ANTLR4), representación interna (AST), chequeos semánticos y verificación, y por último la implementación de un intérprete o generador de código. Dependiendo del alcance (solo sintaxis y parseo vs. resolución simbólica y generación de código optimizado), el esfuerzo puede variar desde unas semanas (prueba de concepto) hasta varios meses (herramienta robusta y documentada).

Relación con el trabajo propuesto

Nuestro proyecto propone crear un lenguaje para expresiones matemáticas simbólicas (en ANTLR4 con backend en Python) que permita, entre otras cosas, describir funciones definidas y continuas, funciones trigonométricas y polinómicas, y operar sobre ellas (por ejemplo, derivación simbólica). Esta capacidad simbólica habilita análisis simbólico, generación de código y usos pedagógicos en cálculo simbólico.

## Motivación

Objetivo general

Desarrollar una calculadora simbólica especializada en cálculo diferencial e integral, que pueda ejecutarse en cualquier entorno mediante contenedores Docker, proporcionando resultados exactos y simbólicos con una interfaz intuitiva.

- Definidas y continuas (por ejemplo funciones a trozos con condiciones sobre el dominio).
- Trigonométricas (sin, cos, tan y combinaciones) con simplificación y derivación simbólica.
- Polinómicas y sus derivadas, con operaciones algebraicas básicas (suma, producto, potencia).

Motivaciones concretas

Simplicidad de uso: Interfaz de línea de comandos intuitiva con modo interactivo.

Portabilidad total: Ejecución en cualquier sistema con Docker instalado.

Precisión simbólica: Resultados exactos, no aproximaciones numéricas.

Validación automática: Detección de errores sintácticos y semánticos.

Aplicación educativa: Herramienta de apoyo para estudiantes de cálculo.

Ejemplos ilustrativos (cómo se expresarían y qué se espera)


- Integración simbólica y numérica (indefinida y definida):

	Ejemplos: \(\int sin(x)\,dx = -\cos(x) + C\) (integral indefinida).
	Para una integral definida: \(\int_{0}^{1} (3x^4 - 5x^2 + 2)\,dx\) el sistema debe poder calcular la antiderivada simbólica si existe y evaluar el valor numérico en los límites; si la integral simbólica no es posible, debe soportar métodos numéricos (por ejemplo cuadratura).

	Expectativa del lenguaje: poder declarar expresiones integrables, solicitar integrales simbólicas (integrate) y realizar integrales definidas/numéricas (definite_integral) cuando corresponda.

- Función trigonométrica y su derivada:

	g(x) = sin(x) * cos(x)

	Derivada simbólica esperada: g'(x) = cos^2(x) - sin^2(x) (o la forma simplificada sin(2x)/2 según reglas de simplificación).

- Polinomio y derivadas:

	p(x) = 3*x^4 - 5*x^2 + 2

	Derivada simbólica: p'(x) = 12*x^3 - 10*x


Operaciones simbólicas esperadas (adiciones)

- integrate(f): devuelve la integral simbólica indefinida cuando existe.
- definite_integral(f, a, b): calcula la integral definida entre a y b, simbólicamente cuando sea posible o numéricamente como respaldo.
- is_integrable_on(f, a, b): verifica condiciones básicas de integrabilidad en el intervalo (por ejemplo continuidad salvo conjunto de medida cero) o indica la necesidad de método numérico.

Cómo encaja ANTLR4 + Python

- ANTLR4: definimos la gramática del lenguaje (tokens, precedencia, expresiones, definiciones por tramos, funciones estándar como sin/cos) y generamos el parser/lexer.
- Python: implementamos listeners o visitors para construir el AST, hacer chequeos semánticos (dominio, continuidad) y aplicar transformaciones simbólicas (derivación, simplificación). Python dispone de librerías útiles (por ejemplo SymPy) que pueden integrarse como backend para verificación/comprobación o para delegar la ingeniería simbólica más avanzada.

Impacto esperado

Al completar el proyecto tendremos una herramienta capaz de recibir expresiones simbólicas legibles, analizarlas y producir información útil (derivadas, continuidad, versión simplificada o código para evaluación numérica). Esto sienta una base sólida para posteriores extensiones, como añadir módulos de análisis simbólico avanzado o generar código de salida para simuladores y librerías numéricas.

## Objetivos

Objetivo general

Desarrollar un lenguaje de dominio específico (DSL) para expresiones matemáticas simbólicas, implementado con una gramática ANTLR4 y un backend en Python, que permita representar y manipular funciones definidas/continuas, trigonométricas y polinómicas, y realizar operaciones simbólicas como derivación, simplificación y comprobaciones de continuidad.

Objetivos específicos

- Definir la gramática mínima del lenguaje (archivo .g4) que soporte literales, variables, operadores, funciones elementales e integrales (notación para integrales indefinidas y definidas).
- Implementar el parser y lexer con ANTLR4 y generar un visitor/listener en Python que construya un AST claro y manipulable.
- Implementar operaciones simbólicas básicas sobre el AST: derivación simbólica, simplificación algebraica y trigonométrica, y comprobaciones de continuidad en puntos críticos.
- Integrar (opcionalmente) una biblioteca simbólica madura (por ejemplo SymPy) para delegar o validar transformaciones complejas y ahorrar tiempo de desarrollo.
- Crear una suite de pruebas con ejemplos (integrales simbólicas e indefinidas, funciones trigonométricas, polinomios) que verifiquen corrección de parseo y de las operaciones simbólicas.

ARQUITECTURA TÉCNICA
Stack Tecnológico
Componente				Tecnología			Versión	Propósito
Parser/Lexer			ANTLR4				4.13.2	Análisis sintáctico
Motor Matemático		SymPy				1.9	Cálculos simbólicos
Lenguaje				Python				3.9+	Implementación
Contenedor				Docker				20.10+	Portabilidad
Generación de código	LLVM(Opcional)		Optimizaciones


RESULTADOS Y PRUEBAS
Ejemplos de Funcionamiento
Expresión					Resultado					Comentario
derivada(x**2, x)			2*x							Regla de la potencia
integral(sin(x), x)			-cos(x) + C					Integral trigonométrica
derivada(sin(cos(x)), x)	-sin(x)*cos(cos(x))			Regla de la cadena
integral(x**2, x, 0, 1)		1/3							Integral definida
derivada(exp(x)*log(x), x)	exp(x)*log(x) + exp(x)/x	Regla del producto
5 + 3						8							Operación básica

Manejo de Errores
python
>>> derivada(5x, x)  # Error común
ERROR: Falta el operador * en multiplicación. Usa: 5*x en lugar de 5x

>>> derivada(x**2 x)  # Falta coma
ERROR: Faltan paréntesis, comas o argumentos

Características Pedagógicas
Constante de integración: Siempre incluye +C en integrales indefinidas

Simplificación automática: Reduce expresiones complejas

Formato legible: Resultados en notación matemática estándar

Ayuda integrada: Comando ayuda con ejemplos y sintaxis

ANÁLISIS DE RESULTADOS
Logros Alcanzados
DSL funcional completo: Gramática que cubre cálculo diferencial e integral
Motor simbólico robusto: Integración con SymPy para cálculos precisos
Interfaz de usuario intuitiva: Modos interactivo y por archivos
Portabilidad total: Contenedor Docker funcional en múltiples plataformas
Manejo de errores: Validación sintáctica y semántica
Documentación completa: Código comentado y ejemplos de uso

Limitaciones Identificadas
 Funcionalidad limitada: Solo cálculo diferencial e integral básico
 Sin optimizaciones avanzadas: No utiliza LLVM para generación de código nativo
 Interfaz textual: Sin interfaz gráfica o web
 Sin persistencia: No guarda historial de cálculos


CONCLUSIONES
Contribuciones Principales
DSL especializado: Lenguaje específico para cálculo diferencial e integral

Arquitectura modular: Separación clara entre parsing, procesamiento y salida

Solución educativa: Herramienta accesible para estudiantes de cálculo

Metodología reproducible: Proceso completo desde gramática hasta despliegue

Aplicaciones Prácticas
Educación: Verificación de ejercicios de cálculo

Investigación: Prototipado rápido de expresiones matemáticas

Ingeniería: Cálculos simbólicos en diseño técnico

Docencia: Generación de material educativo

