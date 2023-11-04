# import acp_times
# import nose
# import logging
# import arrow

# logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.WARNING)
# log = logging.getLogger(__name__)
# print("Running Tests")
# #times less than first
# def small():
# 	date = arrow.Arrow(2023, 11, 8)
# 	assert acp_times.open_time(150, 200, arrow.get(date)) == (date.shift(hours=4,minutes=25)).isoformat()
# 	assert acp_times.close_time(150, 200, arrow.get(date)) == (date.shift(hours=10)).isoformat()

# #additions of times
# def big():
# 	date = arrow.Arrow(2023, 11, 8)
# 	assert acp_times.open_time(700, 1000, arrow.get(date)) == (date.shift(hours=22,minutes=22)).isoformat()
# 	assert acp_times.close_time(700, 1000, arrow.get(date)) == (date.shift(hours=48,minutes=45)).isoformat()

# #time that is exactly equal
# def exact():
# 	date = arrow.Arrow(2023, 11, 8)
# 	assert acp_times.open_time(600, 600, arrow.get(date)) == (date.shift(hours=18,minutes=48)).isoformat()
# 	assert acp_times.close_time(600, 600, arrow.get(date)) == (date.shift(hours=40)).isoformat()

# #test control value of 550
# def reg():
# 	date = arrow.Arrow(2023, 11, 8)
# 	assert acp_times.open_time(550, 600, arrow.get(date)) == (date.shift(hours=17,minutes=8)).isoformat()
# 	assert acp_times.close_time(550, 600, arrow.get(date)) == (date.shift(hours=36,minutes=40)).isoformat()

# #control value that is odd
# def oddnum():
# 	date = arrow.Arrow(2023, 11, 8)
# 	assert acp_times.open_time(311, 400, arrow.get(date)) == (date.shift(hours=9,minutes=21)).isoformat()
# 	assert acp_times.close_time(311, 400, arrow.get(date)) == (date.shift(hours=20,minutes=44)).isoformat()
	
# # Extra 

# # Edge case: control distance is 0
# def control_distance_zero():
#     date = arrow.Arrow(2023, 11, 8)
#     assert acp_times.open_time(0, 200, arrow.get(date)) == arrow.get(date).isoformat()
#     assert acp_times.close_time(0, 200, arrow.get(date)) == arrow.get(date).isoformat()

# # Edge case: control distance equals brevet distance
# def control_distance_equal_to_brevet():
#     date = arrow.Arrow(2023, 11, 8)
#     assert acp_times.open_time(200, 200, arrow.get(date)) == (date.shift(hours=5, minutes=53)).isoformat()
#     assert acp_times.close_time(200, 200, arrow.get(date)) == (date.shift(hours=13, minutes=30)).isoformat()

# # Official ACP brevet distances
# def official_distances():
#     date = arrow.Arrow(2023, 11, 8)
#     assert acp_times.open_time(200, 200, arrow.get(date)) == (date.shift(hours=5, minutes=53)).isoformat()
#     assert acp_times.open_time(300, 300, arrow.get(date)) == (date.shift(hours=9, minutes=0)).isoformat()
#     assert acp_times.open_time(400, 400, arrow.get(date)) == (date.shift(hours=12, minutes=8)).isoformat()
#     assert acp_times.open_time(600, 600, arrow.get(date)) == (date.shift(hours=18, minutes=48)).isoformat()
#     assert acp_times.open_time(1000, 1000, arrow.get(date)) == (date.shift(hours=37, minutes=38)).isoformat()
	

# # Negative control distance
# def negative_control_distance():
#     date = arrow.Arrow(2023, 11, 8)
#     assert acp_times.open_time(-50, 200, arrow.get(date)) == "Invalid Input"
#     assert acp_times.close_time(-50, 200, arrow.get(date)) == "Invalid Input"
	


# # Test with non-integer brevet distance
# def non_integer_brevet_distance():
#     date = arrow.Arrow(2023, 11, 8)
#     assert acp_times.open_time(300, 250, arrow.get(date)) == "Invalid Input"
#     assert acp_times.close_time(300, 250, arrow.get(date)) == "Invalid Input"

# # Test with non-integer control distance
# def non_integer_control_distance():
#     date = arrow.Arrow(2023, 11, 8)
#     assert acp_times.open_time(250, 300, arrow.get(date)) == "Invalid Input"
#     assert acp_times.close_time(250, 300, arrow.get(date)) == "Invalid Input"


import acp_times
import nose
import logging
import arrow

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.WARNING)
log = logging.getLogger(__name__)
# print("Running Tests")
# Times less than first
def test_small():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(150, 200, arrow.get(date)) == (date.shift(hours=4, minutes=25)).isoformat()
    assert acp_times.close_time(150, 200, arrow.get(date)) == (date.shift(hours=10)).isoformat()

# Additions of times
def test_big():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(700, 1000, arrow.get(date)) == (date.shift(hours=22, minutes=22)).isoformat()
    assert acp_times.close_time(700, 1000, arrow.get(date)) == (date.shift(hours=48, minutes=45)).isoformat()

# Time that is exactly equal
def test_exact():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(600, 600, arrow.get(date)) == (date.shift(hours=18, minutes=48)).isoformat()
    assert acp_times.close_time(600, 600, arrow.get(date)) == (date.shift(hours=40)).isoformat()

# Test control value of 550
def test_reg():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(550, 600, arrow.get(date)) == (date.shift(hours=17, minutes=8)).isoformat()
    assert acp_times.close_time(550, 600, arrow.get(date)) == (date.shift(hours=36, minutes=40)).isoformat()

# Control value that is odd
def test_oddnum():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(311, 400, arrow.get(date)) == (date.shift(hours=9, minutes=21)).isoformat()
    assert acp_times.close_time(311, 400, arrow.get(date)) == (date.shift(hours=20, minutes=44)).isoformat()


def test_exact_brevet_distances1():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(200, 200, arrow.get(date)) == (date.shift(hours=5, minutes=53)).isoformat()
    assert acp_times.close_time(200, 200, arrow.get(date)) == (date.shift(hours=13, minutes=30)).isoformat()


def test_exact_brevet_distances2():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(300, 300, arrow.get(date)) == (date.shift(hours=9)).isoformat()
    assert acp_times.close_time(300, 300, arrow.get(date)) == (date.shift(hours=20)).isoformat()

def test_exact_brevet_distances3():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(400, 400, arrow.get(date)) == (date.shift(hours=12, minutes=8)).isoformat()
    assert acp_times.close_time(400, 400, arrow.get(date)) == (date.shift(hours=27)).isoformat()

def test_exact_brevet_distances4():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(600, 600, arrow.get(date)) == (date.shift(hours=18, minutes=48)).isoformat()
    assert acp_times.close_time(600, 600, arrow.get(date)) == (date.shift(hours=40)).isoformat()


def test_exact_brevet_distances5():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(1000, 1000, arrow.get(date)) == (date.shift(hours=33, minutes=5)).isoformat()
    assert acp_times.close_time(1000, 1000, arrow.get(date)) == (date.shift(hours=75)).isoformat()


def test_starting_point():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(0, 200, arrow.get(date)) == (date.shift(hours=0)).isoformat()
    assert acp_times.close_time(0, 200, arrow.get(date)) == (date.shift(hours=1)).isoformat()


def test_brevet_890():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(890, 1000, arrow.get(date)) == (date.shift(hours=29, minutes=9)).isoformat()
    assert acp_times.close_time(890, 1000, arrow.get(date)) == (date.shift(hours=65, minutes=23)).isoformat()








# # Negative control distance
# def test_negative_control_distance():
#     date = arrow.Arrow(2023, 11, 8)
#     assert acp_times.open_time(-50, 200, arrow.get(date)) == "Invalid Input"
#     assert acp_times.close_time(-50, 200, arrow.get(date)) == "Invalid Input"
