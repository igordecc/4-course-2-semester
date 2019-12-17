

"""
load data/linear_w_noise.txt
S = linear_w_noise
N = length(S);
s1 = S(1:2:N-1) + sqrt(3)*S(2:2:N);
d1 = S(2:2:N) - sqrt(3)/4*s1 - (sqrt(3)-2)/4*[s1(N/2); s1(1:N/2-1)];
s2 = s1 - [d1(2:N/2); d1(1)];
s = (sqrt(3)-1)/sqrt(2) * s2;
d = -(sqrt(3)+1)/sqrt(2) * d1;

d

d1 = d * ((sqrt(3)-1)/sqrt(2));
s2 = s * ((sqrt(3)+1)/sqrt(2));
s1 = s2 + circshift(d1,-1);
S(2:2:N) = d1 + sqrt(3)/4*s1 + (sqrt(3)-2)/4*circshift(s1,1);
S(1:2:N-1) = s1 - sqrt(3)*S(2:2:N);

s
"""
def dobeshi(linear_w_noise):
    S = numpy.array(linear_w_noise)
    N = len(S);

    s1 = S[1:N - 1:2] + math.sqrt(3) * S[2: N:2];
    print(s1)
    print(s1[0:N // 2])
    print(len(s1[0:N // 2]))
    print(len(s1[0: N // 2 - 1]))
    d1 = S[2:N:2] - math.sqrt(3) / 4 * s1 - (math.sqrt(3) - 2) / 4 * numpy.concatenate(s1[0:N // 2], s1[0: N // 2 - 1])


    s2 = s1 - numpy.concatenate(d1[2:N / 2], d1[1]);
    s = (math.sqrt(3) - 1) / math.sqrt(2) * s2;
    d = -(math.sqrt(3) + 1) / math.sqrt(2) * d1;
    return d

import math
import numpy
linear_w_noise = []
with open("linear_w_noise.txt") as file:
    for line in file:
        linear_w_noise.append(float(line))
    dobeshi(linear_w_noise)


