from memory.short_term import ShortTermMemory
from memory.long_term import LongTermMemory


def test_short_term_memory():

    memory = ShortTermMemory()

    memory.add(
        "Kubernetes cluster analysis requested"
    )

    assert len(memory.get_all()) == 1



def test_long_term_memory():

    memory = LongTermMemory()

    memory.save(
        "cluster",
        "EKS production cluster"
    )

    assert memory.retrieve("cluster") == "EKS production cluster"