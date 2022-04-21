def mood_today(mood=""):
	if len(mood) == 0:
		return "Today, I am feeling neutral"
	else:
		return "Today, I am feeling " + mood

print(mood_today())