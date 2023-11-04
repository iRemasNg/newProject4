import acp_times
import nose
import logging
import arrow

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.WARNING)
log = logging.getLogger(__name__)


def test_smallNum():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(150, 200, arrow.get(date)) == (date.shift(hours=4, minutes=25)).isoformat()
    assert acp_times.close_time(150, 200, arrow.get(date)) == (date.shift(hours=10)).isoformat()

def test_bigNum():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(700, 1000, arrow.get(date)) == (date.shift(hours=22, minutes=22)).isoformat()
    assert acp_times.close_time(700, 1000, arrow.get(date)) == (date.shift(hours=48, minutes=45)).isoformat()


def test_Case550():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(550, 600, arrow.get(date)) == (date.shift(hours=17, minutes=8)).isoformat()
    assert acp_times.close_time(550, 600, arrow.get(date)) == (date.shift(hours=36, minutes=40)).isoformat()

def test_odd():
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


def test_exceed_brevet200():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(241, 200, arrow.get(date)) == "invalid"
    assert acp_times.close_time(241, 200, arrow.get(date)) == "invalid"

def test_exceed_brevet300():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(361, 300, arrow.get(date)) == "invalid"
    assert acp_times.close_time(361, 300, arrow.get(date)) == "invalid"

def test_exceed_brevet400():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(481, 400, arrow.get(date)) == "invalid"
    assert acp_times.close_time(481, 400, arrow.get(date)) == "invalid"

def test_exceed_brevet600():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(721, 600, arrow.get(date)) == "invalid"
    assert acp_times.close_time(721, 600, arrow.get(date)) == "invalid"

def test_exceed_brevet1000():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(1201, 1000, arrow.get(date)) == "invalid"
    assert acp_times.close_time(1201, 1000, arrow.get(date)) == "invalid"

def test_less_60():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(10, 200, arrow.get(date)) == (date.shift(hours=0, minutes=18)).isoformat()
    assert acp_times.close_time(10, 200, arrow.get(date)) == (date.shift(hours=1, minutes=30)).isoformat()


def test_negative_distance():
    date = arrow.Arrow(2023, 11, 8)
    assert acp_times.open_time(-50, 200, arrow.get(date)) == "invalid"
    assert acp_times.close_time(-50, 200, arrow.get(date)) == "invalid"
