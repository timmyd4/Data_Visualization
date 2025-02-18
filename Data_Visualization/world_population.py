import json

from pygal_maps_world.maps import World
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle
from country_codes import get_country_code


filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)


cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            # print(code + ": " + str(population))
            cc_populations[code] = population
        else:
            print('ERROR - ' + country_name)


cc_pops_1 = {}
cc_pops_2 = {}
cc_pops_3 = {}

for cc, pop in cc_populations.items():
    if pop < 100000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop


print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

#wm = world for pygal.worldmap
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = World(style=wm_style)

wm.title = 'World Population in 2010, by Country'

wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')