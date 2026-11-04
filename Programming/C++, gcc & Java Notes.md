---
tags: [programming, cpp, gcc, java]
updated: 2026-11-04
---
# C++, gcc & Java Notes

> [!summary] Contents
> 1. C++ notes
> 2. gcc command line
> 3. Java: list a jar

---

## 1. C++

### Threads

`std::bind` binds a member function to an object instance, and the result can be passed to `std::thread`:

```cpp
std::thread t(std::bind(&Worker::startTask, &worker));   // member function + object
t.detach();                                              // detach the thread
```

On Windows you can also create a thread with `CreateThread`.

### Pointer casts

```cpp
dynamic_cast        // safe downcast with a runtime check (needs a polymorphic class)
static_cast         // normal compile-time conversion
reinterpret_cast    // reinterpret the bits, no checks at all
```

### Callback inside a class

A member function that is used as a (C-style) callback must be declared **`static`**.

### Strings

```cpp
if (str.find("abc") == std::string::npos) {
    // "abc" was NOT found
}
```

### Small things to remember

- `std::setw(n)` sets the minimum width of the next output item to `n`; shorter data is padded with spaces.
- `std::ofstream` is the class for writing files.
- STL containers: `set`, `map`, `vector`, `queue`.

> [!bug] Sorted `map`
> `std::map` is **always sorted by key**, and so is `std::multimap`. `multimap` does **not** give an unsorted map (an older version of this note said so). For an unsorted container use `std::unordered_map` (C++11), or a `vector` of pairs. In old Visual Studio (2003) there is no `unordered_map`; its extension `stdext::hash_map` is the unsorted one.

---

## 2. gcc Command Line

```bash
gcc -g vadtest.c -I include/ -L lib/ -lvoice -lrecord -Wall -fno-stack-protector
```

| Option | Meaning |
|---|---|
| `-g` | Add debug information |
| `-I include/` | Folder to search for header files |
| `-L lib/` | Folder to search for libraries |
| `-lvoice` `-lrecord` | Link `libvoice` and `librecord` |
| `-Wall` | Turn on the common warnings |
| `-fno-stack-protector` | **Turn off** the stack-smashing check (Ubuntu's gcc enables it by default) |

> [!bug] Fixed in this note
> The old command had `-L -lrecord`. A bare `-L` takes the next word as a folder, so `-lrecord` was never linked as a library. It is just `-lrecord`.
> Also, `-g` and `-fno-stack-protector` do not "check stack errors": `-g` adds debug info, and `-fno-stack-protector` switches the stack check **off**.

---

## 3. Java: List a Jar

```bash
jar tf yourfile.jar        # list the files (and .class files) inside a jar
```
