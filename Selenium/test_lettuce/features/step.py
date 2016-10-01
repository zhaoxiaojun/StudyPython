#coding=utf-8
from lettuce import *
from comp_factorial import comp_factorial

@step('I have the number (\d+)')
def hava_the_number(step,number):
    world.number = int(number)

@step('I compute its factorial')
def compute_its_fatorial(step):
    world.number = comp_factorial.comp_factorial(world.number)

@step('I see the number (\d+)')
def check_number(step, num_expected):
    num_expected = int(num_expected)
    assert world.number == num_expected, "Got %d" % world.number