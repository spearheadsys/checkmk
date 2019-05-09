# yapf: disable


checkname = 'oracle_locks'


info = [['TUX12C',
         '',
         '2985',
         'ora12c.local',
         'sqlplus@ora12c.local (TNS V1-V3)',
         '46148',
         'oracle',
         '633',
         'NULL',
         'NULL'],
        ['newdb',
         '25',
         '15231',
         'ol6131',
         'sqlplus@ol6131 (TNS V1-V3)',
         '13275',
         'oracle',
         'SYS',
         '3782',
         'VALID',
         '1',
         '407',
         '1463',
         'ol6131',
         'sqlplus@ol6131 (TNS V1-V3)',
         '13018',
         'oracle',
         'SYS']]


discovery = {'': [('TUX12C', {}), ('newdb', {})]}


checks = {'': [('TUX12C', {'levels': (1800, 3600)}, [(0, 'No locks existing', [])]),
               ('newdb',
                {'levels': (1800, 3600)},
                [(2,
                  'locktime 63 m (!!) Session (sid,serial, proc) 25,15231,13275 machine ol6131 osuser oracle object: . ; ',
                  [])])]}