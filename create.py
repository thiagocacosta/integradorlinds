    from date.conectar import cursor, conexao

    def inserir_sensor(tipo, mac, lat, long, loc, resp, status, obs, unid):
        try:
            inserir_sensor = f"""INSERT INTO app_smart_sensor(tipo, mac_address, latitude, longitude, localizacao, responsavel, status_operacional, observacao, unidade_medida)
            values
            ('{tipo}', '{mac}', '{lat}', '{long}', '{loc}', '{resp}', '{status}', '{obs}', '{unid}');"""
            cursor.execute(inserir_sensor)
            conexao.commit()
        except:
            print('Erro ao adicionar os sensor...')
        

    inserir_sensor("Optico", 0, -22.913075, -22.913075, 'LAB 500', 'Lindomar', 1, 'Sensor de teste', 'x')