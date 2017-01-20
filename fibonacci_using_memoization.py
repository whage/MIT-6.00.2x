def fib(n, memo = {}):
	if n == 1 or n == 0:
		return 1

	try:
		return memo[n]
	except KeyError:
		memo[n] = (fib(n - 1, memo) + fib(n - 2, memo))

	return memo[n]

print(fib(998, {}))