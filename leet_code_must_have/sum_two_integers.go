func getSum(a int, b int) int {
    sum := a
    for ; b > 0; {
        sum = a ^ b // sum without carry bit
        b = (a & b) << 1 // calculate the carry bit
        a = sum // add sum(without carry) and carry
    }
    return a
}