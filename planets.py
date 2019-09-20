def weight_on_planets():
   weight = input("What do you weigh on earth? ")
   weight = int(weight)
   print("\nOn Mars you would weigh", weight*0.38, "pounds.\nOn Jupiter you would weigh", weight*2.34, "pounds.") 
   
if __name__ == '__main__':
   weight_on_planets()
