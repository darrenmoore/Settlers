#Settings for game


#New
#What a new player is given
NEW = {
	'resources': {
		'wood': 10,
		'gold': 10
	},
	'buildings': {
		'townhall': {}
	},
	'ships': {
	},
	'people': {
		'citizen': 10
	}
}



RESOURCES = {
	'coal': {
		'cell_min':5,
		'cell_max':50
	},
	'lumber':{
		'cell_min':5,
		'cell_max':50
	},
	'stone': {
		'cell_min':5,
		'cell_max':50
	},
	'iron': {
		'cell_min':5,
		'cell_max':50
	},
	'gold': {
		'cell_min':5,
		'cell_max':50
	},
	'bread': {
	},
	'pork': {
	},
	'chicken': {
	},
	'apple': {
	}
}


BUILDINGS = {
	'townhall': {
		'name': 'Town Hall'
	},
	'house': {
		'levels': {
			'1': {
				'requires': {
					'resources': { 'lumber':20, 'stone':5, 'gold':2 },
					'tech': 1
				},
				'attack': 0,
				'defence': 5,
				'ticks_to_build': 20,
				'size':5
			}
		}
	},
	'lumber_mill': {
		'requires': {
			'resources': {
				'lumber': 10,
				'gold': 2
			},
			'tech': 1
		},
		'produce': {
			'resources': {
				'lumber': { 'ticks':5, 'amount':1 },
				'apple': { 'ticks':[5,20], 'amount':1 }		#create a random apple sometimes
			}
		},
		'ticks_to_build': 10
	},
	'barracks': {
	},
	'gold_mine': {
	},
	'stone_quarry': {
	},
	'laboratory': {
	},
	'harbour': {
	},
	'storehouse': {
	},
	'stone_wall': {
	},
	'farm_wheat': {
	},
	'farm_meat': {
	},
	'watch_tower': {
	}.
	'academy': {
	},
	'embassy': {
		#make alliances
	}
}


SHIPS = {
	'warship': {
	},
	'merchant': {
	},
	'collisation': {
	},
	'spy': {
	}
}


PEOPLE = {
	'citizen': {
		'requires': {
			'buildings': {
				'house': { 'level':1, 'space':5 }
			}
		},
		'ticks_to_build': 5,
		'payment': {
			'ticks': 10,
			'amount': 1
		}
	},
	'spearfighter': {
		'levels': {
			'1': {
				'ticks_to_build': 10,
				'requires': {
					'buildings': { 
						'barracks':{ 'level':1 }
					}
				}
			}
		}
	},
	'archer': {},
	'catapault': {},
	'scientist': {},
}