from __future__ import absolute_import, print_function
import numpy as np
import pyopencl as cl

#===========example ==================

a_np = np.random.rand(50000).astype(np.float32)
b_np = np.random.rand(50000).astype(np.float32)

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

mf = cl.mem_flags
a_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_np)
b_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b_np)

prg = cl.Program(ctx, """
__kernel void sum(
    __global const float *a_g, __global const float *b_g, __global float *res_g)
{
  int gid = get_global_id(0);
  res_g[gid] = a_g[gid] + b_g[gid];
}
""").build()

res_g = cl.Buffer(ctx, mf.WRITE_ONLY, a_np.nbytes)
prg.sum(queue, a_np.shape, None, a_g, b_g, res_g)

res_np = np.empty_like(a_np)
cl.enqueue_copy(queue, res_np, res_g)

# Check on CPU with Numpy:
print(res_np - (a_np + b_np))
print(np.linalg.norm(res_np - (a_np + b_np)))
#=====================================

#=========simple_map=======
import numpy as np
data = [np.random.rand(50000).astype(np.float32),
    np.random.rand(50000).astype(np.float32),
]

Prog = """
__kernel void sum(
    __global const float *a_g, __global const float *b_g, __global float *res_g)
{
  int gid = get_global_id(0);
  res_g[gid] = a_g[gid] + b_g[gid];
}
"""

def simple_clmap(Prog, data):


    ctx = cl.create_some_context()
    queue = cl.CommandQueue(ctx)

    mf = cl.mem_flags
    buffers = [cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=data_piece) for data_piece in data]

    prg = cl.Program(ctx, Prog).build()

    res_g = cl.Buffer(ctx, mf.WRITE_ONLY, a_np.nbytes)
    prg.sum(queue, a_np.shape, None, *buffers, res_g)

    res_np = np.empty_like(a_np)
    cl.enqueue_copy(queue, res_np, res_g)
    return res_np


simple_clmap(Prog, data)

# Check on CPU with Numpy:
print(res_np - (a_np + b_np))
print(np.linalg.norm(res_np - (a_np + b_np)))


