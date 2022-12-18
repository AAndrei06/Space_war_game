#	About This Game:
# *****************************************************************
# *   Game  Name : Space War                                                          
# *   Screen Size: 900 x 700 (px)                                                        
# *   Enemies:   2                                                                                 
# *   Space Craft: 1		   		 														      
# *   Space Craft Speed 1-30							     			                 
# *   Space Craft Lives : 4																	 
# *   Include A Radar,Scoring and others										
# *																										 																										 																										 
# ****************************************************************

# Space War

import turtle 
import time
import random
import tkinter

error = False
var = False


try:

	# ********************************************Screen**************************************

	window=turtle.Screen()
	window.setup(900,700)
	window.bgcolor("#1C002D")
	window.title("SPACE WAR")
	try:
		window.bgpic("earth.gif")
	except:
		var = True

	try:
		img = tkinter.Image("photo", file="rocket.png")
		turtle._Screen._root.iconphoto(True, img)
	except:
		if error == False:
			error = True
		else:
			error = False
	window.tracer(0)


	#  **************************************Second Screen***************************************

	screen2=turtle.Turtle()
	screen2.color("#274B6B")
	screen2.penup()
	screen2.shape("square")
	screen2.setposition(342,5)
	screen2.shapesize(34.5,10)
	screen2.stamp()
	screen2.hideturtle()

	# ******************************************Radar************************************************

	radar=turtle.Turtle()
	radar.color("#266D26")
	radar.shape("square")
	radar.penup()
	radar.speed(0)
	radar.shapesize(7,7.3)
	radar.setposition(342,-200)


	penr=turtle.Turtle()
	penr.color("#FF8400")
	penr.penup()
	penr.goto(290,-130)
	penr.write("Radar:",font=("Calibry",20))
	penr.hideturtle()
	penr.penup()
	penr.goto(255,-45)
	penr.write("Rocket Speed: 0.5-5 ",font=("Arial",14))
	penr.goto(255,300)
	penr.write("Rocket Control:",font=("Arial",18))
	penr.goto(255,270)
	penr.write("Left Arrow Key: Turn Left",font=("Arial",12))
	penr.goto(255,250)
	penr.write("Right Arrow Key: Turn Right",font=("Arial",11))
	penr.goto(255,230)
	penr.write("Space: Shoot",font=("Arial",12))
	penr.goto(255,210)
	penr.write("'W' key: increase speed",font=("Arial",12))
	penr.goto(255,180)
	penr.write("'S' key: decrease speed",font=("Arial",12))

	# ****************************************Sprites on Radar***************************************

	med=turtle.Turtle()
	med.color("#BDFF00")
	med.shape("circle")
	med.penup()
	med.speed()
	med.shapesize(0.5,0.5,2)
	med.setposition(random.randint(-400,200),random.randint(-300,300))

	s=turtle.Turtle()
	s.color("blue")
	s.shape("circle")
	s.penup()
	s.speed(0)
	s.shapesize(0.3,0.3,1)

	e=turtle.Turtle()
	e.shapesize(0.3,0.3,1)
	e.speed(0)
	e.penup()
	e.color("red")
	e.shape("circle")

	e1=turtle.Turtle()
	e1.shapesize(0.3,0.3,1)
	e1.speed(0)
	e1.penup()
	e1.color("red")
	e1.shape("circle")

	e2=turtle.Turtle()
	e2.shapesize(0.3,0.3,1)
	e2.penup()
	e2.speed(0)
	e2.color("red")
	e2.shape("circle")

	e3=turtle.Turtle()
	e3.shapesize(0.3,0.3,1)
	e3.penup()
	e3.speed(0)
	e3.color("red")
	e3.shape("circle")

	e4=turtle.Turtle()
	e4.shapesize(0.3,0.3,1)
	e4.penup()
	e4.speed(0)
	e4.color("red")
	e4.shape("circle")

	e5=turtle.Turtle()
	e5.shapesize(0.3,0.3,1)
	e5.speed(0)
	e5.penup()
	e5.color("red")
	e5.shape("circle")

	e6=turtle.Turtle()
	e6.shapesize(0.3,0.3,1)
	e6.speed(0)
	e6.penup()
	e6.color("red")
	e6.shape("circle")


	# *********************************** Variables ***********************************************************

	speed=1
	space_craft_heading = 90
	enemy_speed = 1.3
	is_paused = False
	lives = 4
	health_bar_color ="green"
	health_bar_width = 0.1
	health_bar_height = 1
	score = 0

	# ************************************** Pen  *********************************************************************
	pen=turtle.Turtle()
	pen.color("#C97712")
	pen.penup()
	pen.goto(-200,0)
	pen.hideturtle()
	pen.goto(270,30)
	pen.write("Score: {}".format(score),font=("Arial",24))

	# *************************************** Pen 2 **************************************************************
	pen2=turtle.Turtle()
	pen2.color("#C97712")
	pen2.penup()
	pen2.hideturtle()
	pen2.goto(270,-10)
	pen2.write("Lives: {}".format(lives),font=("Arial",24))

	# **************************************** Border ***************************************************************

	border=turtle.Turtle()
	border.color("white")
	border.penup()
	border.setposition(-446,-340)
	border.pendown()
	border.width(6)
	border.speed(0)

	for line in range(2):
		border.forward(887)
		border.left(90)
		border.forward(688)
		border.left(90)
		
	border.penup()
	border.goto(246,-340)
	border.setheading(90)
	border.pendown()
	border.forward(685)
	border.hideturtle()
		
	# ***************************************Space Craft*****************************************************

	space_craft=turtle.Turtle()
	space_craft.penup()
	space_craft.color("#2965A8")
	space_craft.shape("triangle")
	space_craft.setheading(space_craft_heading)
	space_craft.speed(0)
	space_craft.shapesize(1,1.5,3)

	# *****************************************Bullet*******************************************************
	bullet=turtle.Turtle()
	bullet.color("yellow")
	bullet.shape("circle")
	bullet.penup()
	bullet.speed(1)
	bullet.shapesize(0.3,0.3,2)
	bullet.hideturtle()
	bullet_state="ready"

	# ****************************************Health Bar************************************************

	bar=turtle.Turtle()
	bar.color(health_bar_color)
	bar.shape("square")
	bar.penup()
	bar.speed(0)
	bar.shapesize(health_bar_width,health_bar_height,3)

	# ******************************************Enemies*************************************************

	enemy=turtle.Turtle()
	enemy.color("#5F7D00")
	enemy.shape("square")
	enemy.shapesize(1.3,1.3,2)
	enemy.penup()
	enemy_x=random.randint(-430,200)
	enemy_y=random.randint(-330,330)
	enemy.speed(0)
	enemy.setheading(180)
	enemy.setposition(enemy_x,enemy_y)


	enemy1=turtle.Turtle()
	enemy1.color("#2D7A00")
	enemy1.shape("square")
	enemy1.shapesize(1.3,1.3,2)
	enemy1.penup()
	enemy1_x=random.randint(-430,200)
	enemy1_y=random.randint(-330,330)
	enemy1.speed(0)
	enemy1.setheading(180)
	enemy1.setposition(enemy1_x,enemy1_y)


	enemy2=turtle.Turtle()
	enemy2.color("#5F7D00")
	enemy2.shape("square")
	enemy2.shapesize(1.3,1.3,2)
	enemy2.penup()
	enemy2.speed(0)
	enemy2_x=random.randint(-430,200)
	enemy2_y=random.randint(-330,330)
	enemy2.setheading(70)
	enemy2.setposition(enemy2_x,enemy2_y)


	enemy3=turtle.Turtle()
	enemy3.color("#2D7A00")
	enemy3.shape("square")
	enemy3.shapesize(1.3,1.3,2)
	enemy3.penup()
	enemy3_x=random.randint(-430,200)
	enemy3_y=random.randint(-330,330)
	enemy3.speed(0)
	enemy3.setheading(270)
	enemy3.setposition(enemy3_x,enemy3_y)


	enemy4=turtle.Turtle()
	enemy4.color("#5F7D00")
	enemy4.shape("square")
	enemy4.shapesize(1.3,1.3,2)
	enemy4.penup()
	enemy4_x=random.randint(-430,200)
	enemy4_y=random.randint(-330,330)
	enemy4.speed(0)
	enemy4.setheading(200)
	enemy4.setposition(enemy4_x,enemy4_y)


	enemy5=turtle.Turtle()
	enemy5.color("#2D7A00")
	enemy5.shape("square")
	enemy5.shapesize(1.3,1.3,2)
	enemy5.penup()
	enemy5_x=random.randint(-430,200)
	enemy5_y=random.randint(-330,330)
	enemy5.speed(0)
	enemy5.setheading(120)
	enemy5.setposition(enemy5_x,enemy5_y)


	enemy6=turtle.Turtle()
	enemy6.color("#2D7A00")
	enemy6.shape("square")
	enemy6.shapesize(1.3,1.3,2)
	enemy6.penup()
	enemy6_x=random.randint(-431,200)
	enemy6_y=random.randint(-330,330)
	enemy6.speed(0)
	enemy6.setheading(0)
	enemy6.setposition(enemy6_x,enemy6_y)

	# *******************************************Functions***********************************************

	def turn_left():
		global space_craft_heading
		space_craft_heading +=30
		
	def turn_right():
		global space_craft_heading
		space_craft_heading -=30
		
	def increase_speed1():
		global speed
		speed +=1
		if speed >=6:
			speed=5
			
	def decrease_speed():
		global speed
		speed-=1
		if speed < 0.5:
			speed = 0.5
		
		
	def fire():
		global bullet_state
		if bullet_state =="ready":
			bullet_state="fire"
			
			

	# ***********************************************Keyboard****************************************
	turtle.listen()
	turtle.onkeypress(turn_left,"Left")
	turtle.onkeypress(turn_right,"Right")
	turtle.onkeypress(increase_speed1,"w")
	turtle.onkeypress(fire,"space")
	turtle.onkeypress(decrease_speed,"s")

		
	# **********************************************MAIN LOOP****************************************
	time.sleep(1)

	while True:
		window.update()
		
	#*******************************************Medkit collision with Space Craft*****************
		
		if med.distance(space_craft) <20:
			lives+=1
			med.setposition(random.randint(-400,200),random.randint(-300,300))
			pen2.clear()
			pen2.write("Lives: {}".format(lives),font=("Arial",24))
			
		
	# *******************************************Sprites on Radar*************************************
		x=space_craft.xcor()
		y=space_craft.ycor()
		s.setposition((x / 7)+30 + 320,(y/6)-200)
		
		x=enemy.xcor()
		y=enemy.ycor()
		e.setposition((x / 7)+30 + 320,(y/6)-200)
		
		x=enemy1.xcor()
		y=enemy1.ycor()
		e1.setposition((x / 7)+30 + 320,(y/6)-200)
		
		x=enemy2.xcor()
		y=enemy2.ycor()
		e2.setposition((x / 7)+30 + 320,(y/6)-200)
		
		x=enemy3.xcor()
		y=enemy3.ycor()
		e3.setposition((x / 7)+30 + 320,(y/6)-200)
		
		x=enemy4.xcor()
		y=enemy4.ycor()
		e4.setposition((x / 7)+30 + 320,(y/6)-200)
		
		x=enemy5.xcor()
		y=enemy5.ycor()
		e5.setposition((x / 7)+30 + 320,(y/6)-200)
		
		x=enemy6.xcor()
		y=enemy6.ycor()
		e6.setposition((x / 7)+30 + 320,(y/6)-200)
		
		
	# ************************************************Health Bar******************************************
		
		space_x=space_craft.xcor()
		space_y=space_craft.ycor()
		bar.setposition(space_x,space_y + 17)
		
	# *********************************************Enemy Movement*****************************************

		enemy.forward(enemy_speed)
		enemy1.forward(enemy_speed)
		enemy2.forward(enemy_speed)
		enemy3.forward(enemy_speed)
		enemy4.forward(enemy_speed)
		enemy5.forward(enemy_speed)
		enemy6.forward(enemy_speed)
		
	# *********************************Firing Bullet and Collision with Enemies********************************

		if bullet_state =="fire":
			space_xb=space_craft.xcor()
			space_yb=space_craft.ycor()
			bullet.setheading(space_craft_heading)
			bullet.setposition(space_xb,space_yb)
			bullet.showturtle()
			for i  in range(25):
				bullet.forward(20)
				bullet.stamp()
				if bullet.distance(enemy) < 30:
					bullet.setposition(400,400)
					enemy.setposition(random.randint(-430,200),random.randint(-300,300))
					score+=10
					pen.clear()
					pen.write("Score: {}".format(score),font=("Arial",24))
				if bullet.distance(enemy1) < 30:
					bullet.setposition(400,400)
					enemy1.setposition(random.randint(-430,200),random.randint(-300,300))
					score+=10
					pen.clear()
					pen.write("Score: {}".format(score),font=("Arial",24))
				if bullet.distance(enemy2) < 30:
					bullet.setposition(400,400)
					enemy2.setposition(random.randint(-430,200),random.randint(-300,300))
					score+=10
					pen.clear()
					pen.write("Score: {}".format(score),font=("Arial",24))
				if bullet.distance(enemy3) < 30:
					bullet.setposition(400,400)
					enemy3.setposition(random.randint(-430,200),random.randint(-300,300))
					score+=10
					pen.clear()
					pen.write("Score: {}".format(score),font=("Arial",24))
				if bullet.distance(enemy4) < 30:
					bullet.setposition(400,400)
					enemy4.setposition(random.randint(-430,200),random.randint(-300,300))
					score+=10
					pen.clear()
					pen.write("Score: {}".format(score),font=("Arial",24))
				if bullet.distance(enemy5) < 30:
					bullet.setposition(400,400)
					enemy5.setposition(random.randint(-430,200),random.randint(-300,300))
					score+=10
					pen.clear()
					pen.write("Score: {}".format(score),font=("Arial",24))
				if bullet.distance(enemy6) < 30:
					bullet.setposition(400,400)
					enemy6.setposition(random.randint(-430,200),random.randint(-300,300))
					score+=10
					pen.clear()
					pen.write("Score: {}".format(score),font=("Arial",24))
				bullet.setposition(bullet.xcor(),bullet.ycor())
			time.sleep(0.1)
			bullet.clear()
			bullet.setposition(400,400)
			bullet.hideturtle()
			bullet_state="ready"
		
	#**************************************Collision with enemies*****************************************
		
		if enemy.distance(space_craft) < 30:
			time.sleep(0.5)
			space_craft.setpos(0,0)
			lives=lives-1
			pen2.clear()
			pen2.write("Lives: {}".format(lives),font=("Arial",24))
			
		if enemy1.distance(space_craft) < 30:
			time.sleep(0.5)
			space_craft.setpos(0,0)
			lives = lives-1
			pen2.clear()
			pen2.write("Lives: {}".format(lives),font=("Arial",24))
			
		if enemy2.distance(space_craft) < 30:
			time.sleep(0.5)
			space_craft.setpos(0,0)
			lives = lives-1
			pen2.clear()
			pen2.write("Lives: {}".format(lives),font=("Arial",24))
			
		if enemy3.distance(space_craft) < 30:
			time.sleep(0.5)
			space_craft.setpos(0,0)
			lives = lives-1
			pen2.clear()
			pen2.write("Lives: {}".format(lives),font=("Arial",24))
			
		if enemy4.distance(space_craft) < 30:
			time.sleep(0.5)
			space_craft.setpos(0,0)
			lives = lives-1
			pen2.clear()
			pen2.write("Lives: {}".format(lives),font=("Arial",24))
			
		if enemy5.distance(space_craft) < 30:
			time.sleep(0.5)
			space_craft.setpos(0,0)
			lives = lives-1
			pen2.clear()
			pen2.write("Lives: {}".format(lives),font=("Arial",24))
			
		if enemy6.distance(space_craft) < 30:
			time.sleep(0.5)
			space_craft.setpos(0,0)
			lives = lives-1
			pen2.clear()
			pen2.write("Lives: {}".format(lives),font=("Arial",24))
			
		if lives >= 5:
			health_bar_color="#00FFD8"
			bar.color(health_bar_color)
			health_bar_height=1.2
			bar.shapesize(health_bar_width,health_bar_height,3)
			
		if lives == 4:
			health_bar_color="green"
			bar.color(health_bar_color)
			health_bar_height=1
			bar.shapesize(health_bar_width,health_bar_height,3)
			
			
		if lives == 3:
			health_bar_color="yellow"
			health_bar_height=0.75
			bar.color(health_bar_color)
			bar.shapesize(health_bar_width,health_bar_height,3)
			
		if lives == 2:
			health_bar_color="orange"
			health_bar_height=0.6
			bar.color(health_bar_color)
			bar.shapesize(health_bar_width,health_bar_height,3)
			
		if lives == 1:
			health_bar_color="red"
			health_bar_height=0.4
			bar.color(health_bar_color)
			bar.shapesize(health_bar_width,health_bar_height,3)
			
		if lives == 0:
			bar.hideturtle()
			pen.color("#FF8400")
			pen.goto(-150,0)
			pen.pendown()
			pen.write("Game Over",align="center",font=("Arial Black",50))	
			pen.penup()
			pen.hideturtle()	
			break
			
	#********************************Collision with border and enemies**********************************
		
		if enemy.xcor() > 230:
			enemy.setheading(random.randint(100,200))
		if enemy.xcor() < -430:
			enemy.setheading(random.randint(-70,30))
		if enemy.ycor() > 320:
			enemy.setheading(random.randint(200,360))
		if enemy.ycor() < -320:
			enemy.setheading(random.randint(20,160))
		
		if enemy1.xcor() > 230:
			enemy1.setheading(random.randint(100,200))
		if enemy1.xcor() < -430:
			enemy1.setheading(random.randint(-70,30))
		if enemy1.ycor() > 320:
			enemy1.setheading(random.randint(200,360))
		if enemy1.ycor() < -320:
			enemy1.setheading(random.randint(20,160))	
		
		if enemy2.xcor() > 230:
			enemy2.setheading(random.randint(100,200))
		if enemy2.xcor() < -430:
			enemy2.setheading(random.randint(-70,30))
		if enemy2.ycor() > 320:
			enemy2.setheading(random.randint(200,360))
		if enemy2.ycor() < -320:
			enemy2.setheading(random.randint(20,160))
			
		if enemy3.xcor() > 230:
			enemy3.setheading(random.randint(100,200))
		if enemy3.xcor() < -430:
			enemy3.setheading(random.randint(-70,30))
		if enemy3.ycor() > 320:
			enemy3.setheading(random.randint(200,360))
		if enemy3.ycor() < -320:
			enemy3.setheading(random.randint(20,160))
			
		if enemy4.xcor() > 230:
			enemy4.setheading(random.randint(100,200))
		if enemy4.xcor() < -430:
			enemy4.setheading(random.randint(-70,30))
		if enemy4.ycor() > 320:
			enemy4.setheading(random.randint(200,360))
		if enemy4.ycor() < -320:
			enemy4.setheading(random.randint(20,160))
		
		if enemy5.xcor() > 230:
			enemy5.setheading(random.randint(100,200))
		if enemy5.xcor() < -430:
			enemy5.setheading(random.randint(-70,30))
		if enemy5.ycor() > 320:
			enemy5.setheading(random.randint(200,360))
		if enemy5.ycor() < -320:
			enemy5.setheading(random.randint(20,160))
			
		if enemy6.xcor() > 230:
			enemy6.setheading(random.randint(100,200))
		if enemy6.xcor() < -430:
			enemy6.setheading(random.randint(-70,30))
		if enemy6.ycor() > 320:
			enemy6.setheading(random.randint(200,360))
		if enemy6.ycor() < -320:
			enemy6.setheading(random.randint(20,160))
			
	#*************************************Space Craft Movement******************************************

		space_craft.forward(speed)
		space_craft.setheading(space_craft_heading)
		
	#********************************Collision with border and space craft********************************
		
		if space_craft.xcor() > 240:
			space_craft_heading=180
			
		if space_craft.xcor() < -440:
			space_craft_heading=0
				
		if space_craft.ycor() > 330:
			space_craft_heading= 270
			
		if space_craft.ycor() < -330:
			space_craft_heading=90
				


	turtle.mainloop()

except:
	error = True

