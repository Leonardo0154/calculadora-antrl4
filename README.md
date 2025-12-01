![LogoUPC](./logoupc.svg)
1ACC0218-2520-1733 - Teoría de Compiladores
Profesor: Peter Jonathan Montalvo Garcia

Integrantes:
| Nombres y Apellidos | Codigo | 
|------------|------------|
| Alvaro Jair Abanto Davila    | U202313540    |
| Daniel Jose Huapaya Vargas    | U202312230     | 
# Problemática y motivación.

## Problemática

Ejemplo: no existe un lenguaje específico y ampliamente estandarizado para expresar y manipular expresiones matemáticas simbólicas de forma declarativa y verificable. Aunque existen librerías y sistemas para manipulación simbólica (por ejemplo SymPy, Mathematica, Maple) y herramientas para cálculo numérico, no hay —en la práctica cotidiana— un lenguaje de dominio específico (DSL) pensado para: 1) describir de forma compacta y verificable expresiones y funciones simbólicas; 2) combinar especificaciones simbólicas de funciones (por ejemplo piezas a trozos, funciones elementales); y 3) operar algebraicamente sobre esas expresiones (simplificación, derivación, comprobación de continuidad o dominio).

Por qué es importante

- Reproducibilidad y legibilidad: un DSL permite expresar definiciones matemáticas de manera concisa, legible y versionable, lo que facilita compartir y revisar especificaciones.
- Verificación y análisis simbólico: con una representación simbólica es posible demostrar propiedades (p. ej. continuidad, existencia de límites, integrabilidad) o transformar expresiones antes de evaluarlas numéricamente.
- Integración con herramientas: un lenguaje bien definido facilita la generación automática de código para librerías numéricas, la exportación a formatos simbólicos y la integración con sistemas de computación algebraica.

¿Existe y es un proceso largo?

Existen sistemas y bibliotecas consolidadas para manipulación simbólica y cálculo, pero no un estándar exclusivo para un DSL orientado a expresiones matemáticas simbólicas con enfoque en integración con herramientas de compilación y análisis estático. Diseñar e implementar un DSL completo es un proceso de varias fases: diseño del dominio y la gramática, implementación del parser (por ejemplo con ANTLR4), representación interna (AST), chequeos semánticos y verificación, y por último la implementación de un intérprete o generador de código. Dependiendo del alcance (solo sintaxis y parseo vs. resolución simbólica y generación de código optimizado), el esfuerzo puede variar desde unas semanas (prueba de concepto) hasta varios meses (herramienta robusta y documentada).

Relación con el trabajo propuesto

Nuestro proyecto propone crear un lenguaje para expresiones matemáticas simbólicas (en ANTLR4 con backend en Python) que permita, entre otras cosas, describir funciones definidas y continuas, funciones trigonométricas y polinómicas, y operar sobre ellas (por ejemplo, derivación simbólica). Esta capacidad simbólica habilita análisis simbólico, generación de código y usos pedagógicos en cálculo simbólico.

## Motivación

Objetivo general

Desarrollar un lenguaje de dominio específico (DSL) para expresiones matemáticas simbólicas usando ANTLR4 para la gramática y Python como backend. El lenguaje deberá permitir representar y manipular simbólicamente funciones:

- Definidas y continuas (por ejemplo funciones a trozos con condiciones sobre el dominio).
- Trigonométricas (sin, cos, tan y combinaciones) con simplificación y derivación simbólica.
- Polinómicas y sus derivadas, con operaciones algebraicas básicas (suma, producto, potencia).

Motivaciones concretas

1. Claridad y expresividad: Los usuarios podrán escribir expresiones matemáticas complejas de forma legible y estándar, evitando ambigüedades que aparecen al codificar la misma lógica numéricamente.
2. Automatización de análisis: Con un AST simbólico se pueden automatizar tareas como comprobar continuidad, encontrar derivadas simbólicas, o simplificar expresiones antes de evaluarlas numéricamente.
3. Reutilización en aplicaciones científicas y de ingeniería: Al poder expresar funciones simbólicamente, se facilita su incorporación en pipelines de análisis, optimización y la generación de código para librerías numéricas.
4. Aprendizaje y enseñanza: Un DSL sencillo sirve como herramienta pedagógica para explicar conceptos de cálculo simbólico y análisis matemático.

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







