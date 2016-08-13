import pandas as pd

def process_probas(model, pred_probas, raw_test_set):
    submission = pd.DataFrame(pred_probas, columns=model.classes_)
    submission['ID'] = raw_test_set['ID']
    return submission[['ID', 'Adoption', 'Died', 'Euthanasia', 'Return_to_owner', 'Transfer']]
