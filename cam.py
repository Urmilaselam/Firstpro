num_cam_sold=int(input("Enter the number of cameras sold:  "))
price_cam=int(input("Enter the price of camera: "))
salary=25000
bonus_rate=200
com_rate=0.12
bonus=bonus_rate*num_cam_sold
commision=com_rate*num_cam_sold*(price_cam*num_cam_sold)
print("bonus=", bonus)
print("commision=", commision)
print("Gross salary=",bonus+commision+salary)