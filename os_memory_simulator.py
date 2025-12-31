import matplotlib.pyplot as plt

def lru(pages, capacity):
    frames = []
    faults = 0
    for page in pages:
        if page not in frames:
            faults += 1
            if len(frames) == capacity:
                frames.pop(0)
            frames.append(page)
        else:
            frames.remove(page)
            frames.append(page)
    return faults

def optimal(pages, capacity):
    frames = []
    faults = 0
    for i, page in enumerate(pages):
        if page not in frames:
            faults += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                future = pages[i+1:]
                index = []
                for f in frames:
                    index.append(future.index(f) if f in future else float('inf'))
                frames[index.index(max(index))] = page
    return faults

if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
    capacity = 3

    print("LRU faults:", lru(pages, capacity))
    print("Optimal faults:", optimal(pages, capacity))

    plt.bar(["LRU", "Optimal"], [lru(pages, capacity), optimal(pages, capacity)])
    plt.title("Page Replacement Comparison")
    plt.ylabel("Page Faults")
    plt.show()
