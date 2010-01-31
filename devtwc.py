import mangler
config = {
        'log_level': 'DEBUG',
        'auth_systems': ['tiddlywebplugins.wikidata.loginform'],
        'server_store': ['tiddlywebplugins.diststore', { 
             'main': ['text', {'store_root': 'store'}], 
             'extras': [ 
                 (r'^avox$', ['tiddlywebplugins.mappingsql',
                     {'db_config': 'mysql://avox@localhost/avox?charset=utf8'}]), 
                     #{'db_config': 'sqlite:///test.db'}]), 
                     ], 
                 }],
        # 'server_store': ['mappingsql', {'db_config': 'mysql://avox@localhost/avox?charset=utf8'}],
        'secret': 'the bees are in the what',
        'system_plugins': [
            'tiddlywebplugins.wikidata',
            'tiddlywebplugins.methodhack',
            'tiddlywebplugins.pathinfohack',
            'tiddlywebplugins.status',
            'tiddlywebplugins.static',
            'tiddlywebplugins.logout'],
        'maps_api_key': 'ABQIAAAAfIA5i-5lcivJMUvTzLDrmxQg7wZe1qASdla1M-DFyiqfOoWRghT6gGJohIOLIoy-3oR7sKWQfPvlxA', # http://wiki-data.com/
        'mappingsql.table': 'avox',
        'mappingsql.bag': 'avox',
        'mappingsql.id_column': 'avid',
        'mappingsql.open_fields': [
             'avid',
             'legal_name',
             'previous_name_s_',
             'trades_as_name_s_',
             'trading_status',
             'company_website',
             'registered_country',
             'operational_po_box',
             'operational_floor',
             'operational_building',
             'operational_street_1',
             'operational_street_2',
             'operational_street_3',
             'operational_city',
             'operational_state',
             'operational_country',
             'operational_postcode'
        ],
        'mappingsql.default_search_fields': [
             'legal_name',
             'previous_name_s_',
             'trades_as_name_s_',
        ],
        'mappingsql.full_text': True,
        'mappingsql.limit': 51,
        }
