fn main() {
    'outer: loop {
        println!("Outer loop");

        'inner: loop {
            println!("Inner loop");
            
            // This breaks the outer loop
            break 'outer;
        }
    }

    println!("Exited Outer loop");
}