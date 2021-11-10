package threesum

import "sort"

// https://leetcode.com/problems/3sum/

//   a  b  c
//   a  b     c
//   a  b         c
//   a  b             c
//   a     b  c
//   a     b      c
//   a     b          c
//   a        b   c
//   a        b       c
//   a            b   c
//      a  b  c
// [-1, 0, 1, 2, -1, -4]

// sub problem with first value constant
// same as sub problem with second value constant?

var (
	solutions  [][]int
	Nums       []int
	numToCheck int
)

// slicesEqual determines if two int slices have all the same elements in order
func slicesEqual(one []int, two []int) bool {
	if (one == nil) || (two == nil) {
		return false
	}
	if len(one) != len(two) {
		return false
	}
	for i := range one {
		if one[i] != two[i] {
			return false
		}
	}
	return true
}

func anySlicesEqual(pool [][]int, sl []int) bool {
	for _, csl := range pool {
		if slicesEqual(csl, sl) {
			return true
		}
	}
	return false
}

// sum sums an array of integers
func sum(nums []int) int {
	tot := 0
	for _, n := range nums {
		tot += n
	}
	return tot
}

// tryAllIndices gets all combinations of the remaining indices (numInds)
func tryAllIndices(tot []int, start int, numInds int) {
	if numInds > 0 { // if we have additional indices
		if start < len(Nums) { // we still have space to place new index
			for i, n := range Nums[start:] {
				newTot := append(tot, n)
				tryAllIndices(newTot, i+1, numInds-1)
			}
		} else { // not enough space for new index (that does exist)
			return
		}
	} else { // no more indices is the total correct?
		if sum(tot) == 0 {
			sort.Ints(tot)
			if !anySlicesEqual(solutions, tot) {
				solutions = append(solutions, tot)
			}
		}
	}
}

func Run(nums []int) [][]int {
	var initSln [][]int
	numToCheck = 3 // this is a 3 sum
	solutions = make([][]int, 0)
	if len(nums) < 3 {
		return initSln
	}
	Nums = nums
	for i, n := range Nums[0 : len(Nums)-numToCheck] {
		tryAllIndices([]int{n}, i+1, numToCheck-1)
	}
	return solutions
}
