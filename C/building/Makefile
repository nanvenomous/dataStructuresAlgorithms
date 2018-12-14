setup:
	@echo 'making directory ./.execute/'
	@subDir='./.execute/'; \
	mkdir -p $${subDir}
	@echo

source.txt:
	@echo "building source.txt"
	@echo "this is the source" > source.txt
	@echo

implementation: setup
	@echo "building implementation.c"
	@cc implementation.c -o ./.execute/implementation -I .
	@echo

main: implementation
	@echo 'sequence finished'
