from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
	"""
	Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

	:param stairway: list of ints, where each int is a cost of appropriate step
	:return: minimal cost of getting to the top
	"""
	cost = [i for i in stairway]  # заполни масив нулями такого же размера

	for i in range(2, len(stairway)):
		cost[i] += min(cost[i - 1], cost[i - 2])

	return cost[-1]
