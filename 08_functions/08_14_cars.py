car_info = {}
manufacturer = ''
model = ''

def make_car(manufacturer, model, **car_info):
    '''Build profile about a car'''
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car_info = make_car('honda', 'accord',
                    year = '2012',
                    trim = 'SE')

print(car_info)