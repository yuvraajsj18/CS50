# Questions

## What's `stdint.h`?

It is a header file which allows programmers to write more portable code by providing a set of typedefs that specify exact width integer type, together with the defined minimum and maximum value for each type.
Basically, it contains the uint8_t kind of varaibles

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

These functions are a cross-platform implementation of a standard data type
uint8_t = unsigned integer 8 bit(1 byte)
uint32_t = unsigned integer 32 bit(4 byte)
int32_t = signed integer 32 bit(4 byte)
uint16_t = unsigned integer 16 bit(2 byte)
They have the same fixed size on every platform.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE = 8 BIT OR 1 BYTE(UNSIGNED)
DWORD = 32 BIT OR 4 BYTE (UNSIGNED)
LONG = 32 BIT OR 4 BYTE (SIGNED)
WORD = 16 BIT OR 2 BYTE (UNSIGNED)

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

The first two bytes of BMP file are 'BM' with hex 0x4D42.

## What's the difference between `bfSize` and `biSize`?

bfSize describes the entire file size in bytes, whereas biSize is the size of BITMAPINFOHEADER in bytes.

## What does it mean if `biHeight` is negative?

If biHeight is negative, the bitmap is a top-down DIB and its origin is the upper-left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount

## Why might `fopen` return `NULL` in `copy.c`?

fopen will return null if it cannot open the file. This can happen if there is not enough memory or the file cannot be found.

## Why is the third argument to `fread` always `1` in our code?

The third argument determines the number of elements fread will read. So this argument is always 1 because we are always reading one file.

## What value does `copy.c` assign to `padding` if `bi.biWidth` is `3`?

TODO

## What does `fseek` do?

TODO

## What is `SEEK_CUR`?

TODO
