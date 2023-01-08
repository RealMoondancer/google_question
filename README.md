# google_question
My version for https://www.youtube.com/watch?v=W_E0PoinCvo

Took 23.6655011177063 seconds to run, so 0.37 seconds faster than in the video

![image](https://user-images.githubusercontent.com/67159827/211216678-3f4cca2e-32b3-4c9b-a07c-73396be3e53a.png)

I also added a version that uses imports if they were allowed. This version uses the same function as without imports, but this time is compiled using the module numba. By adding the @jit decorator before the function it is compiled when it's first run. This makes the first run take longer, but all the others much faster.

It was able to complete the job in 6.44749 seconds.
