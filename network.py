def process_packets(buffer_size, n_packets, packets):
    """

    :param buffer_size:
    :param n_packets:
    :param packets:
    :return:
    """
    assert n_packets == len(packets), 'Not enough network packets received'

    buffer = []
    finish_times = []
    start_times = []

    for packet in packets:
        if len(buffer) <= buffer_size:
            packet_arr, packet_proc = packet
            buffer.append(packet)

            if len(finish_times) == 0:
                start_time = 0
            else:
                start_time = finish_times.pop(0)

            if start_time == packet_arr:
                start_times.append(start_time)

                finish_time = start_time + packet_proc
                finish_times.append(finish_time)

            else:
                start_times.append(-1)

    return start_times


buffer_size = 1
n_packets = 2
packets = [
    (0, 1),
    (0, 1)
]

res = process_packets(buffer_size, n_packets, packets)
print(res)
