# Python Rust FFI Timing

Examples for talks.edunham.net/djangoconau2019 presentation. 

Derived and updated from Alex Crichton's work in github.com/alexcrichton/rust-ffi-examples, which has many other languages as well. 

```
cargo build
python timer.py
```

```
.
├── Cargo.lock			Rust's mneumonic of what versions last built successfully
├── Cargo.toml			Info for Rust about any dependencies, versions, etc
├── README.md			You Are Here
├── src
│   ├── lib.rs			The Rust code we FFI to
│   └── main.py			The Python that FFIs to the Rust
├── sum.py			Pure-Python example of the same maths the Rust does
├── target			Emitted by `cargo build`, ok to delete
└── timer.py			Runs the Rust and Python versions on arbitrary inputs, writes data.csv
```
