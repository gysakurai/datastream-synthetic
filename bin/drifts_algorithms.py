from random import randrange
import streamlit as st

limiar = 100

def backline():        
    print('\r', end='')

def abrupt(data_stream,perc_duration,ndiv):

    stream_size = len(data_stream)
    init = randrange(stream_size)
    indexes_start = []
    indexes_end = []
    success = True
    
    #Duration
    p = lambda x : x/100
    duration = p(perc_duration) * stream_size

    i = 0
    timeout = 0
    
    while init < stream_size and i <= ndiv-1:

        rand_duration = randrange(int(duration))
        interval = init + rand_duration

        data_stream[init:interval] = [1 for _ in range(rand_duration)]
        indexes_start.append(init)
        indexes_end.append(interval)

        try:
            init = randrange(interval,stream_size)
            i = i + 1
        except:
            init = randrange(stream_size)
            data_stream = [0] * int(stream_size)
            indexes_start = []
            indexes_end = []
            i = 0
            timeout = timeout + 1
            print(f"{timeout}/{limiar}", end='')                        # just print and flush
            backline()

            if timeout >= limiar:
                success = False
                break
            
            continue

    return data_stream, indexes_start, indexes_end, success

def gradual(data_stream,perc_duration,ndiv):
    
    stream_size = len(data_stream)
    init = randrange(stream_size)
    indexes_start = []
    indexes_end = []

    maior_indexes = 0

    i = 0
    timeout = 0
    interval = 0
    previous_duration = 0
    perc_atual = perc_duration
    success = True

    while init < stream_size and i <= ndiv-1:

        p = lambda x : x/100
        duration = p(perc_atual) * stream_size

        try:
            rand_duration = randrange(previous_duration + 1,int(duration))
            if rand_duration > previous_duration:
                previous_duration = rand_duration
            else:
                # print(f"{previous_duration} - {perc_atual} - {rand_duration}")
                continue
        
        except:
            if len(indexes_start) > maior_indexes: 
                # print(indexes_start,indexes_end)
                maior_indexes = len(indexes_start)

            init = randrange(stream_size)
            data_stream = [0] * int(stream_size)
            indexes_start = []
            indexes_end = []
            i = 0
            previous_duration = 0
            perc_atual = perc_duration
            
            timeout = timeout + 1
            print(f"{timeout}/{limiar}", end='')                        # just print and flush
            backline()

        interval = init + rand_duration

        data_stream[init:interval] = [1 for _ in range(rand_duration)]
        indexes_start.append(init)
        indexes_end.append(interval)

        try:
            init = randrange(interval,stream_size)
            # perc_atual = perc_atual + 0.5
            perc_atual = randrange(perc_atual, 100)
            i = i + 1
        except:
            if len(indexes_start) > maior_indexes: 
                # print(indexes_start,indexes_end)
                maior_indexes = len(indexes_start)

            init = randrange(stream_size)
            data_stream = [0] * int(stream_size)
            indexes_start = []
            indexes_end = []
            i = 0
            previous_duration = 0
            perc_atual = perc_duration
            
            timeout = timeout + 1
            print(f"{timeout}/{limiar}", end='')                        # just print and flush
            backline()

            if timeout >= limiar:
                success = False
                break
            
            continue

    return data_stream, indexes_start, indexes_end, success

def incremental(data_stream, perc_duration):

    stream_size = len(data_stream)

    #Duration
    p = lambda x : x/100
    duration = p(perc_duration) * stream_size
    indexes_start = []
    timeout = 0
    success = True

    while True:
        init = randrange(stream_size)
        duration = init + duration
        
        if duration > stream_size:
            init = randrange(stream_size)
            duration = p(perc_duration) * stream_size
            print(init, duration)
            continue
        
        else:
            signal = 0.1
            start = init
            r = 0
            while signal < 1 and r < duration:
                try:
                    r = randrange(start+1, duration)
                    data_stream[start:r] = [round(signal,1) for _ in range(r-start)]
                    start = r
                    signal = float(signal) + 0.1

                except Exception as e:
                    data_stream = [0] * int(stream_size)
                    signal = 0.1
                    start = init
                    
                    timeout = timeout + 1
                    print(f"{timeout}/{limiar}", end='')                        # just print and flush
                    backline()

                    if timeout >= limiar:
                        success = False
                        break

                    
                data_stream[r+1:stream_size] = [1 for _ in range(stream_size-r)]
            
            indexes_start.append(init)
            break

    return data_stream, indexes_start, success