import election, typing, itertools
import csv

class StateData:
    '''
    @author: James Petullo (Ajax1234)
    '''
    _csv_state_ids = {'Alabama': '1', 'Alaska': '2', 'Arizona': '4', 'Arkansas': '5', 'California': '6', 'Colorado': '8', 'Connecticut': '9', 'Delaware': '10', 'District of Columbia': '11', 'Florida': '12', 'Georgia': '13', 'Hawaii': '15', 'Idaho': '16', 'Illinois': '17', 'Indiana': '18', 'Iowa': '19', 'Kansas': '20', 'Kentucky': '21', 'Louisiana': '22', 'Maine': '23', 'Maryland': '24', 'Massachusetts': '25', 'Michigan': '26', 'Minnesota': '27', 'Mississippi': '28', 'Missouri': '29', 'Montana': '30', 'Nebraska': '31', 'Nevada': '32', 'New Hampshire': '33', 'New Jersey': '34', 'New Mexico': '35', 'New York': '36', 'North Carolina': '37', 'North Dakota': '38', 'Ohio': '39', 'Oklahoma': '40', 'Oregon': '41', 'Pennsylvania': '42', 'Rhode Island': '44', 'South Carolina': '45', 'South Dakota': '46', 'Tennessee': '47', 'Texas': '48', 'Utah': '49', 'Vermont': '50', 'Virginia': '51', 'Washington': '53', 'West Virginia': '54', 'Wisconsin': '55', 'Wyoming': '56', 'Puerto Rico': '72'}
    _states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
    _missing = 'Minnesota'
    _parties = {'Bernie Sanders': 'Democrat', 'Uncommitted': 'N/A', 'No Preference': 'N/A', 'Carly Fiorina': 'Republican', 'Rand Paul': 'Republican', 'Ted Cruz': 'Republican', 'Marco Rubio': 'Republican', 'Ben Carson': 'Republican', 'Chris Christie': 'Republican', 'Rick Santorum': 'Republican', 'Donald Trump': 'Republican', 'Jeb Bush': 'Republican', "Martin O'Malley": 'Democrat', 'John Kasich': 'Republican', 'Mike Huckabee': 'Republican', 'Hillary Clinton': 'Democrat'}
    @classmethod
    def state_winner(cls, _cand, _row:typing.List[dict]) -> str:
        _all_results = {i:sum(_c['Vote Data'][i]['Number of Votes'] for _c in _row) for i in _cand}
        return max(_all_results, key=lambda x:_all_results[x])
    @classmethod
    def county_winner(cls, _row:dict) -> str:
        return max(_row['Vote Data'], key=lambda x:_row['Vote Data'][x]['Number of Votes'])
    @classmethod
    def _top_results(cls,_state:str, _row:list, _find = {'Donald Trump', 'Hillary Clinton'}, val = 2) ->typing.Tuple:
        
        _sorted = sorted(_row, key=lambda x:x[-1])
        try:
        #print('republican', [[a, b] for a, b in _sorted if cls._parties[a] == 'Republican'])
        #print('democrate', [[a, b] for a, b in _sorted if cls._parties[a] == 'Democrat'])
            *_, [r1_name, _r1_p], [r2_name, _r2_p] = [[a, b] for a, b in _sorted if cls._parties[a] == 'Republican']
            *_, [d1_name, _d1_p], [d2_name, _d2_p] = [[a, b] for a, b in _sorted if cls._parties[a] == 'Democrat']
            return {'Trump':0 if all(c != 'Donald Trump' for c in [r1_name, r2_name]) else [-1, 1][r2_name == 'Donald Trump']*(_r2_p-_r1_p), 'Hillary Clinton':0 if all(c != 'Hillary Clinton' for c in [d1_name, d2_name]) else [-1, 1][d2_name == 'Hillary Clinton']*(_d2_p-_d1_p)}
        except ValueError:
            return {'Trump':0, 'Hillary Clinton':0}
        
full_data = election.get_results()
#print(full_data[0])
_all_candidates = {i for b in full_data for i in b['Vote Data'] if i not in {'Uncommitted', 'No Preference'}}
#print(_all_candidates)
_nationwide = {i:sum(c['Vote Data'][i]['Number of Votes'] for c in full_data) for i in _all_candidates} #1
_all_states = {c['Location']['State'] for c in full_data}
_state_percentages = {i:(lambda x:[[[h, _i[h]['Percent of Votes']] for h in _all_candidates] for _i in x])([c['Vote Data'] for c in full_data if c['Location']['State'] == i]) for i in StateData._states}
new_groups = {a:[[c, (lambda _h:sum(_h)/float(len(_h)))([j for _, j in d])] for c, d in itertools.groupby(sorted([h for t in b for h in t], key=lambda x:x[0]), key=lambda x:x[0])] for a, b in _state_percentages.items()}
margins = {a:StateData._top_results(a, b) for a,b in new_groups.items()} #2

_state_results = {i:[c for c in full_data if c['Location']['State'] == i] for i in StateData._states}
_state_grouped = {a:StateData.state_winner(_all_candidates, b) for a, b in _state_results.items()}
number_3 = {a:sum(StateData.county_winner(i) == _state_grouped[a] for i in b) for a, b in _state_results.items()} #3

print(_nationwide)
print('-'*30)
print(margins)
print('-'*30)
print(number_3)

'''
for a in StateData._states:
    print(a)
    print([a, StateData._csv_state_ids[a], margins[a]['Trump'], margins[a]['Hillary Clinton'], number_3[a]])
'''
#print([[a, b, _nationwide[a], margins[a]['Trump'], margins[a]['Clinton'], number_3[a]] for a, b in StateData._csv_state_ids.items()])
'''
with open('final_data_listing.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows([['state', 'id', 'Trump_margin', 'Clinton_margin', 'County'], *[[a, StateData._csv_state_ids[a], margins[a]['Trump'], margins[a]['Hillary Clinton'], number_3[a]] for a in StateData._states]])

'''
