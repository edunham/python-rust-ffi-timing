fn sum_digits(mut sumthing: u64) -> u64 {
    let mut total = 0;
    while sumthing > 0 {
        total += sumthing % 10;
        sumthing /= 10;
    }
    if total >= 10 {
        total = sum_digits(total)
    }
    return total;
}
#[no_mangle]
pub extern "C" fn sum_up(upto: u64) -> u64 {
    let mut total = 0;
    for n in 0..=upto {
        total = sum_digits(n + total);
    }
    return total;
}
