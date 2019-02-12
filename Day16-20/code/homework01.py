"""
装饰器的应用
"""
from functools import wraps
from random import randint
from time import sleep


class Retry():
	"""让函数可以重试执行的装饰器"""

	def __init__(self, times=3, max_wait=0, errors=(Exception, )):
		self.times = times
		self.max_wait = max_wait
		self.errors = errors

	def __call__(self, func):

		@wraps(func)
		def wrapper(*args, **kwargs):
			for _ in range(self.times):
				try:
					return func(*args, **kwargs)
				except self.errors:
					sleep(randint(self.max_wait))

		return wrapper


def retry(*, times=3, max_wait=0, errors=(Exception, )):
	"""让函数重试执行的装饰器函数"""

	def decorate(func):

		@wraps(func)
		def wrapper(*args, **kwargs):
			for _ in range(times):
				try:
					return func(*args, **kwargs)
				except errors:
					sleep(randint(max_wait))
		return wrapper

	return decorate


# @Retry(max_wait=5)
@retry(max_wait=5)
def get_data_from_url(url):
	pass

