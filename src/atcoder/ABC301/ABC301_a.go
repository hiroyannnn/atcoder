package main

import (
	"fmt"
)

func main() {

	// TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

	// param
	var a int
	// var b, c int
	var s string
	fmt.Scanf("%d\n", &a)
	// fmt.Scanf("%d %d\n", &b, &c)
	fmt.Scanf("%s\n", &s)
	ans := 0
	bns := 0
	for i := 0; i < len(s); i++ {
		if s[i] == 'A' {
			ans++
		}
		if s[i] == 'T' {
			bns++
		}
      	// fmt.Printf("%d %d %d\n", a / 2,ans,bns)

      if ans >= (a / 2) {
			fmt.Printf("A")
			break
		}
      if bns >= (a / 2) {
			fmt.Printf("T")
			break
		}
	}
}
