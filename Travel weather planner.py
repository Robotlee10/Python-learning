distance_mi = input(int('What is your distancein miles?'))
is_raining = False
has_bike = False
has_car = False
has_ride_share_app = False
if not distance_mi:
    print(False)
elif distance_mi <=6 and has_bike and not is_raining:
    print(True)
elif distance_mi <=6 and not has_bike and is_raining:
    print(False)
elif distance_mi <=6 and not has_bike and not is_raining:
    print(False)

elif distance_mi >6 and has_car or has_ride_share_app:
    print(True)
else:
    print(False)
