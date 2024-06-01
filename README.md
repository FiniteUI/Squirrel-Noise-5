# Squirrel-Noise-5

This is a python implementation of Squirrel Eiserloh's SquirrelNoise5 algorithm, which is a modified version of his squirrel3 algorithm presented at GDC 2017.

The GDC talk can be found here:
https://www.youtube.com/watch?v=LWFzPP8ZbdU

The original version can be found here:
http://eiserloh.net/noise/SquirrelNoise5.hpp

This script implements the base noise function, which returns a "random" 32 bit integer based on a seed and an input, then implements several functions built off of this.
There are 1d, 2d, 3d, and 4d impelemtations of:
1. A base noise function
2. A noise function with a normalized (0 - 1) float
3. A noise function which returns an integer in a specified range
4. A noise function which returns a float in a specified range
5. A noise function which returns a boolean
6. A noise function which returns a boolean which returns true a specified percent of the time

There are also implementations of random functions that can return randomized values without an input. These utilize an internal counter as the input for the basic other
built in noise functions. Utilizing these, random values can be generated without requiring an input, but can still be recreated if the same seed is used.
1. A function which returns a random 32 bit integer
2. A function which returns a random integer in a specified range
3. A function which returns a random float in a specified range
4. A function which returns a random boolean
5. A function which returns a random boolean which returns true a specified percent of the time
6. A function which returns a random normalized (0 - 1) float

A new noise generator can be created initialized by importing the script into your existing project and using:
```python
ns = noise_squirrel5.noise_squirrel5(seed)
```
