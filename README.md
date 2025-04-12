# eveline

eveline library inspired by the biology of living organisms, micro-level randomness, pseudo-organism interactions and gene mutations. It models a complex ecosystem with interdependent organisms, where each new state depends on the previous one, similar to a real evolutionary algorithm.


Cryptography
The eveline library provides both controlled and completely random ecosystem development. Since an ecosystem is essentially evolving chaos, the library can be used for purposes to create random keys, hashes, bytes, etc. 
!  We strongly recommend that you do not even try to use this library for cryptography like encryption methods and others. The system is chaotic and non-deterministic, and its algorithms are completely irreversible, you risk losing data forever.


Mathematical model of the final result:


The system is described as:

$P$ - number of organisms.

$C$ - number of chromosomes per organism.

$G$ - number of genes per chromosome.

$t$ - time step.


$O_i^t$ - state of organism i at time t

$C_j^i(t)$ - j-th chromosome of organism i

$G_k^j(t)$ - k-th gene in chromosome j of organism i


Signal (body activity)


$S_i(t) = (1 / C) * Σ σ(C_j^i(t))$

Where:

$σ(C)$ is the sum of gene values in chromosome C normalized to the range [0, 1].


Gene mutation


$G_k^j(t+1) = μ_k(t)(G_k^j(t) ⊕ E_t)$

Where:

$μ_k(t)$ - mutation function at time t.

$E_t$ - entropy of the current step (time, random, os.urandom, etc.).

$⊕$ - XOR operation (bitwise random mutation).


Metamutation


$μ_k(t+1) = M(μ_k(t))$

M(...) is a function that randomly changes the current mutation (e.g., changing SHA3 to BLAKE2).


Interaction of organisms


$G_k^j(t+1) = μ_k(t)(G_k^j(t) ⊕ S_j(t) ⊕ E'_t)$

Where $S_j(t)$ is the signal of the interacting organism, $E'_t$ is the new entropy portion.


A general model of evolution


$O_i^{t+1} = f(O_i^t, S_i^t, {S_j^t}_{j≠i}, E_t, μ(t), M(μ), I_t)$

Where:

$f$ is the final transformation function of the organism.

$I_t$ - map of interactions in step t.


The exponential growth of chao


$|F(t)| ∝ (2^256)^(G × C × P × t)$

That is, the number of possible states of the system at the t-th step is unimaginably large.


