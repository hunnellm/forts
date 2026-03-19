def has_minimal_fort_size3(G):
    """Check if G has any minimal fort of size exactly 3."""
    vertices = list(G.vertices())

    def is_fort(S_set):
        for v in G.vertices():
            if v not in S_set:
                if sum(1 for u in G.neighbors(v) if u in S_set) == 1:
                    return False
        return True

    def is_minimal_fort(S_set):
        if not is_fort(S_set):
            return False
        S_list = list(S_set)
        for i in range(1, len(S_list)):
            for sub in Subsets(S_list, i):
                if is_fort(set(sub)):
                    return False
        return True

    for triple in Subsets(vertices, 3):
        if is_minimal_fort(set(triple)):
            return True, set(triple)
    return False, None

def fort_number(G):
    """Return the fort number (size of smallest fort) of G, or None if no fort exists."""
    vertices = list(G.vertices())

    def is_fort(S_set):
        for v in G.vertices():
            if v not in S_set:
                if sum(1 for u in G.neighbors(v) if u in S_set) == 1:
                    return False
        return True

    for size in range(1, len(vertices) + 1):
        for S in Subsets(vertices, size):
            if is_fort(set(S)):
                return size
    return None


def has_fort_number_3(G):
    """Return True if the smallest fort of G has size exactly 3."""
    return fort_number(G) == 3
