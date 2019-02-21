checkname = 'docker_node_disk_usage'

info = [[
    '{"Active":"2"', '"Reclaimable":"8.674GB (90%)"', '"Size":"9.57GB"', '"TotalCount":"15"',
    '"Type":"Images"}'
],
        [
            '{"Active":"1"', '"Reclaimable":"1.224GB (99%)"', '"Size":"1.226GB"',
            '"TotalCount":"2"', '"Type":"Containers"}'
        ],
        [
            '{"Active":"1"', '"Reclaimable":"0B (0%)"', '"Size":"9.323MB"', '"TotalCount":"1"',
            '"Type":"Local Volumes"}'
        ],
        [
            '{"Active":"0"', '"Reclaimable":"0B"', '"Size":"0B"', '"TotalCount":"0"',
            '"Type":"Build Cache"}'
        ]]

discovery = {'': [('build cache', {}), ('containers', {}), ('images', {}), ('local volumes', {})]}

checks = {
    '': [('build cache', {}, [(0, 'size: 0 B', [('size', 0, None, None, None, None)]),
                              (0, 'reclaimable: 0 B', [('reclaimable', 0, None, None, None, None)]),
                              (0, 'count: 0', [('count', 0, None, None, None, None)]),
                              (0, 'active: 0', [('active', 0, None, None, None, None)])]),
         ('containers', {},
          [(0, 'size: 1169.20 MB', [('size', 1226000000, None, None, None, None)]),
           (0, 'reclaimable: 1167.30 MB', [('reclaimable', 1224000000, None, None, None, None)]),
           (0, 'count: 2', [('count', 2, None, None, None, None)]),
           (0, 'active: 1', [('active', 1, None, None, None, None)])]),
         ('images', {}, [(0, 'size: 8.91 GB', [('size', 9570000000, None, None, None, None)]),
                         (0, 'reclaimable: 8.08 GB', [('reclaimable', 8674000000, None, None, None,
                                                       None)]),
                         (0, 'count: 15', [('count', 15, None, None, None, None)]),
                         (0, 'active: 2', [('active', 2, None, None, None, None)])]),
         ('local volumes', {}, [(0, 'size: 8.89 MB', [('size', 9323000, None, None, None, None)]),
                                (0, 'reclaimable: 0 B', [('reclaimable', 0, None, None, None,
                                                          None)]),
                                (0, 'count: 1', [('count', 1, None, None, None, None)]),
                                (0, 'active: 1', [('active', 1, None, None, None, None)])])]
}
