

class Composite:

    @staticmethod
    def get():

        composites = {}

        composites['decomposition_move_method'] = {
            'name': 'Class Decomposition',
            'operations': [],
            'level': []
        }
        composites['decomposition_extract_method'] = {
            'name': 'Method Decomposition',
            'operations': [],
            'level': []
        }

        composites['composition_extract_method'] = {
            'name': 'Method Composition',
            'operations': [],
            'level': []
        }

        composites['composition_pull_up_method'] = {
            'name': 'Pull Up Method',
            'operations': [],
            'level': []
        }

        composites['decomposition_push_down_method'] = {
            'name': 'Push Down Method',
            'operations': [],
            'level': []
        }

        composites['decomposition_inline_method'] = {
            'name': 'Inline Method',
            'operations': [],
            'level': []
        }

        composites['composition_pull_up_field'] = {
            'name': 'Pull Up Field',
            'operations': [],
            'level': []
        }

        composites['decomposition_push_down_field'] = {
            'name': 'Push Down Field',
            'operations': [],
            'level': []
        }

        return composites
