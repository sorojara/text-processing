from mine_dwarf.variables import dwarf_title, dance_title, guys_title, epic_title, isometric_title, train_title, delta_title
import random


def generate_random_title():
	title_pool = [dwarf_title, dance_title, guys_title, epic_title, isometric_title, train_title]
	return random.choice(title_pool)