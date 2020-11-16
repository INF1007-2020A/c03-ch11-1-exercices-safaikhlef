"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""	
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	
	UNARMED_POWER = 20
	
	def __init__(self, name, power, min_level):
		self.__name = name #le nom ne peut être changé
		self.power = power
		self.min_level = min_level
		
	@property # on utilise le décorateur directement, on le rend accessible en mode lecture, @name.setter pour pouvoir le modifier, ne pas mettre le setter empêche de le modifier, mais on toujours l'accès
	def name(self):
		return self.__name #décorateur
	

		
class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	
	def __init__(self, name, max_hp, attack, defense, level):
		self.__name = name #le nom ne peut être changé
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.__hp = self.max_hp
		self.weapons = None
		
	@property
	def name(self):
		return self.__name #décorateur
	
	@property
	def hp(self):
		return self.__hp #décorateur
	
	@hp.setter
	def hp(self, val):
		self.__hp = utils.clamp(val, 0, self.max_hp)
	
	def compute_damage(self, other):
		level_factor = (2*self.level) / 5 + 2
		weapon_factor = self.weapom.power
		atk_def_factor = self.attack / other.defense
		critique = random.random() <= 1/16
		modifier = (2 if critical else 1) * random.uniform(0.85, 1.0)
		damage = ((level_factor * weapon_factor * atk_def_factor) / 50 + 2) * modifier
		return damage, critical



def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	damage, critical = attacker.compute_damage(defender)
	defender.hp -= damage
	print(f"{attacker.name} used {attacker.weapon.name}")
	if crit:
		print("  Critical hit!")
	print(f"  {defender.name} took {damage} dmg")

def run_battle(c1, c2):
	attacker = c1
	defender = c2
	turn = 1
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	print(f"{attacker.name} starts a battle with {defender.name}!")
	while True:
		# TODO: Appliquer l'attaque
		deal_damage(attacker, defender)
		# TODO: Si le défendeur est mort
		if defender.hp <= 0:
			print(f"{defender.name } is sleeping with the fishes.")
			break
		# Échanger attaquant/défendeur
		attacker, defender = defender, attacker
		turn += 1
	# TODO: Retourner nombre de tours effectués
	return turn
