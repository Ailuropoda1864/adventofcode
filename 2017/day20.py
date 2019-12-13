import re


TEST = '/home/fay/Downloads/test.txt'


# pt 1
def match_pattern(string):
    pattern = r'p=<(.+)>, v=<(.+)>, a=<(.+)>'
    match = re.match(pattern, string)
    return map(lambda x: [int(num) for num in x.split(',')],
               [match.group(1), match.group(2), match.group(3)])


def parse_particles(file):
    with open(file) as f:
        return {i: match_pattern(line) for i, line in enumerate(f)}


def update_attr(attr1, attr2):
    return [a1 + attr2[i] for i, a1 in enumerate(attr1)]


def simulation(particles, threshold=100):
    last_closest, closest = None, None
    count = 1

    while True:
        min_distance = float('inf')
        for i, particle in particles.items():
            p, v, a = particle
            v = update_attr(v, a)
            p = update_attr(p, v)
            particles[i] = [p, v, a]
            distance = sum(map(abs, p))
            if distance < min_distance:
                min_distance = distance
                closest = i

        count = count + 1 if last_closest == closest else 1

        if count >= threshold:
            return closest

        last_closest = closest


# pt 2
def collision(particles, threshold=100):
    count = 1

    while True:
        collide_pstn, collide_ptcl = {}, {}
        num_particles = len(particles)
        for i, particle in particles.items():
            p, v, a = particle
            v = update_attr(v, a)
            p = update_attr(p, v)
            particles[i] = [p, v, a]
            collide_pstn[tuple(p)] = collide_pstn.get(tuple(p), 0) + 1
            collide_ptcl[tuple(p)] = collide_ptcl.get(tuple(p), []) + [i]

        for pos, num in collide_pstn.items():
            if num > 1:
                for i in collide_ptcl[pos]:
                    del particles[i]

        count = count + 1 if num_particles == len(particles) else 1

        if count >= threshold:
            return len(particles)


def main():
    # pt 1
    particles = parse_particles(TEST)
    print(simulation(particles, 5000))

    # pt 2
    print(collision(particles, 500))


if __name__ == '__main__':
    main()