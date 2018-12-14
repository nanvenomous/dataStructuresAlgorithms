# tutorial: https://gist.github.com/isaacs/62a2d1825d04437c6f08

# format of a makefile rule
# <target>: <prerequisites...>
# 	<commands>

# also note that no prerequesites are necessary
setup:
	@echo 'making directory ./.execute/'
	@subDir='./.execute/'; \
	mkdir -p $${subDir}
	@echo

source.txt:
	@echo "building source.txt"
	@echo "this is the source" > source.txt
	@echo

# @ is a way to echo without writing twice, @ supresses makefile output
result.txt: setup source.txt
	@echo "building result.txt from source.txt"
	@cp source.txt .execute/result.txt
	@echo

main: result.txt
	@echo 'whole project built successfully'
