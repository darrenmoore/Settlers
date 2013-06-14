from random import randint
from random import choice
import thread
import time
#from scipy.spatial import KDTree

resources = {
	'coal': 	{ 'min':5, 'max':50 },
	'lumber': 	{ 'min':5, 'max':50 },
	'stone': 	{ 'min':5, 'max':50 },
	'iron': 	{ 'min':5, 'max':50 },
	'gold' : 	{ 'min':5, 'max':50 }
}

buildings = {
	'house': {
		'requires': {
			'lumber': 20
		},
		'ticks': 20
	},
	'barracks': {
	},
	'gold_mine': {},
	'stone_quarry': {},
	'lumber_mill': {},
	'laboratory': {},
	'harbour': {},
	'storehouse': {},
	'stone_wall': {},
	'watch_tower': {}
}

ships = {
	'warship': {},
	'merchant': {},
	'collisation': {},
	'spy': {}
}

people = {
	'normal': { 'attack':1, 'defense':1 },
	'spearfighter': {},
	'archer': {},
	'catapault': {},
	'scientist': {},
}

tech = {
}

stockhold = {}


min_island_size = 20;
max_island_size = 50;
max_islands = 3;
max_world_size = 40;
tick_count = 0;

current_island = 0;

player = {
	'user': {},
	'alliances': [],
	'islands': [],
	'stockhold': [],
	'ships': [],
	'buildings': [],
}
map = []
islands = []
events = []


def main():
	print "Settlers!"
	createWorld();
	createStockhold();
	printMap();
	printIslandDetail();
	printIslandResources();
	start();
	return


def start():
	#eventRaining
	events.append({ 'ticks':10, 'method':eventWeather, 'args':{ 'name':'raining' } });
	events.append({ 'ticks':20, 'method':eventWeather, 'args':{ 'name':'sunny' } });

	#Put the ticker into a thread
	thread.start_new_thread( ticker, () )

	#Take user input
	cli();
	return


def cli():
	print '> Type help'

	while True:
		cmd = raw_input(":");

		if cmd == 'quit' or cmd == 'q' or cmd == 'exit':
			print "See ya!"
			break
		elif cmd == 'help':
			printHelp()
		elif cmd == 'map':
			printMap()
		elif cmd == 'resources':
			printIslandResources()
		elif cmd == 'island':
			printIslandDetail()
		elif cmd == 'chopLumber':
			chopLumber()
		elif cmd == 'stockhold':
			printStockhold()


def ticker():
	global tick_count
	while True:
		tick_count += 1;
		#print 'Tick tock: '+str(tick_count)
		checkEvents(tick_count);
		time.sleep( 1 );
	return


def checkEvents(count):
	for e in events:
		if e['ticks'] == count:
			e['method'](e['args'])

			if 'repeat' in e and e['repeat']:
				addEvent(e['repeat'], e['method'], e['args'], e['repeat'])

			#events.remove(e)

	return


def printHelp():
	print '> map'
	print '> resources'
	print '> island'
	print '> stockhold'
	print '> chopLumber'
	print '> quit'


def createWorld():
	del map[:]
	for rows in range(max_world_size):
		line = []
		for cols in range(max_world_size):
			line.append({});
		map.append(line);

	for i in range(0,max_islands):
		createIsland({ 'size':{ 'min':min_island_size, 'max':max_island_size } })

	return;


def createIsland(options):
	island_id = len(islands);
	size = randint(options['size']['min'],options['size']['max'])

	islands.append({
		'name': 'Island ' + str(island_id),
		'size': size,
		'cells': []
	});

	#create an initial cell to start from
	coords = findEmptyCell()
	createCell(coords, island_id)

	#create branches from this cell
	branchCell(coords, island_id, 0, size);
	return;


def branchCell(coords, island_id, depth = 0, max_depth = 0):
	n = emptyNeighbours(coords);

	#if no neighbours get out of here
	if not n:
		return depth

	randCoords = choice(n)
	createCell(randCoords, island_id)

	depth += 1
	if depth < max_depth:
		#either branch from random or these coords
		branchFrom = coords
		if randint(0,1):
			branchFrom = randCoords

		return branchCell(branchFrom, island_id, depth, max_depth);
	
	return depth



def emptyNeighbours(coords):
	n = neighbours(coords)

	for cell in n:
		if not isEmptyCell(cell):
			n.remove(cell)
	return n


def neighbours(coords):
	n = [];

	#top
	for x in range(coords['x']-1,coords['x']+2):
		n.append({ 'x':x, 'y':coords['y']-1 })

	#bottom
	for x in range(coords['x']-1,coords['x']+2):
		n.append({ 'x':x, 'y':coords['y']+1 })

	#left and right
	n.append({ 'x':coords['x']-1, 'y':coords['y'] })
	n.append({ 'x':coords['x']+1, 'y':coords['y'] })

	#remove anything out of range
	output = [];
	for cell in n:
		if(cell['x'] >= 0 and cell['x'] < max_world_size and cell['y'] >= 0 and cell['y'] < max_world_size):
			output.append(cell)

	return output


def randomNeighbour(coords):
	x = randint(coords['x']-1, coords['x']+1)
	y = randint(coords['y']-1, coords['y']+1)
	return { 'x':x, 'y':y }


def createCell(coords, island_id):
	#random resources
	_resources = randomResources();

	save = {
		'x': coords['x'],
		'y': coords['y'],
		'resources': _resources
	}

	#add to islands
	islands[island_id]['cells'].append(save);

	#add to map
	#fix this, island_id should always be above 0, but for testing it's currently 0 so it doesn't register
	map[coords['x']][coords['y']] = island_id+1;

	return



def randomResources():
	r = {};
	for resource in resources:
		r[resource] = randint(resources[resource]['min'],resources[resource]['max'])
	return r;



def isEmptyCell(coords):
	#Boundries
	if(coords['x'] < 0 or coords['y'] < 0): return False
	if(coords['x'] > max_world_size-1): return False
	if(coords['y'] > max_world_size-1): return False

	cell = map[coords['x']][coords['y']];
	if cell:
		return False;
	else:
		return True;
	return;


def closestNeighbour(coords):
	#scipy.spatial.KDTree
	closest = 5;
	return closest;



def findEmptyCell():
	while 1:
		x = randint(0,max_world_size-1);
		y = randint(0,max_world_size-1);

		if isEmptyCell({ 'x':x, 'y':y }) and closestNeighbour({ 'x':x, 'y':y }) > 4:
			return { 'x':x, 'y':y }
			break

	print x;
	print y;

	#coords = { 'x':10, 'y':10 }
	coords = { 'x':0, 'y':0 }
	return coords;



def chopLumber():
	print 'Chopping lumber! +5 per 2 ticks'
	addEvent(2,eventChoplumber,{},2);
	return


def addEvent(time, call, args, repeat):
	when = tick_count + time;
	events.append({ 'ticks':when, 'repeat':repeat, 'method':call, 'args':args });



def eventWeather(args):
	print 'It is '+args['name']+'!';


def eventChoplumber(args):
	stockhold['lumber'] += 5


def closestCell():
	return


def createStockhold():
	for r in resources:
		stockhold[r] = 0
	return



def buildHouse():
	print "Building a house!"



def printStockhold():
	for s in stockhold:
		print s+': '+str(stockhold[s])
	return


def printMap():
	for row in map:
		for col in row:
			if col:
				print('#'),
			else:
				print('.'),
		print
	return;


def printIslandResources():
	print 'Resources'
	print '------------------'

	_resources = islandResources(islands[current_island]['cells'])
	for r in _resources:
		print r+': '+str(_resources[r])


def islandResources(cells):
	totals = {}

	for r in resources:
		totals[r] = 0

	for c in cells:
		for r in c['resources']:
			total = c['resources'][r]
			totals[r] += total

	return totals


def printIslandDetail():
	print 'Name: '+islands[current_island]['name']
	print 'Size: '+str(len(islands[current_island]['cells']))
	return



main();


#while(1):
#	createWorld();
#	printMap();
#	print '---------------------------------------------------------------'
#	time.sleep( 1 )