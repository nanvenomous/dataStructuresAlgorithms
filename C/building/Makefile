allFiles:
	@echo 'building implementation.c functionInSrc.c'
	@cc implementation.c headers/functionInSrc.c -o ./execute -I .
	@echo

allFilesReversed:
	@echo 'building functionInSrc.c implementation.c'
	@cc headers/functionInSrc.c implementation.c -o ./execute -I .
	@echo

main: allFilesReversed
	@echo 'sequence finished'
