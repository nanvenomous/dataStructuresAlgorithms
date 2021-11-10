package threesum

import (
	"testing"
)

var expectedEmpty [][]int

func testSlicesEqual(t *testing.T, one []int, two []int) {
	if (one == nil) || (two == nil) {
		t.Error("an array was nil")
	}
	if len(one) != len(two) {
		t.Error("array lengths not equal")
	}
	for i := range one {
		if one[i] != two[i] {
			t.Errorf("inequality at %d", i)
		}
	}
}

func testSliceOfSlicesEqual(t *testing.T, one [][]int, two [][]int) {
	if one == nil && two == nil {
		return
	}
	if (one == nil) || (two == nil) {
		t.Error("an array was nil")
	}
	if len(one) != len(two) {
		t.Error("array lengths not equal")
	}
	for i := range one {
		testSlicesEqual(t, one[i], two[i])
	}
}

func TestThreeSum(t *testing.T) {
	mock := []int{-1, 0, 1, 2, -1, -4}
	expected := [][]int{{-1, 0, 1}, {-1, -1, 2}}
	actual := Run(mock)
	testSliceOfSlicesEqual(t, expected, actual)
}

func TestEmpty(t *testing.T) {
	mock := []int{}
	actual := Run(mock)
	testSliceOfSlicesEqual(t, expectedEmpty, actual)
}

func TestZero(t *testing.T) {
	mock := []int{0}
	actual := Run(mock)
	testSliceOfSlicesEqual(t, expectedEmpty, actual)
}
