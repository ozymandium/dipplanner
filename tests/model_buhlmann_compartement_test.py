#! /usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 Thomas Chiroux
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.
# If not, see <http://www.gnu.org/licenses/gpl.html>
# 
# This module is part of dipplanner, a Dive planning Tool written in python
"""
Test for compartment class
"""

__authors__ = [
  # alphabetical order by last name
  'Thomas Chiroux',
]

import unittest
# import here the module / classes to be tested
from model.buhlmann.compartment import Compartment
from model.buhlmann.model_exceptions import ModelStateException
import dipplanner
import settings

class TestModelBuhlmannCompartemnt(unittest.TestCase):
  def setUp(self):
    # temporary hack (tests):
    dipplanner.activate_debug_for_tests()
    settings.RUN_TIME = True
    self.compt1 = Compartment(1.88,    5.0,    16.189, 0.4770, 11.696, 0.5578)
    self.compt2 = Compartment(1.88,    5.0,    16.189, 0.4770, 11.696, 0.5578)
    self.compt2.set_pp(0.3*5, (1-0.21-0.3)*5)
    self.compt3 = Compartment(1.88,    5.0,    16.189, 0.4770, 11.696, 0.5578)
    #self.compt3 = Compartment(70.69,  187.0,  5.333,  0.8997, 3.497,  0.9319)
    self.compt3.set_pp(0.0, 3.16)
    
class TestModelBuhlmannCompartemntSimple1(TestModelBuhlmannCompartemnt):
  def runTest(self):
    assert self.compt1.pp_He == 0, "wrong pp_He : %s" % self.compt1.pp_He
  
class TestModelBuhlmannCompartemntSimple2(TestModelBuhlmannCompartemnt):
  def runTest(self):
    assert self.compt1.pp_N2 == 0, "wrong pp_N2 : %s" % self.compt1.pp_N2
  
class TestModelBuhlmannCompartemntSimple3(TestModelBuhlmannCompartemnt):
  def runTest(self):
    assert round(self.compt1.k_He, 14) == 0.00614492181347, "wrong k_He : %s" % self.compt1.k_He

class TestModelBuhlmannCompartemntSimple4(TestModelBuhlmannCompartemnt):
  def runTest(self):
    assert round(self.compt1.k_N2, 14) == 0.00231049060187, "wrong k_N2 : %s" % self.compt1.k_N2

class TestModelBuhlmannCompartemntSimple5(TestModelBuhlmannCompartemnt):
  def runTest(self):
    assert self.compt1.a_He == 1.6189, "wrong a_He : %s" % self.compt1.a_He

class TestModelBuhlmannCompartemntSimple6(TestModelBuhlmannCompartemnt):
  def runTest(self):
    assert self.compt1.b_He == 0.4770, "wrong b_He : %s" % self.compt1.b_He

class TestModelBuhlmannCompartemntSimple7(TestModelBuhlmannCompartemnt):
  def runTest(self):
    assert self.compt1.a_N2 == 1.1696, "wrong a_N2 : %s" % self.compt1.a_N2
    
class TestModelBuhlmannCompartemntSimple8(TestModelBuhlmannCompartemnt):
  def runTest(self):
    assert self.compt1.b_N2 == 0.5578, "wrong b_N2 : %s" % self.compt1.b_N2
  
class TestModelBuhlmannCompartemntSimple9(TestModelBuhlmannCompartemnt):
  def runTest(self):
    assert self.compt2.pp_He == 1.5, "wrong pp_He : %s" % self.compt2.pp_He
    
class TestModelBuhlmannCompartemntSimple10(TestModelBuhlmannCompartemnt):
  def runTest(self):
    assert self.compt2.pp_N2 == 2.45, "wrong pp_N2 : %s" % self.compt2.pp_N2
  
class TestModelBuhlmannCompartemntSimple11(TestModelBuhlmannCompartemnt):
  def runTest(self):
    self.compt2.const_depth(0.3*4.5, (1-0.21-0.3)*4.5, 12*60)
    assert round(self.compt2.pp_He,11) == 1.35179731087,  "wrong pp_He : %s" % self.compt2.pp_He
  
class TestModelBuhlmannCompartemntSimple12(TestModelBuhlmannCompartemnt):
  def runTest(self):
    self.compt2.const_depth(0.3*4.5, (1-0.21-0.3)*4.5, 12*60)
    assert round(self.compt2.pp_N2,11) == 2.25141881985,  "wrong pp_N2 : %s" % self.compt2.pp_N2
  
class TestModelBuhlmannCompartemntSimple13(TestModelBuhlmannCompartemnt):
  def runTest(self):
    self.compt2.asc_desc(0.2997, 0.48951, 0.1, 0.163333333333, 9.0)
    assert round(self.compt2.pp_He, 11) == 1.45985489718,  "wrong pp_He : %s" % self.compt2.pp_He

class TestModelBuhlmannCompartemntSimple14(TestModelBuhlmannCompartemnt):
  def runTest(self):
    self.compt2.asc_desc(0.2997, 0.48951, 0.1, 0.163333333333, 9.0)
    assert round(self.compt2.pp_N2, 11) == 2.42483220311,  "wrong pp_N2 : %s" % self.compt2.pp_N2

class TestModelBuhlmannCompartemntMValue1(TestModelBuhlmannCompartemnt):
  def runTest(self):
    mv = self.compt3.get_m_value_at(0.0)
    assert mv == 1.1696, "wrong M-Value : %s" % mv
  
class TestModelBuhlmannCompartemntMValue2(TestModelBuhlmannCompartemnt):
  def runTest(self):
    mv = self.compt3.get_m_value_at(1.0)
    assert round(mv,11) == 2.96235726067, "wrong M-Value : %s" % mv
    
class TestModelBuhlmannCompartemntMValue3(TestModelBuhlmannCompartemnt):
  def runTest(self):
    mv = self.compt3.get_m_value_at(3.0)
    assert round(mv,9) == 6.547871782, "wrong M-Value : %s" % mv

class TestModelBuhlmannCompartemntMaxAmb1(TestModelBuhlmannCompartemnt):
  def runTest(self):
    max_amb = self.compt3.get_max_amb(0.8)
    assert round(max_amb,11) == 1.36110151389, "wrong max_amb for given gf : %s" % max_amb
    
class TestModelBuhlmannCompartemntMV1(TestModelBuhlmannCompartemnt):
  def runTest(self):
    mv = self.compt3.get_mv(1.0)
    assert round(mv,11) == 1.06671806333, "wrong mv for given amb pressure : %s" % mv
    
if __name__ == "__main__":
  #unittest.main()
  import sys
  suite = unittest.findTestCases(sys.modules[__name__])
  #suite = unittest.TestLoader().loadTestsFromTestCase(Test)
  unittest.TextTestRunner(verbosity=2).run(suite)