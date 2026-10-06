def _is_fort(G, S_set):
    """Return True if S_set is a fort: nonempty, and no vertex outside S
    has exactly one neighbor in S."""
    if not S_set:
        return False
    for v in G.vertices():
        if v not in S_set:
            if sum(1 for u in G.neighbors(v) if u in S_set) == 1:
                return False
    return True


def has_minimal_fort_size3(G):
    """Check if G has any minimal fort of size exactly 3."""
    vertices = list(G.vertices())

    def is_minimal_fort(S_set):
        if not _is_fort(G, S_set):
            return False
        S_list = list(S_set)
        for i in range(1, len(S_list)):
            for sub in Subsets(S_list, i):
                if _is_fort(G, set(sub)):
                    return False
        return True

    for triple in Subsets(vertices, 3):
        if is_minimal_fort(set(triple)):
            return True, set(triple)
    return False, None


def forts_of_size(G, k):
    """Return a list of all forts of G of size exactly k (each as a set)."""
    return [set(S) for S in Subsets(list(G.vertices()), k)
            if _is_fort(G, set(S))]


def all_forts(G):
    """Return a list of all forts of G, ordered by increasing size."""
    result = []
    for size in range(1, len(list(G.vertices())) + 1):
        result.extend(forts_of_size(G, size))
    return result


def fort_number(G):
    """Return the fort number (size of smallest fort) of G, or None if no fort exists."""
    vertices = list(G.vertices())
    for size in range(1, len(vertices) + 1):
        for S in Subsets(vertices, size):
            if _is_fort(G, set(S)):
                return size
    return None


def has_fort_number_3(G):
    """Return True if the smallest fort of G has size exactly 3."""
    return fort_number(G) == 3
