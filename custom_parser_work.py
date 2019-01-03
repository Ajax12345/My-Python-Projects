import abc, typing, collections, re
import json, copy, itertools
data = {'ID': '1234', 'Genres': [1, 2, 3], 'Nested1': [{'First': 'David', 'Last': 'Mark'}, {'First': 'Tony', 'Last': 'Scott'}], 'Value': {'[@Attrib]': {'Nested2': [{'Color': 'red', 'Age': 4}, {'Color': 'blue', 'Age': 5}]}}, 'Nested3': {'Member': {'Form': 'Five'}, 'Oven': {'Form': 'Seven'}}}



class _method_Description(abc.ABC):
    @abc.abstractmethod
    def flatten_list(self, _key:str) -> None:
        """
        Consense the "{_key}" list item
        """

    @abc.abstractmethod
    def repeat_list(self, _path:str) -> None:
        """
        Repeat the list elements into MULTIPLE items
        """

    @abc.abstractmethod
    def push_keys_to_list(self, _key:str, key_value:str='Value') -> None:
        """
        Create list from dict keys
        """

    

class DataUtility(_method_Description):
    def __init__(self, _data:dict=data) -> None:
        self._data, self._step_counter = _data, itertools.count(1)

    @classmethod
    def get_dot_path(cls, _tree:typing.Any, _path:typing.List[str]):
        if isinstance(_tree, dict):
            for a, b in _tree.items():
                yield from cls.get_dot_path(b, _path+[a])
        elif isinstance(_tree, list):
            if all(not isinstance(i, list) and not isinstance(i, dict) for i in _tree):
                yield from [[_path, i] for i in _tree]
            else:
                for c in _tree:
                    yield from cls.get_dot_path(c, _path)
        else:
            yield [_path, _tree]


    @classmethod
    def update_in_place(cls, _d:dict, _target:str):
        _flag = False
        if isinstance(_d, list):
            for c in _d:
                cls.update_in_place(c, _target)
        else:
            for a, b in _d.items():
                if a == _target:
                    _results = [['.'.join(a), b] for a, b in cls.get_dot_path(b, [a])]
                    print('results here', _results)
                    _container = collections.defaultdict(list)
                    for c, d in _results:
                        _container[c].append(d)
                    _flag = [a, _container]
                else:
                    if isinstance(b, list):
                        if all(isinstance(i, list) or isinstance(i, dict) for i in b):
                            for c in b:
                                if isinstance(c, dict):
                                    cls.update_in_place(c, _target)
                    else:
                        if isinstance(b, dict):
                            cls.update_in_place(b, _target)
            
            if _flag:
                a, _container = _flag
                del _d[a]
                _d.update(dict(_container))



           
    @classmethod
    def find_start_path(cls, _d:typing.Any, _path:typing.List[str]):
        if isinstance(_d, dict):
            if _path[0] in _d:
                _new_data = _d[_path[0]]
                for i in _path[1:]:
                    _new_data = _new_data[i]
                
                _flattened = [['.'.join(a), b] for a, b in cls.get_dot_path(_new_data, _path)]
                _container = collections.defaultdict(list)
                for a, b in _flattened:
                    _container[a].append(b)

                _grouped = list(zip(*[[[a, i] for i in b] for a, b in _container.items()]))
                del _d[_path[0]]
                yield [{**_d, **dict(i)} for i in _grouped]
                
                

            else:
                for _, b in _d.items():
                    yield from cls.find_start_path(b, _path)

        elif isinstance(_d, list) and all(isinstance(i, list) or isinstance(i, dict) for i in _d):
            for c in _d:
                yield from cls.find_start_path(c, _path)
        
        

    @classmethod
    def flatten_keys(cls, _d:typing.Any, _target:str, _replace_with:int) -> None:
        if isinstance(_d, list) and all(isinstance(i, list) or isinstance(i, dict) for i in _d):
            for c in _d:
                cls.flatten_keys(c, _target, _replace_with)
        elif isinstance(_d, dict):
            for a, b in _d.items():
                if a == _target:
                    _d[a] = [{_replace_with:c, **d} for c, d in b.items()]
                else:
                    cls.flatten_keys(b, _target, _replace_with)


    def flatten_list(self, _key:str) -> None:
        self.__class__.update_in_place(self._data, _key)
        if not isinstance(self._data, list):
            self._data = [self._data]

    def repeat_list(self, _path:str) -> None:
        _full_path = re.findall('\[@\w+\]|\w+', _path)
        self._data = [i for b in self.__class__.find_start_path(self._data, _full_path) for i in b]
        
        

    def push_keys_to_list(self, _key:str, key_value:str='Value') -> None:
        self.__class__.flatten_keys(self._data, _key, key_value)

    def flush(self) -> None:
        print('{}Step {}{}'.format('-'*6, next(self._step_counter), '-'*6))
        print(json.dumps(self._data, indent=4))

d = DataUtility(data)
d.flatten_list("Genres")
d.flush()
d.flatten_list("Nested1")
d.flush()
d.repeat_list("Value[@Attrib].Nested2")
d.flush()

d.push_keys_to_list("Nested3", key_value="Territory")
d.flush()
d.repeat_list("Nested3")
d.flush()
