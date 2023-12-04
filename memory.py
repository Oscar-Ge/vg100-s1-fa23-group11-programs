import gc

print(gc.mem_free() / 1024) # stack mem

import Maix

print(Maix.utils.heap_free() / 1024) # heap mem
