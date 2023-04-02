# HackItba - Fifty Fifty

Buenos dias,

Este es el readme de la web Vivi. 
Vivi es una web que, mediante una busqueda inteligente, encontrará tu vivienda más rapido y mas facil
La idea principal del proyecto es presentar un MVP de lo que podria llegar a ser esta app que te mantiene informado de todos los alquileres que cumplen con los criterios que necesitas, ya no sos vos buscando un alquiler sino que el alquiler te busca a vos con Vivi. Fue desarrollada por el grupo de Antonella Berzzotti, Cecilia Bolaños, Tomas Curti y Gonzalo Teplizky.

## Cosas a tener a encuenta para el correcto funcionamiento de la app

1. Es necesario que esto se corra en Linux o en un entorno virtual (detallado en el proximo paso) ya que usamos el paquete de flask el cual no se puede correr en Windows :(

2.$cd hackitba-main
  $py -m pip install --upgrade pip
  $py -m pip install --user virtualenv
  $py -m venv env
  $.\env\Scripts\activate
  $pip install -r requirements.txt
  $pip install pandas
  $pip install requests
  $pip install flask

3. Correr el programa. ($python main.py)

4. Copiar http://127.0.0.1:8000 y luego pegarlo en el buscador.

5. Apareceran 2 botones, Ingresar y Registrar, vamos a asumir que ya tienen una cuenta y deciden INGRESAR con este mail con el que se registraron y al que les llegar el mail con los links.

6. Ponen su mail y su contraseña. (actualmente pueden ingresar con cualquier mail y contraseña)

7. Les aparecerán los parámetros a seleccionar, entre ellos: el barrio, el monto mínimo y máximo que desean pagar y la cantidad de ambientes. 

8. Apretar enviar y corroborar que llegue el mail al correo que pusieron.
