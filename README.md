# Compilador-2022B 

En está parte se encontrarán todas las actividades de investigación y los reportes sobre cada parte del proyecto.

### Actividad - 1.1 Mini generador léxico

En esta parte de la actividad solo se creo lo básico del analizador lexico y lo necesario para la impresión de los datos. 

Para la parte del analizador lexico se creo una clase con este nombre la cual cuenta con su método **analizar** que recibe una cadena de texto y así determinar cuantos identificadores, números reales, números enteros o errores se encuentran (recordar que cada token debe estar separado por un espacio en blanco **' '**).

Para la parte de la impresión se realizo por consola pero fue pensado para que en futuro (si el tiempo alcanza) sea una GUI (interfaz grafica de usuario), es por ello que en la carpeta **Ventana** se pueden encontrar dos archivos una para representar la supuesta ventana y el otro un componente tabla. La ventana cuenta por el momentos con metodos muy básicos como para inicializarce, mostrar datos y leer una entrada. Por otra parte la clase **Tabla** tiene diferentes métodos para entregarle datos y darle un formato agradables a estos mismos para ser mostrados.

![01](Capturas%20Actividades/1.1/01.png "Inicio")

![01](Capturas%20Actividades/1.1/02.png "Leyendo datos")

![01](Capturas%20Actividades/1.1/03.png "Imprimiendo resultados")

### Actividad - 1.2 ¿Qué es es un analizador léxico?

#### Introducción

El compilador estar conformado por varias fases para llegar a la ejecución de ciertos programas, en este documento descubriremos de una forma resumida pero entendible que es y para que funciona una analizador léxico.

#### ¿Qué es un analizador léxico?

Esta es la primera fase de la compilación, en esta parte se encarga de leer el conjunto de caracteres que se obtinenen de la entrada del programa fuente, agrupar los lexemas y producir la salida con una secuencia de tokens. La salida se debe de enviar al analizador sintaticos para su verificación. Por lo general el analizador léxico interactua con la tabla de simbolos ya que cuando se encuentra un identificador referente a un lexema debe almacenarse en la tabla.

La siguiente imagen nos ayuda a examinar una interación rápida de los tres últimos componentes mencionados:

![01](Capturas%20Actividades/1.2/01.png)

También como el analizador léxico tiene la responsabilidad de leer el archivo principal entonces debe realizar otras tareas para encontrar los lexemas. Unas de esas tareas es eliminar todos los comentarios porque como ya sabemos esto no se compila solo es información que nos ayuda a nosotros los desarrolladores, otra tarea es eliminar espacios en blanco (tabuladores, saltos de linea y entre mas caracteres que funciones para separar tokens), y por último otra tarea puede ser llevar en contedo de los saltos de linea para ayudar a relacionar los mensajes de error que generara el compilador.
Hay dos formas de de dividir al analizador léxico:

1. **El escaneo** es la parte sencilla como eliminar comentarios o caractes blancos.
2. **El propio analizador léxico** es la parte compleja la cual se encarga de generar la salida de tokens para pasar a la siguiente fase.

#### Ventajas de separar las fases de analizador léxico y sintatico

Una de ellas es hacer tu código más limpio y así no tener fases demasiado complejas que otras. También se llega a mejorar la eficiencia, ya que se pueden aplicar tecnicas especiales que solo son utilez para el analizador léxico y no para el sintatico. Mejoramos la portabilidad. 

#### Tokens, patrones y lexemas

1. **Token:** Es una descripción clave - valor que representa de forma abstracta la unidad de un lexema, por ejemplo: if, identificador, numero, operador reacional.

2. **Patrón:** Es la regla de caracteres que describe la forma en como se puede represetar un lexema, por ejemplo '/^if$/'

3. **Lexema:** Es una secuencia de caracteres que se encuentra en el archivo fuente y que se encontro relacion con un patrón para representar un token, por ejemplo if, <=, nomUsuario.  

#### Conclusión

En esta parte conocimos la importacia del analizador léxico, que apesar de que se mire que es la fase más sencillas su existencia es muy importante para determinar si una compilación será eficiente o no.

#### Bibliografía

1. Aho, A., V. (2022). Compiladores Principios Tecnicas Y Herramientas (2.a ed.). ADDISON WESLEY LONGMAN/PEARSON.

### Actividad - 1.3 Analizador léxico completo

Para esta actividad se completo la parte analizador léxico, por lo cual ya no solo encuentra los identificadores o numeros (reales y enteros), si no que también encuentra operadores tanto relacionales, de igualdad o aritmeticos, palabras reservadas, tipos de datos, cadenas y caracteres como parentesis, llaves, etc. Para ello llamamos del analizador léxico el método **analizar** el cual recibe una cadena con todos los posibles lexemas.

![01](Capturas%20Actividades/1.3/01.png)

![02](Capturas%20Actividades/1.3/02.png)

![03](Capturas%20Actividades/1.3/03.png)

![04](Capturas%20Actividades/1.3/04.png)

![05](Capturas%20Actividades/1.3/05.png)

![05](Capturas%20Actividades/1.3/06.png)

### Actividad - 1.5 Mini Analizador Sintatico

Para esta parte se realizo la gramatica para la suma de dos o más variables. En esta parte del proyecto se incluye la clase Analizador sintatico y una estructura pila que será de gran ayuda al analizar la gramatica. Por otro lado al analizador lexico se le hizo algunas mejoras para que le pueda entregar de una manera más legible los simbolos al analizador sintatico.

#### **hola + mundo**

![01](Capturas%20Actividades/1.5/01-01.png)

![02](Capturas%20Actividades/1.5/01-02.png)

![03](Capturas%20Actividades/1.5/01-03.png)

#### **a + b + c + d + e + f**

![01](Capturas%20Actividades/1.5/02-01.png)

![02](Capturas%20Actividades/1.5/02-02.png)

![03](Capturas%20Actividades/1.5/02-03.png)

![04](Capturas%20Actividades/1.5/02-04.png)

### Actividad - 1.6 Analizador Sintáctico (Implementación usando Objetos)

En esta parte del proyecto solo se modifico la pila del analizador sintático para que ahora almacene objetos en vez de solo caracteres. Por lo cual ahora la ejecución la veremos un poco más rara ya que python imprime solo la información del objeto.

![01](Capturas%20Actividades/1.6/01.png)

![02](Capturas%20Actividades/1.6/02.png)

![03](Capturas%20Actividades/1.6/03.png)

![04](Capturas%20Actividades/1.6/04.png)

### Actividad - 1.7 Gramatica del compilador

En esta parte del proyecto se incluyo la gramatica completa, para esto se leer el archivo compilador.cvs y con ella se crea una matriz que le servida al analizador sintatico. También se realizo mejoras al todo el proyecto para que sea un código más limpio y que termine por funcionar correctamente.

![01](Capturas%20Actividades/1.7/01.png)

![02](Capturas%20Actividades/1.7/02.png)

![03](Capturas%20Actividades/1.7/03.png)

![04](Capturas%20Actividades/1.7/04.png)

![05](Capturas%20Actividades/1.7/05.png)

![06](Capturas%20Actividades/1.7/06.png)

![07](Capturas%20Actividades/1.7/07.png)

### Actividad - 1.8 Árbol sintático

Para esta parte se debio mostrar el arbol sintatico que será utilizado por el analizador semantico.

![01](Capturas%20Actividades/1.8/01.png)
![02](Capturas%20Actividades/1.8/02.png)
![03](Capturas%20Actividades/1.8/03.png)
![04](Capturas%20Actividades/1.8/04.png)
![05](Capturas%20Actividades/1.8/05.png)
![06](Capturas%20Actividades/1.8/06.png)
![07](Capturas%20Actividades/1.8/07.png)
![08](Capturas%20Actividades/1.8/08.png)
![09](Capturas%20Actividades/1.8/09.png)
![10](Capturas%20Actividades/1.8/10.png)
![11](Capturas%20Actividades/1.8/11.png)
![12](Capturas%20Actividades/1.8/12.png)
![13](Capturas%20Actividades/1.8/13.png)
![14](Capturas%20Actividades/1.8/14.png)
![15](Capturas%20Actividades/1.8/15.png)
![16](Capturas%20Actividades/1.8/16.png)
![17](Capturas%20Actividades/1.8/17.png)
![18](Capturas%20Actividades/1.8/18.png)

### Actividad - Proyecto Final
En esta sección el compilador ya debe esta terminado, yo solo pude hacer que funcionara con mi código de ejemplo
todo lo demás funciona correctamente, pero pasar el codigo a ensamblador por medio de python me llevo más tiempo de lo esperado así que si se modifica el main.c estará correcto pero el resultado en ensamblador será el mismo.

![01](Capturas%20Actividades/Final/01.png)
![02](Capturas%20Actividades/Final/02.png)
![03](Capturas%20Actividades/Final/03.png)
![04](Capturas%20Actividades/Final/04.png)
![05](Capturas%20Actividades/Final/05.png)

### Notas:

1. desplazamiento apilamos
2. reducion desapilamos
3. tope de la pila con el nombre del bloque de reducion
4. guardar en las reduciones el numero de simbolos a pop y \e se queda igual
5. si solo sale un numero en la tabla de popea igual y se compara con el simbolo
6. cuando se reduce se compara con el nombre de la reducion
7. Los objetos no terminales deben contar con un metodo mostrar y otro validar, y tener sus elementos despopeados
8. Las tablas de simbolos tendrán 3 columnas: nombre, tipo, ámbito (global, main o nomFunción)
