import turtle
import time
import random
from playsound import playsound
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#Variables Iniciales
posponer=0.15
timer=0
reloj=60
contador = 0
cronometro = 0

#Configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego de la Cuarentena")
wn.setup(width = 600, height = 600)
wn.bgpic(resource_path("casa.png"))
wn.update()
wn.tracer(0)

#Imagenes del Juego
image = resource_path("player.gif")
image2 = resource_path("player2.gif")
imgpizza = resource_path("pizza.gif")
imgcupcake = resource_path("cupcake.gif")
imghamburguer = resource_path("hamburguer.gif")
imghotdog = resource_path("hotdog.gif")
imghelado = resource_path("helado.gif")
imgdonut = resource_path("donut.gif")
imgmensaje = resource_path("instrucciones.gif")
imgreloj = resource_path("Reloj.gif")
imgnumeros = [resource_path("cero.gif"),resource_path("uno.gif"),resource_path("dos.gif"),resource_path("tres.gif"),resource_path("cuatro.gif"),resource_path("cinco.gif"),resource_path("seis.gif"),resource_path("siete.gif"),resource_path("ocho.gif"),resource_path("nueve.gif")]
imgh1 = resource_path("homen1.gif")
imgh2 = resource_path("homen2.gif")
imgh3 = resource_path("homen3.gif")
imgh4 = resource_path("homen4.gif")

#Cargar las imagenes
wn.addshape(image)
wn.addshape(image2)
wn.addshape(imgpizza)
wn.addshape(imgcupcake)
wn.addshape(imghamburguer)
wn.addshape(imghotdog)
wn.addshape(imghelado)
wn.addshape(imgdonut)
wn.addshape(imgmensaje)
wn.addshape(imgh1)
wn.addshape(imgh2)
wn.addshape(imgh3)
wn.addshape(imgh4)
wn.addshape(imgreloj)
for item in range(len(imgnumeros)):
	wn.addshape(imgnumeros[item])

#Cabeza del Jugador
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape(image)
cabeza.color("white")
cabeza.penup()
cabeza.goto(120,-150)
cabeza.direction = "stop"

#Cuerpo del Jugador
cuerpo = turtle.Turtle()
cuerpo.speed(0)
cuerpo.shape(imgh1)
cuerpo.penup()
cuerpo.goto(125,-220)
cuerpo.direction = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape(imghamburguer)
comida.penup()
comida.goto(-100,80)

#Mensaje Inicial
mensaje = turtle.Turtle()
mensaje.speed(0)
mensaje.shape(imgmensaje)
mensaje.penup()
mensaje.goto(140,-70)

#Fondo del Reloj
freloj = turtle.Turtle()
freloj.speed(0)
freloj.shape(imgreloj)
freloj.penup()
freloj.goto(0,235)

#Numeros del Reloj
digito1 = turtle.Turtle()
digito1.speed(0)
digito1.shape(imgnumeros[6])
digito1.penup()
digito1.goto(-20,225)
digito2 = turtle.Turtle()
digito2.speed(0)
digito2.shape(imgnumeros[0])
digito2.penup()
digito2.goto(18,225)

#Funciones
def arriba():
	cabeza.shape(image)
	if mensaje.isvisible(): mensaje.hideturtle()
	cabeza.direction = "up"
def abajo():
	cabeza.shape(image)
	if mensaje.isvisible(): mensaje.hideturtle()
	cabeza.direction = "down"
def izquierda():
	cabeza.shape(image)
	if mensaje.isvisible(): mensaje.hideturtle()
	cabeza.direction = "left"
def derecha():
	cabeza.shape(image)
	if mensaje.isvisible(): mensaje.hideturtle()
	cabeza.direction = "right"

def actualizar_reloj(tiempo):
	if tiempo>=0:
		if 0<=tiempo<=9:  
			digito1.shape(imgnumeros[0])
			digito2.shape(imgnumeros[tiempo])
		else:
			tempo=str(tiempo)
			tiempo1=int(tempo[0:1])
			tiempo2=int(tempo[1:2])
			digito1.shape(imgnumeros[tiempo1])
			digito2.shape(imgnumeros[tiempo2])
	else:		
		#Fin del Juego
		cabeza.direction="stop"
		cuerpo.direction="stop"
		wn.bgpic(resource_path("casa2.png"))
		wn.update()
		turtle.color('deep pink')
		style = ('Courier', 14, 'italic', "bold")
		turtle.penup()
		turtle.goto(0,-40)
		turtle.write('        Felicidades! \n Tú conseguiste ' + str(contador) + ' comidas! \n Pero yo subí ' + str(contador*2) + ' kilos :)', font=style, align="center", move = True)

def mov():
	if cabeza.direction == "up":
		y = cabeza.ycor()
		cabeza.sety(y + 20)
		cuerpo.sety(y - 50)

	if cabeza.direction == "down":
		y = cabeza.ycor()
		cabeza.sety(y - 20)
		cuerpo.sety(y - 90)

	if cabeza.direction == "left":
		x = cabeza.xcor()
		cabeza.setx(x - 20)
		cuerpo.setx(x - 15)

	if cabeza.direction == "right":
		x = cabeza.xcor()
		cabeza.setx(x + 20)
		cuerpo.setx(x + 25)

#Escuchar Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while cronometro > -5:
	wn.update()
	#Interseccion con las comidas
	if cabeza.distance(comida) < 40:
		cabeza.shape(image2)
		x = random.randint(-260,260)
		y = random.randint(-260,260)
		z = random.choices('hpdcsu')
		contador+=1
		if z[0] == 'h': comida.shape(imghamburguer)
		if z[0] == 'c': comida.shape(imgcupcake)
		if z[0] == 'p': comida.shape(imgpizza)
		if z[0] == 'd': comida.shape(imghotdog)
		if z[0] == 's': comida.shape(imghelado)
		if z[0] == 'u': comida.shape(imgdonut)
		comida.goto(x,y)

	#Cambiar el cuerpo
	if 1 <= contador < 5: cuerpo.shape(imgh1)
	if 5 <= contador < 10: cuerpo.shape(imgh2)
	if 10 <= contador < 15: cuerpo.shape(imgh3)
	if 15 <= contador: cuerpo.shape(imgh4)

	if cronometro >= 0: mov()
	time.sleep(posponer)
	#Iniciar el juego
	if mensaje.isvisible() == False:
		if timer == 0: playsound(resource_path("Cuarentena.wav"), False) 		 
		timer=timer+0.185
		cronometro=int(round(int(round((reloj-timer),0))))
		print(cronometro)
		actualizar_reloj(cronometro)
