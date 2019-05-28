import pandas as pd
import random

# Global variables
alloc_matrix = []
physical_machine = pd.DataFrame(columns=['id', 'is_full', 'CPU', 'Memory', 'Network'])
virtual_machine = pd.DataFrame(columns=['id', 'is_placed', 'pm_id', 'CPU', 'Memory', 'Network'])


def getorder():
    pass


def place(vm, pm):
    pm['CPU'] += vm['CPU']
    pm['Memory'] += vm['Memory']
    pm['Network'] += vm['Network']
    # pm[-3:] += vm[-3:]
    if pm['CPU'] >= 1 or pm['Memory'] >= 1 or pm['Network'] > 1:
        pm[['CPU', 'Memory', 'Network']] -= vm[['CPU', 'Memory', 'Network']]
        return False
    else:
        alloc_matrix.append((pm['id'], vm['id']))
        return True


def planner():
    req_matrix = virtual_machine[virtual_machine['is_placed'] == False]
    for vm in req_matrix.iterrows():
        # todo implement "getorder()" function to apply heuristics
        order_of_pm_visit = physical_machine[physical_machine['is_full'] == False]

        for pm in order_of_pm_visit.iterrows():
            if place(vm[1], pm[1]):
                break
    return alloc_matrix


def update():
    df = pd.DataFrame(alloc_matrix)
    df.columns = ['pm id', 'vm id']
    for i in df.iterrows():
        virtual_machine.loc[i[1]['vm id'], 1:3] = True, i[1]['pm id']

    return df


def main():
    # test
    for i in range(10):
        physical_machine.loc[i] = i, False, random.randrange(0, 100) / 100.0,\
                                  random.randrange(0, 100) / 100.0, random.randrange(0, 100) / 100.0
    for i in range(100):
        virtual_machine.loc[i] = i, False, None,  random.randrange(0, 100)/100.0,\
                                 random.randrange(0, 100)/100.0, random.randrange(0, 100)/100.0

    planner()
    plan = update()
    # print(virtual_machine.sort_values(by=['pm_id']))
    print(physical_machine.sort_values(by=['CPU']))


if __name__ == '__main__':
    main()
