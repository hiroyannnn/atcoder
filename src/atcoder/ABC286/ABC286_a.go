package main

import (
	"fmt"
)

func main() {

	// TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

	// param
	var a, b, c, d, e int
	fmt.Scanf("%d %d %d %d %d\n", &a, &b, &c, &d, &e)

	slice := make([]int, a)
	for i := 0; i < a; i++ {
		fmt.Scanf("%d", &slice[i])
	}

	swap := make([]int, c-b+1)
	for i := 0; i < c-b+1; i++ {
		swap[i] = slice[d-1+i]
	}
	for i := 0; i < c-b+1; i++ {
		slice[d-1+i] = slice[b-1+i]
	}
	for i := 0; i < c-b+1; i++ {
		slice[b-1+i] = swap[i]
	}

	// answer
	for _, v := range slice {
		fmt.Printf("%d ", v) // a bc def
	}
}
