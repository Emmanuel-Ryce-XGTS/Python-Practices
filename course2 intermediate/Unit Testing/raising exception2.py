"""The assert Statement part2
"""
destinations = {
  'BUD': 'Budapest',
  'CMN': 'Casablanca',
  'IST': 'Istanbul'
}
print('Welcome to Small World Airlines!')
print('What is the airport code of your travel destination?')
destination = 'HND'


# Write your code below: 
assert destination in destinations, 'Sorry, Small World currently does not fly to this destination!'
  
city_name = destinations[destination]
print('Great! Retrieving information for your flight to ...' + city_name)



"""UNIT TESTING part 3"""

def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    location = 'back'
  return location

# Write your code below:
def test_row_1():

  assert get_nearest_exit(1) == "front", 'The nearest exit to row 1 is in the front!'

def test_row_20():

  assert get_nearest_exit(20) == "middle", 'The nearest exit to row 20 is in the middle!'

def test_row_40():

  assert get_nearest_exit(40) == "back", 'The nearest exit to row 40 is in the back!'

test_row_1()
test_row_20()
test_row_40()

"""Python unittest framework"""
# your code below:
import unittest

def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    location = 'back'
  return location

# Write your code below:
class NearestExitTests(unittest.TestCase):
  def test_row_1(self):
    self.assertEqual(get_nearest_exit(1) , 'front', 'The nearest exit to row 1 is in the front!')
    

  def test_row_20(self):
    self.assertEqual(get_nearest_exit(20) , 'middle', 'The nearest exit to row 20 is in the middle!')
    

  def test_row_40(self):
    self.assertEqual(get_nearest_exit(40) , 'back', 'The nearest exit to row 40 is in the back!')
    

unittest.main()



"""ASSERT METHODS 1: Equality and membership"""
import unittest
import entertainment

# Write your code below: 
class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()

    self.assertIn(daily_movie, licensed_movies)

  def test_wifi_status(self):
    wifi_enabled = entertainment.get_wifi_status()
    self.assertTrue(wifi_enabled)

unittest.main()



"""Assert Methods 2 Quantitative methods"""

import unittest
import entertainment

class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  def test_wifi_status(self):
    wifi_enabled = entertainment.get_wifi_status()
    self.assertTrue(wifi_enabled)

  # Write your code below:
  def test_maximum_display_brightness(self):
    brightness = entertainment.get_maximum_display_brightness()
    self.assertAlmostEqual(brightness, 400)

  def test_device_temperature(self):
    device_temp = entertainment.get_device_temp()
    self.assertLess(device_temp, 35) 

unittest.main()


"""Assert Methods III: Exception and Warning Methods
"""

import unittest
# import alerts

# # Write your code here:
# class SystemAlertTests(unittest.TestCase):
#   def test_power_outage_alert(self):
#     self.assertRaises(alerts.PowerError , alerts.power_outage_detected, True)

#   def test_water_levels_warning(self)
#     self.assertWarns(alerts.WaterLevelWarning, alerts.water_levels_check , 150)



# unittest.main()


"""PARAMETERIZING TESTS PART 8"""
import unittest
import entertainment

class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):

    # Write your code below:
    daily_movies = entertainment.get_daily_movies()
    licensed_movies = entertainment.get_licensed_movies()


    for movie in daily_movies:
      print(movie)
      with self.subTest(movie):
        self.assertIn(movie, licensed_movies)


unittest.main()



"""TEST FIXTURES PT 9 """
import unittest
import kiosk

class CheckInKioskTests(unittest.TestCase):

  def test_check_in_with_flight_number(self):
    print('Testing the check-in process based on flight number')

  def test_check_in_with_passport(self):
    print('Testing the check-in process based on passport')

  # Write your code below:
  @classmethod
  def setUpClass(cls):
    kiosk.power_on_kiosk()
  
  @classmethod
  def tearDownClass(cls): 
    kiosk.power_off_kiosk()

  def setUp(self):
    kiosk.return_to_welcome_page()
  


unittest.main()



"""SKipping texts"""
import unittest
import entertainment

class EntertainmentSystemTests(unittest.TestCase):

  @unittest.skipIf(entertainment.regional_jet(), 'Not available on regional jets')
  def test_movie_license(self):
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  @unittest.skipUnless(entertainment.regional_jet() is False, 'Not available on regional jets')
  def test_wifi_status(self):
    wifi_enabled = entertainment.get_wifi_status()
    self.assertTrue(wifi_enabled)

  def test_device_temperature(self):

    if entertainment.regional_jet():
      self.skipTest('Not available on regional jets')

    device_temp = entertainment.get_device_temp()
    self.assertLess(device_temp, 35)

  def test_maximum_display_brightness(self):

    if entertainment.regional_jet():

      self.skipTest('Not available on regional jets')

    brightness = entertainment.get_maximum_display_brightness()
    self.assertAlmostEqual(brightness, 400)


unittest.main()


"""Part 11 Expected Failures """

import unittest
import feedback

class CustomerFeedbackTests(unittest.TestCase):

  # Write your code below:
  @unittest.expectedFailure
  def test_survey_form(self):
    self.assertEqual(feedback.issue_survey(), 'Success')

  def test_complaint_form(self):
    self.assertEqual(feedback.log_customer_complaint(), 'Success')

unittest.main()
