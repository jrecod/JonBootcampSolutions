#version 1
# distance = int(input("What is the distance if feet?: "))
# feet_to_meter = distance*.3048
# rounded = round(feet_to_meter, 4)
# print(distance, "ft is", rounded, "m")

#version 2
# distance = int(input("What is the distance? "))
# unit = input("Would you like feet(ft), miles(mi), or kilometers(km) converted into meters?: ")


# if unit == "ft":
#    converted_distance = distance/3.281
# elif unit =="mi":
#     converted_distance = distance*1609.34
# elif unit =="km":
#     converted_distance = distance*1000
# final_distance = round(converted_distance, 4)
# print(distance, unit, "is", final_distance, "m")

#version 3
# distance = int(input("What is the distance? "))
# unit = input("Would you like feet(ft), miles(mi), kilometers(km), yard(yd), or inch(in) converted into meters?: ")


# if unit == "ft":
#    converted_distance = distance/3.281
# elif unit =="mi":
#     converted_distance = distance*1609.34
# elif unit =="km":
#     converted_distance = distance*1000
# elif unit =="yd":
#     converted_distance = distance/1.0944
# elif unit =="in":
#     converted_distance = distance/39.37
# final_distance = round(converted_distance, 4)
# print(distance, unit, "is", final_distance, "m")

#version 4

#get distance and units to convert from user
distance = int(input("What is the distance? "))
input_unit = input("Input unit? Options: feet(ft), miles(mi), kilometers(km), or meters(m): ")
output_unit = input("Output unit? Options: feet(ft), miles(mi), kilometers(km), or meters(m): ")

#convert units
if input_unit == "ft" and output_unit == "m":#meter conversions
   converted_distance = distance/3.281
elif input_unit == "mi" and output_unit == "m":
    converted_distance = distance*1609.34
elif input_unit == "km" and output_unit == "m":
    converted_distance = distance*1000
elif input_unit == "ft" and output_unit == "km":#kilometer conversions
    converted_distance = distance*.000305
elif input_unit == "m" and output_unit == "km":
    converted_distance = distance/1000
elif input_unit == "mi" and output_unit == "km":
    converted_distance = distance*1.6093
elif input_unit == "mi" and output_unit == "ft":#feet conversions
    converted_distance = distance*5280
elif input_unit == "m" and output_unit == "ft":
    converted_distance = distance*3.281
elif input_unit == "km" and output_unit == "ft":
    converted_distance = distance*3280.8398
elif input_unit == "ft" and output_unit == "mi":#miles conversions
    converted_distance = distance/5280
elif input_unit == "m" and output_unit == "mi":
    converted_distance = distance/1609.34
elif input_unit == "km" and output_unit == "mi":
    converted_distance = distance*.62137

#display conversion to user
final_distance = round(converted_distance, 6)
print(distance, input_unit, "is", final_distance, output_unit)
