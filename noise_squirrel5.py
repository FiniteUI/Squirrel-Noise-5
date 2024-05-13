#noise_squirrel5
#this is a python implementation of Squirrel Eiserloh's SquirrelNoise5 algorithm
#which is a modified version of his squirrel3 algorithm presented at GDC 2017
#https://www.youtube.com/watch?v=LWFzPP8ZbdU
#http://eiserloh.net/noise/SquirrelNoise5.hpp
#having to use numpy because the algorithm relies on 32 bit unsigned integer math, and regular python ints are unbound and signed

import numpy

numpy.seterr(over='ignore')

class noise_squirrel5:
    BIT_NOISE_1 = 0xd2a80a3f
    BIT_NOISE_2 = 0xa884f197
    BIT_NOISE_3 = 0x6C736F4B
    BIT_NOISE_4 = 0xB79F3ABB
    BIT_NOISE_5 = 0x1b56c4f5
    PRIME_1 = 198491317
    PRIME_2 = 6542989
    PRIME_3 = 357239
    NORMAL = numpy.double(1 / 0xFFFFFFFF)
    HALF = numpy.uint32(0xFFFFFFFF / 2)
    MAX = 0xFFFFFFFF

    def __init__(self, seed):
        #requires 32 bit seed
        self.seed = noise_squirrel5.__convertToUInt32(seed)
        self.position = -1

    def __convertToUInt32(integer):
        integer = numpy.uint32(integer % (noise_squirrel5.MAX + 1))
        return integer

    def __get2dInput(x, y):
        x = noise_squirrel5.__convertToUInt32(x)
        y = noise_squirrel5.__convertToUInt32(y)
        input = numpy.uint32(x + (noise_squirrel5.PRIME_1 * y))

        return input
    
    def __get3dInput(x, y, z):
        x = noise_squirrel5.__convertToUInt32(x)
        y = noise_squirrel5.__convertToUInt32(y)
        z = noise_squirrel5.__convertToUInt32(z)
        input = numpy.uint32(x + (noise_squirrel5.PRIME_1 * y) + (noise_squirrel5.PRIME_2 * z))

        return input
    
    def __get4dInput(x, y, z, t):
        x = noise_squirrel5.__convertToUInt32(x)
        y = noise_squirrel5.__convertToUInt32(y)
        z = noise_squirrel5.__convertToUInt32(z)
        t = noise_squirrel5.__convertToUInt32(t)
        input = numpy.uint32(x + (noise_squirrel5.PRIME_1 * y) + (noise_squirrel5.PRIME_2 * z) + (noise_squirrel5.PRIME_3 * t))

        return input

    def noise(self, input):
        #requires 32 bit input, so we just mod
        temp = noise_squirrel5.__convertToUInt32(input)
        
        #now scramble the bits
        temp = numpy.uint32(temp * noise_squirrel5.BIT_NOISE_1)
        temp = numpy.uint32(temp + self.seed)
        temp = numpy.uint32(temp ^ (temp >> 9))
        temp = numpy.uint32(temp + noise_squirrel5.BIT_NOISE_2)
        temp = numpy.uint32(temp ^ (temp >> 11))
        temp = numpy.uint32(temp * noise_squirrel5.BIT_NOISE_3)
        temp = numpy.uint32(temp ^ (temp >> 13))
        temp = numpy.uint32(temp + noise_squirrel5.BIT_NOISE_4)
        temp = numpy.uint32(temp ^ (temp >> 15))
        temp = numpy.uint32(temp * noise_squirrel5.BIT_NOISE_5)
        temp = numpy.uint32(temp ^ (temp >> 17))
        
        return int(temp)

    def normalizedNoise(self, input):
        temp = numpy.double(noise_squirrel5.NORMAL * self.noise(input))

        return float(temp)

    def rangeNoise(self, input, minimum, maximum):
        range = maximum - minimum
        input = range * self.normalizedNoise(input)
        input = input + minimum

        return input

    def rangeNoiseInt(self, input, minimum, maximum):
        range = maximum - minimum
        input = self.noise(input) % (range + 1)
        input = input + minimum

        return input

    def noiseBool(self, input):
        input = self.noise(input)

        if input <= noise_squirrel5.HALF:
            return True
        else:
            return False

    def noiseBoolThreshold(self, input, threshold: float):
        #return a boolean True if the result is under the threshold
        input = self.normalizedNoise(input)
        if input < threshold:
            return True
        else:
            return False
        
    def noise2d(self, x, y):
        input = noise_squirrel5.__get2dInput(x, y)
        input = self.noise(input)

        return input

    def normalizedNoise2d(self, x, y):
        input = noise_squirrel5.__get2dInput(x, y)
        input = self.normalizedNoise(input)

        return input

    def rangeNoise2d(self, x, y, minimum, maximum):
        input = noise_squirrel5.__get2dInput(x, y)
        input = self.rangeNoise(input, minimum, maximum)

        return input

    def rangeNoiseInt2d(self, x, y, minimum, maximum):
        input = noise_squirrel5.__get2dInput(x, y)
        input = self.rangeNoiseInt(input, minimum, maximum)

        return input

    def noiseBool2d(self, x, y):
        input = noise_squirrel5.__get2dInput(x, y)
        input = self.noiseBool(input)

        return input

    def noiseBoolThreshold2d(self, x, y, threshold: float):
        input = noise_squirrel5.__get2dInput(x, y)
        input = self.noiseBoolThreshold(input, threshold)
        
        return input

    def noise3d(self, x, y, z):
        input = noise_squirrel5.__get3dInput(x, y, z)
        input = self.noise(input)

        return input

    def normalizedNoise3d(self, x, y, z):
        input = noise_squirrel5.__get3dInput(x, y, z)
        input = self.normalizedNoise(input)

        return input

    def rangeNoise3d(self, x, y, z, minimum, maximum):
        input = noise_squirrel5.__get3dInput(x, y, z)
        input = self.rangeNoise(input, minimum, maximum)

        return input

    def rangeNoiseInt3d(self, x, y, z, minimum, maximum):
        input = noise_squirrel5.__get3dInput(x, y, z)
        input = self.rangeNoiseInt(input, minimum, maximum)

        return input

    def noiseBool3d(self, x, y, z):
        input = noise_squirrel5.__get3dInput(x, y, z)
        input = self.noiseBool(input)

        return input
    
    def noiseBoolThreshold3d(self, x, y, z, threshold: float):
        input = noise_squirrel5.__get3dInput(x, y, z)
        input = self.noiseBoolThreshold(input, threshold)
        
        return input

    def noise4d(self, x, y, z, t):
        input = noise_squirrel5.__get4dInput(x, y, z, t)
        input = self.noise(input)

        return input

    def normalizedNoise4d(self, x, y, z, t):
        input = noise_squirrel5.__get4dInput(x, y, z, t)
        input = self.normalizedNoise(input)

        return input

    def rangeNoise4d(self, x, y, z, t, minimum, maximum):
        input = noise_squirrel5.__get4dInput(x, y, z, t)
        input = self.rangeNoise(input, minimum, maximum)

        return input

    def rangeNoiseInt4d(self, x, y, z, t, minimum, maximum):
        input = noise_squirrel5.__get4dInput(x, y, z, t)
        input = self.rangeNoiseInt(input, minimum, maximum)

        return input

    def noiseBool4d(self, x, y, z, t):
        input = noise_squirrel5.__get4dInput(x, y, z, t)
        input = self.noiseBool(input)

        return input

    def noiseBoolThreshold4d(self, x, y, z, t, threshold: float):
        input = noise_squirrel5.__get4dInput(x, y, z, t)
        input = self.noiseBoolThreshold(input, threshold)
        
        return input

    def randomInt(self):
        self.position += 1

        return self.noise(self.position)

    def randomIntRange(self, minimum, maximum):
        self.position += 1

        return self.rangeNoiseInt(self.position, minimum, maximum)
    
    def randomFloatRange(self, minimum, maximum):
        self.position += 1

        return self.rangeNoise(self.position, minimum, maximum)

    def randomBool(self):
        self.position += 1

        return self.noiseBool(self.position)

    def randomBoolPercentage(self, chance):
        self.position += 1
        
        return self.noiseBoolThreshold(self.position, chance)
    
    def randomNormalizedFloat(self):
        self.position += 1

        return self.normalizedNoise(self.position)

    
