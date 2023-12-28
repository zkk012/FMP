from library.data.dataset import SequentialDataset, KnowledgeBasedDataset


class KGSeqDataset(SequentialDataset, KnowledgeBasedDataset):
    """Containing both processing of Sequential Models and Knowledge-based Models.

    Inherit from :class:`~library.data.dataset.sequential_dataset.SequentialDataset` and
    :class:`~library.data.dataset.kg_dataset.KnowledgeBasedDataset`.
    """

    def __init__(self, config):
        super().__init__(config)
