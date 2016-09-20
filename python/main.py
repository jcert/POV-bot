


#pin def
	#motor pins
		#motor A
21 ena
20	in1
16 in2
		#motor B
19	in3
16	in4
13	enb

	#encoder pins
		#encoder A
23 enc1
		#encoder B
22	enc2



	#make thread to poll the encoders
	#make while loop to get direction commands
		#eventually make a control system using both, so you just give global/local positions

#
on = True
while(on):
	command = raw_input("type a command: ")
   match = re.search(r"\Amove (\d*) (\d*)", command)
	if(match):
		spin(match.group(1)) #choose the wheel, 'l' or 'r'
		time.sleep(match.group(2)) #for how long it will spin in seconds?

   match = re.search(r"\Aexit", command)
	if(match):
		on = False


