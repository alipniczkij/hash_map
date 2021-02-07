from hash_map.main import HashMap
import random

def test_hashmap_01():
    hashmap = HashMap(10)
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ())]
    for k, v in entries:
        assert hashmap._get_hash(k) == hash(k)
        assert hashmap._get_hash(v) == hash(v)
    for k, v in entries:
        assert hashmap._get_index(hashmap._get_hash(k)) == hash(k) % 10
        assert hashmap._get_index(hashmap._get_hash(v)) == hash(v) % 10

def test_hashmap_02():
    hashmap = HashMap(10)
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ())]
    for k, v in entries:
        hashmap.put(k, v)
    assert len(hashmap) == 5
    for k, v in entries:
        hashmap.put(k, v)
    assert len(hashmap) == 5
    for k, v in entries:
        assert k in hashmap


def test_hashmap_03():
    hashmap = HashMap(10)
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ())]
    inner_list_name = [k for k, v in hashmap.__dict__.items() if isinstance(v, list)][0]
    for k, v in entries:
        hashmap.put(k, v)
    for k, v in entries:
        assert HashMap.Entry(k, None) in hashmap.__dict__[inner_list_name][hashmap._get_index(hashmap._get_hash(k))]


def test_hashmap_04():
    hashmap = HashMap(10)
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ()), ({"s": "v"}, {"v": "s"})]
    for k, v in entries:
        entry = HashMap.Entry(k, v)
        assert entry.get_key() == k
        assert entry.get_value() == v

    for i in range(len(entries)):
        entry_one = HashMap.Entry(entries[i][0], entries[i][1])
        for _ in range(10):
            j = random.randint(0, len(entries) - 1)
            p = random.randint(0, len(entries) - 1)
            entry_two = HashMap.Entry(entries[j][0], entries[p][1])
            if j == i:
                assert entry_one == entry_two
            else:
                assert entry_one != entry_two


def test_hashmap_05():
    hashmap = HashMap(10)
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ())]
    for k, v in entries:
        hashmap.put(k, v)
    for k, v in entries:
        assert hashmap.get(k) == v
    for _ in range(100):
        i = random.randint(0, len(entries) - 1)
        j = random.randint(0, len(entries) - 1)
        hashmap.put(i, j)
        assert hashmap.get(i) == j
    assert hashmap.get("nexit", "default") == "default"


def test_hashmap_06():
    hashmap = HashMap(10)
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ())]
    for k, v in entries:
        hashmap.put(k, v)
    output_values = set()
    output_keys = set()
    for v in hashmap.values():
        output_values.add(v)
    for k in hashmap.keys():
        output_keys.add(k)
    for k, v in entries:
        assert k in output_keys
        assert v in output_values
    output_values = set()
    output_keys = set()
    for k, v in hashmap.items():
        output_values.add(v)
        output_keys.add(k)
    for k, v in entries:
        assert k in output_keys
        assert v in output_values


def test_hashmap_07():
    hashmap = HashMap(2)
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ())]
    for k, v in entries:
        hashmap.put(k, v)
    assert len(hashmap) == 5
    for k, v in entries:
        hashmap.put(k, v)
    assert len(hashmap) == 5
    for k, v in entries:
        assert k in hashmap
