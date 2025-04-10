# -*- coding: utf-8 -*-
import os
import secrets
import random
import hashlib
import time

def entropy_seed():
    t = time.perf_counter_ns()
    pid = os.getpid()
    return int.from_bytes(os.urandom(8), 'big') ^ t ^ pid

class Gene:
    def __init__(self, value=None):
        self.value = value or secrets.token_bytes(32)
        self.mutation_logic = lambda x: hashlib.sha3_256(x).digest()

    def mutate(self):
        entropy = secrets.token_bytes(16) + time.perf_counter_ns().to_bytes(8, 'little')
        combined = self.value + entropy
        self.value = self.mutation_logic(combined)
        # шанс мутации самой мутации (!!!)
        if random.random() < 0.1:
            self.mutation_logic = self._mutate_logic()

    def _mutate_logic(self):
        funcs = [
            lambda x: hashlib.sha512(x).digest(),
            lambda x: hashlib.sha3_256(x).digest(),
            lambda x: hashlib.blake2b(x).digest(),
            lambda x: hashlib.sha1(x).digest()
        ]
        return random.choice(funcs)

class Chromosome:
    def __init__(self, num_genes=8):
        self.genes = [Gene() for _ in range(num_genes)]
        self.activity = random.random()

    def mutate(self, signal_strength):
        # сигнал влияет на вероятность мутаций
        for gene in self.genes:
            if random.random() < self.activity * signal_strength:
                gene.mutate()

    def signal(self):
        # генерирует внутреннюю активность (псевдохимия)
        raw = b''.join(g.value for g in self.genes)
        return sum(raw) % 256 / 255

class DigitalOrganism:
    def __init__(self, id, chromosomes=4, genes_per_chromo=8):
        self.id = id
        self.chromosomes = [Chromosome(genes_per_chromo) for _ in range(chromosomes)]
        self.age = 0
        self.traits = {}

    def interact(self, other):
        signal = other.signal()
        for chrom in self.chromosomes:
            chrom.mutate(signal)

    def signal(self):
        return sum(chrom.signal() for chrom in self.chromosomes) / len(self.chromosomes)

    def evolve(self):
        self.age += 1
        base_signal = self.signal()
        for chrom in self.chromosomes:
            chrom.mutate(base_signal)

    def genome_signature(self):
        genome = b''.join(g.value for c in self.chromosomes for g in c.genes)
        return hashlib.sha3_256(genome).hexdigest()

class ChaosEcosystem:
    def __init__(self, population=10):
        random.seed(entropy_seed())
        self.organisms = [DigitalOrganism(i) for i in range(population)]

    def cycle(self):
        for org in self.organisms:
            org.evolve()
        # взаимодействия случайны
        for _ in range(len(self.organisms) * 2):
            a, b = random.sample(self.organisms, 2)
            a.interact(b)

    def snapshot(self):
        return [org.genome_signature() for org in self.organisms]


