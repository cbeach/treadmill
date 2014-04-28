def pounds_to_kilograms(pounds):
    return 0.4536 * pounds


def miles_to_kilometers(miles):
    return 1.609344 * miles


def inches_to_centimeters(inches):
    return inches * 2.54


def kilometers_to_miles(kilometers):
    return 0.621371 * kilometers


def mph(distance, hours):
    """
        distance is in kilometers
    """
    return kilometers_to_miles(distance) / hours


def mi_per_min(distance, hours):
    """
        distance is in kilometers
    """
    return kph(distance, hours) / 0.06


def kph(distance, hours):
    """
        distance is in kilometers
    """
    return distance / hours


def get_bmr(height, weight, age, gender='male'):
    """
        Weight is in kilograms.
    """
    if gender == 'male':
        return (13.75 * weight) + (5 * height) - (6.76 * age) + 66
    elif gender == 'female':
        return (9.56 * weight) + (1.85 * height) - (4.68 * age) + 655
    else:
        raise TypeError('Gender is {}. Gender must be either "male", or "female".'.format(gender))


def gross_to_net(gross_cals, height, weight, age, gender, hours):
    rmr = get_bmr(height, weight, age, gender) * 1.1
    rmr_hours = (rmr / 24) * hours
    return gross_cals - rmr_hours


def gross_cals_burned_walking(weight, percent_grade, distance, age, hours):
    distance = float(distance)
    hours = float(hours)
    fractional_grade = float(percent_grade) / 100.0

    if percent_grade == -5:
        kcals = 0.0251 * kph(distance, hours) ** 3 - 0.2157 * kph(distance, hours) ** 2 + 0.7888 * kph(distance, hours) + 1.2957
    elif percent_grade == -4:
        kcals = 0.0244 * kph(distance, hours) ** 3 - 0.2079 * kph(distance, hours) ** 2 + 0.8053 * kph(distance, hours) + 1.3281
    elif percent_grade == -3:
        kcals = 0.0237 * kph(distance, hours) ** 3 - 0.2 * kph(distance, hours) ** 2 + 0.8217 * kph(distance, hours) + 1.3605
    elif percent_grade == -2:
        kcals = 0.023 * kph(distance, hours) ** 3 - 0.1922 * kph(distance, hours) ** 2 + 0.8382 * kph(distance, hours) + 1.3929
    elif percent_grade == -1:
        kcals = 0.0222 * kph(distance, hours) ** 3 - 0.1844 * kph(distance, hours) ** 2 + 0.8546 * kph(distance, hours) + 1.4253
    elif percent_grade == 0:
        kcals = 0.0215 * kph(distance, hours) ** 3 - 0.1765 * kph(distance, hours) ** 2 + 0.871 * kph(distance, hours) + 1.4577
    elif percent_grade == 1:
        kcals = 0.0171 * kph(distance, hours) ** 3 - 0.1062 * kph(distance, hours) ** 2 + 0.608 * kph(distance, hours) + 1.86
    elif percent_grade == 2:
        kcals = 0.0184 * kph(distance, hours) ** 3 - 0.1134 * kph(distance, hours) ** 2 + 0.6566 * kph(distance, hours) + 1.92
    elif percent_grade == 3:
        kcals = 0.0196 * kph(distance, hours) ** 3 - 0.1205 * kph(distance, hours) ** 2 + 0.7053 * kph(distance, hours) + 1.98
    elif percent_grade == 4:
        kcals = 0.0208 * kph(distance, hours) ** 3 - 0.1277 * kph(distance, hours) ** 2 + 0.7539 * kph(distance, hours) + 2.04
    elif percent_grade == 5:
        kcals = 0.0221 * kph(distance, hours) ** 3 - 0.1349 * kph(distance, hours) ** 2 + 0.8025 * kph(distance, hours) + 2.1
    else:
        kcals = (0.1 * mi_per_min(distance, hours) + 1.8 * mi_per_min(distance, hours) * fractional_grade + 3.5) * 60 * 5 / 1000

    return kcals * weight * hours


def net_cals_burned_walking(height, weight, percent_grade, distance, age, hours, gender):
    gross_cals = gross_cals_burned_walking(weight, percent_grade, distance, age, hours)
    return gross_to_net(gross_cals, height, weight, age, gender, hours)

if __name__ == '__main__':
    for i in range(1, 13):
        print '{}: {}'.format(i, net_cals_burned_walking(inches_to_centimeters(71),
            pounds_to_kilograms(240), i, miles_to_kilometers(8), 32, 4, 'male'))

