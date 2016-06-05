#!/usr/bin/python

'''@base_data

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

from brain.database.save_feature import Save_Feature


def svm_feature_count(self, dataset):
    '''@save_feature_count

    This method saves the number of features that can be expected in a given
    observation with respect to 'id_entity'.

    @self.dataset[0], we assume that validation has occurred, and safe to
        assume the data associated with the first dataset instance is identical
        to any instance n within the overall collection of dataset(s).

    @self.dataset['count_features'], is defined within the 'dataset_to_dict'
        method.

    Note: this method needs to execute after 'dataset_to_dict'

    '''

    premodel_data = dataset
    db_save = Save_Feature({
        'id_entity': premodel_data['id_entity'],
        'count_features': premodel_data['count_features']
    })

    # save dataset element, append error(s)
    db_return = db_save.save_count()
    if db_return['error']:
        return {'error': db_return['error']}
    else:
        return {'error': None}